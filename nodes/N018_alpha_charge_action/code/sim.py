"""Conditional alpha diagnostics. Benchmark is never a model normalization."""
import argparse
import json
import math

TARGET_INVERSE=137.035999177
TARGET_UNCERTAINTY=0.000000021

def alpha_from_shape(eta_em, C_Q, C_U):
    if not all(math.isfinite(v) for v in (eta_em,C_Q,C_U)) or eta_em<0 or C_U<=0:
        raise ValueError('Require finite eta_em>=0, finite charge coefficient, C_U>0')
    return 4*math.pi*eta_em*C_Q**2/C_U

def profile_energy(steps=8192):
    # xi-radius=tan(t): original infinite integral becomes sin(t)^4.
    h=math.pi/(2*steps)
    return 2*math.pi*h/3*sum((1 if i in (0,steps) else 4 if i%2 else 2)*math.sin(i*h)**4
                             for i in range(steps+1))

def enclosed_coefficient(radius):
    return radius**3/(1+radius**2)**1.5

def profile_charge_integral(steps=8192):
    # Integral rho dV/(4pi eps0 E_* L^2); r=tan(t).
    h=math.pi/(2*steps)
    return h/3*sum((1 if i in (0,steps) else 4 if i%2 else 2)*
                   3*math.sin(i*h)**2*math.cos(i*h) for i in range(steps+1))

def compare(candidate_inverse=None):
    out=dict(status='not_derived',predicted_inverse=None,residual=None,
             residual_in_benchmark_uncertainties=None)
    if candidate_inverse is not None:
        if not math.isfinite(candidate_inverse) or candidate_inverse<=0:
            raise ValueError('Candidate inverse must be finite and positive')
        d=candidate_inverse-TARGET_INVERSE
        out.update(status='supplied_not_derived',predicted_inverse=candidate_inverse,
                   residual=d,residual_in_benchmark_uncertainties=d/TARGET_UNCERTAINTY)
    return out

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--candidate-inverse',type=float)
    args=parser.parse_args()
    cu=profile_energy()
    assert abs(cu-3*math.pi**2/8)<1e-11
    assert abs(profile_charge_integral()-1)<1e-11
    # Demonstrate a continuum without using TARGET_INVERSE as a fitting input.
    rows=[dict(eta_em=x,alpha=alpha_from_shape(x,1,cu)) for x in (0.001,0.01,0.1)]
    print(json.dumps(dict(benchmark=dict(inverse=TARGET_INVERSE,uncertainty=TARGET_UNCERTAINTY,
          source='CODATA 2022, benchmark only'),comparison=compare(args.candidate_inverse),
          diagnostic_profile=dict(classification='supplied_source_not_electron',
          C_Q=1,C_U_numeric=cu,C_U_exact=3*math.pi**2/8,
          charge_integral=profile_charge_integral(),amplitude_freedom=rows)),indent=2,sort_keys=True))
if __name__=='__main__':
    main()
