"""Deterministic CMB/standing Beltrami checks. Numerical checks supplement proofs."""
from __future__ import annotations
import cmath
import json
import math
from pathlib import Path

C = 299792458.0
HP = 6.62607015e-34
KB = 1.380649e-23
ZETA3 = 1.2020569031595942854


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def cross(a, b):
    return (a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2], a[0]*b[1]-a[1]*b[0])


def norm2(a):
    return sum(abs(x)**2 for x in a)


def scale(a, s):
    return tuple(s*x for x in a)


def add(a, b):
    return tuple(x+y for x,y in zip(a,b))


def planck_spectrum(nu, temperature):
    if nu < 0 or temperature <= 0:
        raise ValueError('nu >= 0 and T > 0 required')
    if nu == 0:
        return 0.0
    x = HP*nu/(KB*temperature)
    return 0.0 if x > 700 else 8*math.pi*HP*nu**3/(C**3*math.expm1(x))


def simpson(f, lo=0.0, hi=45.0, n=12000):
    if n % 2:
        raise ValueError('even subdivision count required')
    h=(hi-lo)/n
    return h/3*(f(lo)+f(hi)+sum((4 if i%2 else 2)*f(lo+i*h) for i in range(1,n)))


def thermal_values(temperature=2.725):
    i3=simpson(lambda x: x**3/math.expm1(x) if x else 0.0)
    i2=simpson(lambda x: x**2/math.expm1(x) if x else 0.0)
    return {'temperature_K':temperature,'energy_density_J_m3':8*math.pi*(KB*temperature)**4/(HP**3*C**3)*i3,
            'photon_density_m3':8*math.pi*(KB*temperature)**3/(HP**3*C**3)*i2,
            'integral_x3':i3,'integral_x2':i2,
            'energy_integral_relative_error':abs(i3/(math.pi**4/15)-1),
            'number_integral_relative_error':abs(i2/(2*ZETA3)-1)}


def beltrami_spatial(r, k=1.3):
    """Sum of three differently oriented curl+k modes, not a single z-wave."""
    x,y,z=r
    return (math.cos(k*z)-.4*math.sin(k*y),
            -math.sin(k*z)+.7*math.cos(k*x),
            -.7*math.sin(k*x)+.4*math.cos(k*y))


def standing_fields(r, t, k=1.3):
    """c=epsilon0=mu0=1 for this numerical test."""
    e=beltrami_spatial(r,k)
    return scale(e,math.cos(k*t)),scale(e,-math.sin(k*t))


def derivative(field, r, axis, h=1e-5):
    p=list(r); m=list(r); p[axis]+=h; m[axis]-=h
    return scale(add(field(p),scale(field(m),-1)),1/(2*h))


def curl(field,r):
    dx,dy,dz=[derivative(field,r,a) for a in range(3)]
    return (dy[2]-dz[1],dz[0]-dx[2],dx[1]-dy[0])


def divergence(field,r):
    return sum(derivative(field,r,a)[a] for a in range(3))


def dft(a):
    return tuple(sum(a[r]*cmath.exp(-2j*math.pi*j*r/3) for r in range(3))/math.sqrt(3) for j in range(3))


def cycle(a):
    return a[1:]+a[:1]


def projector(a,j):
    out=(0j,0j,0j); v=tuple(a)
    for r in range(3):
        out=add(out,scale(v,cmath.exp(-2j*math.pi*j*r/3)/3)); v=cycle(v)
    return out


def diagnostics():
    k=1.3; residual=0.; energy_error=0.; flux=0.; div=0.
    for r in [(0.2,.4,.9),(.8,-.3,.6),(-.7,.2,1.1)]:
        for t in [0.,.31,1.2,math.pi/(2*k)]:
            e,b=standing_fields(r,t,k); h=1e-5
            ep,bp=standing_fields(r,t+h,k); em,bm=standing_fields(r,t-h,k)
            dedt=scale(add(ep,scale(em,-1)),1/(2*h)); dbdt=scale(add(bp,scale(bm,-1)),1/(2*h))
            ce=curl(lambda x:standing_fields(x,t,k)[0],r); cb=curl(lambda x:standing_fields(x,t,k)[1],r)
            residual=max(residual,math.sqrt(norm2(add(ce,dbdt))),math.sqrt(norm2(add(cb,scale(dedt,-1)))))
            div=max(div,abs(divergence(lambda x:standing_fields(x,t,k)[0],r)),abs(divergence(lambda x:standing_fields(x,t,k)[1],r)))
            energy_error=max(energy_error,abs((norm2(e)+norm2(b))/2-norm2(beltrami_spatial(r,k))/2))
            flux=max(flux,math.sqrt(norm2(cross(e,b))))
    a=(1+.3j,-.2+.7j,.4-1.2j); ps=[projector(a,j) for j in range(3)]
    p_error=max(math.sqrt(norm2(add(projector(ps[l],j),scale(ps[l],-1 if j==l else 0)))) for j in range(3) for l in range(3))
    result={'thermal':thermal_values(),'maxwell_finite_difference_residual':residual,'max_divergence':div,
            'standing_energy_error':energy_error,'standing_flux_max':flux,'projector_algebra_error':p_error,
            'dft_norm_error':abs(norm2(a)-norm2(dft(a))),
            'projector_energy_error':abs(norm2(a)-sum(norm2(p) for p in ps)),
            'interpretation':'Exact representation and standing solution checked; no neutrino identity or attracting lock inferred.'}
    assert residual < 1e-8 and div < 1e-8 and energy_error < 1e-12 and flux < 1e-12
    assert p_error < 1e-12 and result['dft_norm_error'] < 1e-12
    assert result['thermal']['energy_integral_relative_error'] < 1e-9
    assert result['thermal']['number_integral_relative_error'] < 1e-9
    return result

if __name__=='__main__':
    result=diagnostics()
    path=Path(__file__).resolve().parents[1]/'results'/'diagnostics.json'
    path.parent.mkdir(exist_ok=True)
    path.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print(json.dumps(result,indent=2,sort_keys=True))
