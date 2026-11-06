#!/usr/bin/env python3
"""Build-time SVG polygon rounding. Coordinates must form a simple perimeter."""
import argparse
import json
import math

def f(x): return f'{x:.3f}'.rstrip('0').rstrip('.')
def pt(q): return ' '.join(map(f,q))
def rounded_polygon(poly, r=0.75):
    if len(poly)<3 or not math.isfinite(r) or r<=0:
        raise ValueError("At least three vertices and a positive finite radius are required")
    if any(len(q)!=2 or any(not math.isfinite(x) for x in q) for q in poly):
        raise ValueError("Vertices must contain two finite coordinates")
    corners=[]
    for i,b in enumerate(poly):
        a=poly[i-1];c=poly[(i+1)%len(poly)]
        u=(a[0]-b[0],a[1]-b[1]);v=(c[0]-b[0],c[1]-b[1])
        lu=math.hypot(*u);lv=math.hypot(*v)
        if lu==0 or lv==0: raise ValueError("Adjacent vertices must differ")
        u=tuple(x/lu for x in u);v=tuple(x/lv for x in v)
        theta=math.acos(max(-1,min(1,u[0]*v[0]+u[1]*v[1])))
        if abs(-u[0]*v[1]+u[1]*v[0])<1e-8: raise ValueError("Remove collinear or reversing vertices")
        d=r/math.tan(theta/2)
        if d>=min(lu,lv)/2: raise ValueError("Radius too large for an adjacent edge")
        start=(b[0]+u[0]*d,b[1]+u[1]*d);end=(b[0]+v[0]*d,b[1]+v[1]*d)
        sweep=1 if (-u[0]*v[1]+u[1]*v[0])>0 else 0
        corners.append((start,end,sweep))
    s='M'+pt(corners[0][0])
    for i,(start,end,sweep) in enumerate(corners):
        if i:s+=' L'+pt(start)
        s+=f' A{f(r)} {f(r)} 0 0 {sweep} '+pt(end)
    return s+' Z'

if __name__ == '__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--points', required=True, help='JSON list of [x,y] coordinates')
    parser.add_argument('--radius', type=float, default=.75)
    args=parser.parse_args()
    try:
        print(rounded_polygon(json.loads(args.points),args.radius))
    except (ValueError,TypeError) as exc:
        parser.error(str(exc))
