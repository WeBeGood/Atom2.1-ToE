"""Poisson fixed-fraction losses; exact moments checked by probability summation."""
import json
import math
from pathlib import Path


def moments(mu,kappa):
    if mu<0 or not 0<=kappa<1:
        raise ValueError('mu >= 0 and 0 <= kappa < 1 required')
    mean=math.exp(-mu*kappa)
    return mean,math.exp(mu*(-2*kappa+kappa*kappa)),math.sqrt(math.expm1(mu*kappa*kappa))


def poisson_sum(mu,kappa):
    if not 0<=mu<=100:
        raise ValueError('summation validation limited to mu in [0,100]')
    p=math.exp(-mu); mass=mean=second=0.
    for n in range(600):
        if n: p*=mu/n
        energy=(1-kappa)**n
        mass+=p; mean+=p*energy; second+=p*energy**2
    return mass,mean,second


def width_bound(z,width):
    if z<=0 or width<0: raise ValueError('positive z, nonnegative width required')
    return math.log1p(width*width)/math.log1p(z)


def diagnostics():
    kappa=1/8; mu=math.log(2)/kappa
    mean,second,cv=moments(mu,kappa); mass,m1,m2=poisson_sum(mu,kappa)
    a=(70000/3.085677581491367e22)/299792458
    result={'kappa':kappa,'loss_after_three':1-(1-kappa)**3,'mu_at_mean_half':mu,
            'surviving_mean_fraction':mean,'relative_rms_width':cv,'sd_over_initial_energy':mean*cv,
            'poisson_probability_sum':mass,'poisson_mean_error':abs(mean-m1),'poisson_second_moment_error':abs(second-m2),
            'a_loss_m_inverse':a,'sigma_m2_back_calibrated':a/(kappa*4.1e8),
            'log_energy_rate_over_mean_energy_rate':-math.log1p(-kappa)/kappa,
            'illustrative_kappa_bound_z1_width_0p001':width_bound(1.,.001),
            'interpretation':'Conditional independent-event statistics only; cross-section is inverse calibration and width limit illustrative.'}
    assert abs(mass-1)<1e-12 and abs(mean-m1)<1e-12 and abs(second-m2)<1e-12
    return result

if __name__=='__main__':
    result=diagnostics(); path=Path(__file__).resolve().parents[1]/'results'/'diagnostics.json'
    path.parent.mkdir(exist_ok=True); path.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print(json.dumps(result,indent=2,sort_keys=True))
