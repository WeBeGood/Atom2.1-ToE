"""Analytic/numerical counterexamples for energy-helicity and C3 claims."""
import cmath
import json
import math
from pathlib import Path


def spectrum(a,b):
    return [a+2*(b*cmath.exp(2j*math.pi*j/3)).real for j in range(3)]


def elastic_energy(length,tension,stiffness,twist):
    if length<=0 or tension<=0 or stiffness<=0:
        raise ValueError('positive length, tension and stiffness required')
    return tension*length+stiffness*twist**2/(2*length)


def diagnostics():
    # Numerical integrals for B=(cos kz,-sin kz,0), normalized mu0=1.
    k=2.; length=2*math.pi/k; n=4000; step=length/n
    ub=hb=bad=0.
    for j in range(n):
        z=(j+.5)*step; b=(math.cos(k*z),-math.sin(k*z),0.)
        a=tuple(x/k for x in b)
        ub+=sum(x*x for x in b)*step/2
        hb+=sum(x*y for x,y in zip(a,b))*step
        bad+=complex(sum(x*(k*x) for x in b)).imag*step
    tau=2.; stiffness=3.; theta=2*math.pi
    optimum=abs(theta)*math.sqrt(stiffness/(2*tau))
    center=elastic_energy(optimum,tau,stiffness,theta)
    results={'magnetic_energy':ub,'magnetic_helicity':hb,'energy_helicity_relative_error':abs(ub/(k*hb/2)-1),
             'grok_imaginary_formula':bad,'elastic_length_optimum':optimum,'elastic_energy_optimum':center,
             'elastic_neighbors_above_minimum':all(elastic_energy(optimum*f,tau,stiffness,theta)>center for f in [.7,.99,1.01,1.3]),
             'c3_spectrum_real_coupling':spectrum(4.,1.),'c3_spectrum_complex_coupling':spectrum(4.,1.+.4j),
             'two_equal_photons_120_mass_energy_over_E0':math.sqrt(2*(1-math.cos(2*math.pi/3))),
             'interpretation':'C3 eigenvalues depend on unspecified dynamics; elastic coefficients are illustrative, not fitted masses.'}
    assert results['energy_helicity_relative_error']<1e-12 and hb>0 and bad==0
    assert results['elastic_neighbors_above_minimum']
    return results

if __name__=='__main__':
    result=diagnostics(); path=Path(__file__).resolve().parents[1]/'results'/'diagnostics.json'
    path.parent.mkdir(exist_ok=True); path.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print(json.dumps(result,indent=2,sort_keys=True))
