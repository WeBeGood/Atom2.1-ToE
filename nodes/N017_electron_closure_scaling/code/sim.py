"""Geometry diagnostics only; no electron stability or charge prediction."""
import json
import math

def point(t, R, rho):
    if R <= 0 or not 0 < rho < 1:
        raise ValueError('Require R>0 and 0<rho<1')
    a = R*rho
    return (a*math.sin(3*t), (R+a*math.cos(3*t))*math.cos(2*t),
            (R+a*math.cos(3*t))*math.sin(2*t))

def length(R, rho, steps=8192):
    point(0, R, rho)
    if steps < 2 or steps % 2:
        raise ValueError('Simpson steps must be positive and even')
    h = 2*math.pi/steps
    def speed(t):
        return R*math.sqrt(4*(1+rho*math.cos(3*t))**2+9*rho**2)
    return h/3*sum((1 if i in (0,steps) else 4 if i%2 else 2)*speed(i*h)
                   for i in range(steps+1))

def polygon_length(R, rho, steps=32768):
    pts = [point(2*math.pi*i/steps,R,rho) for i in range(steps+1)]
    return sum(math.dist(a,b) for a,b in zip(pts,pts[1:]))

def main():
    rows=[]
    for rho in (0.1,0.3,0.6,0.9):
        f=length(1,rho)
        poly=polygon_length(1,rho)
        assert math.dist(point(0,1,rho),point(2*math.pi,1,rho))<1e-13
        assert abs(poly/f-1)<1e-7
        rows.append(dict(rho=rho,F=f,polygon_relative_error=poly/f-1,
                         beta_for_hypothetical_n1=1/f))
    print(json.dumps(dict(status='geometry_only_closure_open',rows=rows),indent=2,sort_keys=True))
if __name__=='__main__':
    main()
