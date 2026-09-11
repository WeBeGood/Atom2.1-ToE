import importlib.util
import math
from pathlib import Path
import pytest
R=Path(__file__).resolve().parents[1]
def load(node):
    spec=importlib.util.spec_from_file_location(node,R/'nodes'/node/'code/sim.py')
    m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m
cl=load('N017_electron_closure_scaling')
al=load('N018_alpha_charge_action')

@pytest.mark.parametrize('rho',[0.1,0.3,0.6,0.9])
def test_geometry_independent_polygon_and_scaling(rho):
    ell=cl.length(1,rho)
    assert math.dist(cl.point(0,1,rho),cl.point(2*math.pi,1,rho))<1e-13
    assert cl.polygon_length(1,rho)==pytest.approx(ell,rel=1e-7)
    assert cl.length(3,rho)==pytest.approx(3*ell,rel=1e-12)

@pytest.mark.parametrize('rho',[0.1,0.6])
def test_phase_closure_does_not_select_shape(rho):
    pitch=2.3;n=3
    beta=n/cl.length(1,rho)
    assert cl.length(beta*pitch,rho)==pytest.approx(n*pitch,rel=1e-12)

def test_radial_charge_and_energy_against_analytic_integrals():
    assert al.profile_energy()==pytest.approx(3*math.pi**2/8,rel=1e-12)
    assert al.profile_charge_integral()==pytest.approx(1,abs=1e-12)
    # Divergence theorem at finite radii: derivative of enclosed charge.
    for s in (0.2,1,3):
        h=1e-5
        derivative=(al.enclosed_coefficient(s+h)-al.enclosed_coefficient(s-h))/(2*h)
        assert derivative==pytest.approx(3*s*s/(1+s*s)**2.5,rel=1e-8)

def test_coordinate_and_shape_normalization_invariance():
    eta,cq,cu=0.07,-0.3,2.4
    alpha=al.alpha_from_shape(eta,cq,cu)
    for b in (0.2,3):
        assert al.alpha_from_shape(b*eta,cq/b**2,cu/b**3)==pytest.approx(alpha)
        assert al.alpha_from_shape(eta,b*cq,b*b*cu)==pytest.approx(alpha)

def test_continuum_zero_charge_and_no_fabricated_prediction():
    assert al.alpha_from_shape(0.1,0,2)==0
    assert al.alpha_from_shape(0.4,1,2)==pytest.approx(4*al.alpha_from_shape(0.1,1,2))
    assert al.compare()['predicted_inverse'] is None
    assert al.compare()['residual'] is None
    assert al.compare(al.TARGET_INVERSE)['status']=='supplied_not_derived'
    assert al.compare(al.TARGET_INVERSE)['residual']==0
    assert al.compare(al.TARGET_INVERSE+1)['residual']==pytest.approx(1)

@pytest.mark.parametrize('bad',[float('nan'),float('inf'),0,-1])
def test_invalid_benchmark_candidate(bad):
    with pytest.raises(ValueError):al.compare(bad)
