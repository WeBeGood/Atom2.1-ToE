"""Reproducible two-wave vector animation. Run from any directory.

Standard-library field model; Pillow required only to render. c=E0=k=1.
Electric-only and magnetic-only describe the selected y=z=0 line, not 3-D modes.
"""
from pathlib import Path
import math
import argparse

S=math.sqrt(3)/2
N=((.5,S,0),(.5,-S,0))
Z=((0,0,1),(0,0,1))
IN_PLANE=((S,-.5,0),(-S,-.5,0))
MODES=('Charge Only','Magnetic Only','EM-like')

def cross(a,b):
    return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def add(a,b): return tuple(x+y for x,y in zip(a,b))
def dot(a,b): return sum(x*y for x,y in zip(a,b))
def fields(mode,r,t):
    """Return ((E1,cB1),(E2,cB2),(Etotal,cBtotal)) at r,t."""
    pol=IN_PLANE if mode=='Charge Only' else Z
    delta=2*math.pi/3 if mode=='EM-like' else math.pi
    parents=[]
    for i in range(2):
        a=math.cos(dot(N[i],r)-t+i*delta)
        e=tuple(a*v for v in pol[i])
        parents.append((e,cross(N[i],e)))
    return (*parents,(add(parents[0][0],parents[1][0]),add(parents[0][1],parents[1][1])))

def verify():
    # Transversality, magnetic handedness and normalized plane-wave dispersion.
    for pol in (Z,IN_PLANE):
        for n,e in zip(N,pol):
            assert abs(dot(n,e))<1e-14
            assert abs(dot(cross(n,e),cross(n,e))-1)<1e-14
    for j in range(97):
        x=j*.137;t=j*.271;a=math.cos(.5*x-t)
        e,b=fields('Charge Only',(x,0,0),t)[2]
        assert max(abs(v) for v in b)<2e-14
        assert abs(e[0]-math.sqrt(3)*a)<2e-14 and abs(e[1])<2e-14
        e,b=fields('Magnetic Only',(x,0,0),t)[2]
        assert max(abs(v) for v in e)<2e-14
        assert abs(b[0]-math.sqrt(3)*a)<2e-14 and abs(b[1])<2e-14
    # Maxwell curl/divergence residuals throughout space, not just chosen line.
    h=1e-5
    for mode in MODES:
        for r in ((.3,.4,.7),(-.7,.2,.1)):
            t=.31
            grads=[]
            for axis in range(3):
                rp=list(r);rm=list(r);rp[axis]+=h;rm[axis]-=h
                fp=fields(mode,rp,t)[2];fm=fields(mode,rm,t)[2]
                grads.append(tuple(tuple((fp[f][k]-fm[f][k])/(2*h) for k in range(3)) for f in range(2)))
            fp=fields(mode,r,t+h)[2];fm=fields(mode,r,t-h)[2]
            dt=tuple(tuple((fp[f][k]-fm[f][k])/(2*h) for k in range(3)) for f in range(2))
            for f in range(2):
                assert abs(sum(grads[i][f][i] for i in range(3)))<1e-8
                curl=(grads[1][f][2]-grads[2][f][1],grads[2][f][0]-grads[0][f][2],grads[0][f][1]-grads[1][f][0])
                target=tuple(-v for v in dt[1]) if f==0 else dt[0]
                assert max(abs(a-b) for a,b in zip(curl,target))<1e-8
    print('PASS: plane-wave constraints, line cancellations, 3-D Maxwell residuals')

def render(out,frames=64):
    from PIL import Image,ImageDraw,ImageFont
    out.mkdir(parents=True,exist_ok=True)
    font_path='/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
    def font(s):
        try:return ImageFont.truetype(font_path,s)
        except OSError:return ImageFont.load_default()
    bg='#0b1324';fg='#e9f0fa';muted='#a8b8cf';blue='#58baff';red='#ff768b';green='#76e2b3'
    pictures=[]
    for frame in range(frames):
        im=Image.new('RGB',(1440,1080),bg);d=ImageDraw.Draw(im)
        def txt(x,y,s,size=19,color=fg):d.text((x,y),s,font=font(size),fill=color)
        def arrow(a,b,color,width=2):
            d.line((a,b),fill=color,width=width)
            dx=b[0]-a[0];dy=b[1]-a[1];l=math.hypot(dx,dy)
            if l<3:return
            ux=dx/l;uy=dy/l
            d.polygon((b,(b[0]-7*ux+3*uy,b[1]-7*uy-3*ux),(b[0]-7*ux-3*uy,b[1]-7*uy+3*ux)),fill=color)
        txt(35,20,'ATOM 2.1  |  Two parent waves -> one resultant field',31)
        txt(35,66,'120 degree crossing   /   x = selected seed-line axis   /   time advances; both parents remain present',20,muted)
        txt(35,102,'Electric E / E0',19,blue);txt(235,102,'Magnetic cB / E0',19,red)
        txt(535,102,'Arrows are field vectors; anchor positions lie on y = z = 0.',19,muted)
        t=2*math.pi*frame/frames
        for row,mode in enumerate(MODES):
            top=150+row*285
            txt(35,top,mode,25,green)
            subtitle=('In-plane parent E; relative phase 180 deg. B cancels on the selected line.' if row==0 else 'Common z-polarized parent E; relative phase 180 deg. E cancels on the selected line.' if row==1 else 'N015 common z polarization; relative phase 120 deg. Both E and B remain.')
            txt(35,top+34,subtitle,17,muted)
            for col in range(3):
                left=35+col*465;cy=top+153
                d.rounded_rectangle((left,top+69,left+440,top+270),radius=12,fill='#132139',outline='#293b55')
                txt(left+14,top+78,('Parent 1','Parent 2','Resultant: parent 1 + parent 2')[col],18)
                # Same spatial line in each column; no split-screen propagation illusion.
                arrow((left+20,cy),(left+420,cy),'#7f91aa')
                txt(left+414,cy+8,'x',16,muted)
                for j in range(15):
                    x=-2*math.pi+4*math.pi*j/14
                    px=left+37+365*j/14
                    e,b=fields(mode,(x,0,0),t)[col]
                    def project(v):return (px+23*v[0]+12*v[2],cy-30*v[1]-35*v[2])
                    arrow((px,cy),project(e),blue)
                    arrow((px,cy),project(b),red)
                # Coordinate triad encodes depth; x remains horizontal.
                a=(left+30,top+240)
                for v,label in (((28,0),'x'),((0,-22),'y'),((12,-16),'z')):
                    b=(a[0]+v[0],a[1]+v[1]);arrow(a,b,muted,1);txt(b[0]+2,b[1]-8,label,12,muted)
                if col<2:
                    txt(left+155,top+239,('n1 = (1/2, +sqrt(3)/2, 0)','n2 = (1/2, -sqrt(3)/2, 0)')[col],13,muted)
                else:
                    txt(left+112,top+239,('E along x; B = 0 on this line','B along x; E = 0 on this line','E along z; B in x-y plane')[row],14,green)
        txt(35,1020,'Local interference views, not demonstrated independent NewWave particles or photon fusion.',20,muted)
        txt(35,1050,'Charge-Only polarization extension: verified Maxwell algebra; pending project-ledger acceptance.',17,muted)
        pictures.append(im)
    pictures[0].save(out/'two_waves_three_views.gif',save_all=True,append_images=pictures[1:],duration=80,loop=0,optimize=False)
    pictures[0].save(out/'two_waves_three_views.png')
    for row,slug in enumerate(('charge_only','magnetic_only','em_like')):
        cropped=[]
        for im in pictures:
            card=Image.new('RGB',(1440,500),bg)
            card.paste(im.crop((0,0,1440,140)),(0,0))
            card.paste(im.crop((0,150+row*285,1440,150+(row+1)*285)),(0,140))
            card.paste(im.crop((0,1010,1440,1080)),(0,430))
            cropped.append(card)
        cropped[0].save(out/(slug+'.gif'),save_all=True,append_images=cropped[1:],duration=80,loop=0,optimize=False)
    print('Rendered to',out)

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--check',action='store_true');args=parser.parse_args()
    verify()
    if not args.check:render(Path(__file__).resolve().parent/'figs')
