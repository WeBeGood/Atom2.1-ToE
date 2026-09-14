"""Independent checks of the proposed field transformations and audit formulas."""
import cmath
import importlib.util
import math
from pathlib import Path
import pytest
ROOT=Path(__file__).resolve().parents[1]


def load(path):
    spec=importlib.util.spec_from_file_location(path,ROOT/path)
    module=importlib.util.module_from_spec(spec); spec.loader.exec_module(module)
    return module

cmb=load('nodes/N016_cmb_seeded_beltrami_line/code/sim.py')
eh=load('nodes/N019_energy_helicity_modes/code/sim.py')
tl=load('nodes/N020_tired_light_statistics/code/sim.py')


def test_maxwell_standing_solution_and_planck_integrals():
    d=cmb.diagnostics()
    assert 4e8<d['thermal']['photon_density_m3']<4.2e8
    assert 4e-14<d['thermal']['energy_density_J_m3']<4.3e-14
    assert cmb.planck_spectrum(0,2.725)==0
    assert cmb.planck_spectrum(160e9,2.725)>0


def test_curl_eigenvalue_for_arbitrary_phase_not_only_120():
    def f1(r): return (cmath.cos(r[2]),-cmath.sin(r[2]),0j)
    def f2(r): return (0j,cmath.cos(r[0]),-cmath.sin(r[0]))
    for phase in [0.,.17,2*math.pi/3,math.pi]:
        field=lambda r:cmb.add(f1(r),cmb.scale(f2(r),cmath.exp(1j*phase)))
        r=(.2,.7,-.4)
        assert cmb.norm2(cmb.add(cmb.curl(field,r),cmb.scale(field(r),-1)))<1e-17


def test_unitary_thermal_covariance_and_projector_reconstruction():
    # Form covariance explicitly from three orthonormal input basis vectors.
    basis=[tuple(float(i==j) for i in range(3)) for j in range(3)]
    outputs=[cmb.dft(v) for v in basis]
    for i in range(3):
        for j in range(3):
            value=sum(v[i]*v[j].conjugate() for v in outputs)
            assert abs(value-float(i==j))<1e-12
    a=(1+.2j,-.7j,1.3)
    reconstructed=tuple(sum(cmb.projector(a,j)[i] for j in range(3)) for i in range(3))
    assert cmb.norm2(cmb.add(reconstructed,cmb.scale(a,-1)))<1e-25


def test_local_energy_speed_inequality():
    for e,b in [((1.,2.,3.),(.4,-.3,.9)),((1.,0.,0.),(0.,1.,0.)),((1.,0.,0.),(1.,0.,0.))]:
        u=(cmb.norm2(e)+cmb.norm2(b))/2
        lhs=u*u-cmb.norm2(cmb.cross(e,b))
        rhs=((cmb.norm2(e)-cmb.norm2(b))**2+4*cmb.dot(e,b)**2)/4
        assert lhs==pytest.approx(rhs) and lhs>=-1e-12


def test_energy_helicity_and_elastic_minimum():
    assert eh.diagnostics()['magnetic_helicity']>0
    # Fixed total twist: nonuniform distribution has greater energy by Cauchy-Schwarz.
    length=2.; theta=3.; n=2000; ds=length/n
    integral=sum((theta/length+.4*math.cos(2*math.pi*(j+.5)/n))**2*ds for j in range(n))
    assert integral>theta**2/length


def test_c3_eigenpairs_from_explicit_matrix():
    a=4.; b=1.+.4j
    for j,kval in enumerate(eh.spectrum(a,b)):
        w=cmath.exp(2j*math.pi*j/3); v=(1.,w,w*w)
        kv=tuple(a*v[i]+b*v[(i+1)%3]+b.conjugate()*v[(i-1)%3] for i in range(3))
        assert max(abs(kv[i]-kval*v[i]) for i in range(3))<1e-12


@pytest.mark.parametrize('mu,kappa',[(0.,.125),(.7,.01),(math.log(2)*8,.125),(12.,.3)])
def test_poisson_moments_against_distribution(mu,kappa):
    mean,second,cv=tl.moments(mu,kappa)
    mass,m1,m2=tl.poisson_sum(mu,kappa)
    assert mass==pytest.approx(1.)
    assert mean==pytest.approx(m1,abs=1e-14)
    assert second==pytest.approx(m2,abs=1e-14)
    assert cv**2==pytest.approx(m2/m1**2-1,abs=1e-13)


def test_corrected_width_and_continuous_limit():
    d=tl.diagnostics()
    assert d['loss_after_three']==169/512
    assert d['relative_rms_width']==pytest.approx(.30084503097983467)
    assert tl.moments(math.log(2)/1e-7,1e-7)[2]<.001
    assert tl.width_bound(1.,.001)==pytest.approx(math.log(1.000001)/math.log(2))
