#-*- coding:utf-8 -*-
# point / vectpr structure by SnapFlip20

from math import acos, degrees, fabs, sin, sqrt

class point:
    def __init__(self, x=0, y=0, z=0):
        if isinstance(x, (list, tuple, point)):
            if len(x) == 1: # 1D
                _cv = [x[0], 0, 0]
                x, y, z = _cv
            elif len(x) == 2: # 2D
                _cv = [x[0], x[1], 0]
                x, y, z = _cv
            elif len(x) == 3: # 3D
                _cv = [x[0], x[1], x[2]]
                x, y, z = _cv
        self.v = [x, y, z]
        self.x = x
        self.y = y
        self.z = z

    @classmethod
    def invert(cls, v):
        if not isinstance(v, list):
            raise TypeError
        cv = cls()
        cv.v = v
        return cv

    def __repr__(self):
        comp = ', '.join([repr(x) for x in self.v])
        return f'{type(self).__name__}({comp})'
    
    def __str__(self):
        comp = ', '.join([str(x) for x in self.v])
        return f'point({comp})'

    def __pos__(self):
        return self

    def __neg__(self):
        return point(-self.x, -self.y, -self.z)
    
    def __eq__(self, other):
        if not isinstance(other, point):
            raise TypeError
        return self.v == other.v

    def __lt__(self, other):
        if self.z < other.z:
            return True
        elif self.z > other.z:
            return False
        else:
            if self.y < other.y:
                return True
            elif self.y > other.y:
                return False
            else:
                if self.x < other.x:
                    return True
                else:
                    return False

    def __ne__(self, other):
        if not isinstance(other, point):
            raise TypeError
        return self.v != other.v

    def __len__(self):
        return len(self.v)
    
    def __getitem__(self, i):
        if i > 2:
            raise IndexError
        return self.v[i]

    def area(lst):
        ...

    def ccw(a, b, c):
        a_b = vector.to_vector(a, b)
        b_c = vector.to_vector(b, c)
        return vector.cross(a_b, b_c)[2]

    def dist(a, b):
        return sqrt((a.x-b.x)**2 + (a.y-b.y)**2 + (a.z-b.z)**2)

    def dist2(a, b):
        return (a.x-b.x)**2 + (a.y-b.y)**2 + (a.z-b.z)**2

    def dist_taxi(a, b):
        return fabs(a.x-b.x) + fabs(a.y-b.y) + fabs(a.z-b.z)

    def flipx(self):
        return point(-self.x, self.y, self.z)

    def flipy(self):
        return point(self.x, -self.y, self.z)

    def flipz(self):
        return point(self.x, self.y, -self.z)

    def flipxy(self):
        return point(-self.x, -self.y, self.z)

    def flipxz(self):
        return point(-self.x, self.y, -self.z)

    def flipyz(self):
        return point(self.x, -self.y, -self.z)

    def flipxyz(self):
        return point(-self.x, -self.y, -self.z)
    
    def mid(a, b):
        return point((a.x+b.x)/2, (a.y+b.y)/2, (a.z+b.z)/2)

    def move(self, value_x=0, value_y=0, value_z=0):
        return point(self.x+value_x, self.y+value_y, self.z+value_z)
    
    def slope(a, b):
        if a.x != b.x:
            return 1.0*(a.y-b.y)/(a.x-b.x)
        else:
            return float('inf')

    def sort_closest(lst, pt):
        _s = []
        while pt in lst:
            _s.append(lst.pop(lst.index(pt)))
        sorted_lst = sorted(lst, key=lambda _pt: point.dist(_pt, pt))
        return _s+sorted_lst

    def sort_acw(lst, pt):
        _s = []
        while pt in lst:
            _s.append(lst.pop(lst.index(pt)))
        sorted_lst = sorted(lst, key=lambda _pt: (point.slope(_pt, pt), point.dist(_pt, pt)))
        return _s+sorted_lst

class vector:
    def __init__(self, x=0, y=0, z=0):
        if isinstance(x, (list, tuple, vector)):
            if len(x) == 1:
                _cv = [x[0], 0, 0]
                x, y, z = _cv
            elif len(x) == 2:
                _cv = [x[0], x[1], 0]
                x, y, z = _cv
            elif len(x) == 3:
                _cv = [x[0], x[1], x[2]]
                x, y, z = _cv
        self.v = [x, y, z]
        self.x = x
        self.y = y
        self.z = z
    
    @classmethod
    def invert(cls, v):
        if not isinstance(v, list):
            raise TypeError
        cv = cls()
        cv.v = v
        return cv

    def __repr__(self):
        comp = ', '.join([repr(x) for x in self.v])
        return f'{type(self).__name__}({comp})'
    
    def __str__(self):
        comp = ', '.join([str(x) for x in self.v])
        return f'vector({comp})'
    
    def __add__(self, other):
        if not isinstance(other, vector):
            if other == 0:
                return self
            raise TypeError
        _add = [a+b for (a, b) in zip(self.v, other.v)]
        return vector.invert(_add)

    def __radd__(self, other):
        if not isinstance(other, vector):
            if other == 0:
                return self
            raise TypeError
        _radd = [a+b for (a, b) in zip(self.v, other.v)]
        return vector.invert(_radd)

    def __sub__(self, other):
        if not isinstance(other, vector):
            raise TypeError
        _sub = [a-b for (a, b) in zip(self.v, other.v)]
        return vector.invert(_sub)

    def __mul__(self, scalar):
        if not isinstance(scalar, (int or float)):
            raise TypeError
        _mul = [x*scalar for x in self.v]
        return vector.invert(_mul)

    def __rmul__(self, scalar):
        if not isinstance(scalar, (int or float)):
            raise TypeError
        _mul = [x*scalar for x in self.v]
        return vector.invert(_mul)

    def __truediv__(self, scalar):
        if not isinstance(scalar, (int or float)):
            raise TypeError
        _tdiv = [x/scalar for x in self.v]
        return vector.invert(_tdiv)

    def __floordiv__(self, scalar):
        if not isinstance(scalar, (int or float)):
            raise TypeError
        _fdiv = [x//scalar for x in self.v]
        return vector.invert(_fdiv)
    
    def __abs__(self):
        return sum([x**2 for x in self.v])**0.5

    def __pos__(self):
        return self

    def __neg__(self):
        return vector(-self.x, -self.y, -self.z)

    def __eq__(self, other):
        if not isinstance(other, vector):
            raise TypeError
        return list(self) == list(other)

    def __ne__(self, other):
        if not isinstance(other, vector):
            raise TypeError
        return list(self) != list(other)

    def __len__(self):
        return len(self.v)
    
    def __getitem__(self, i):
        if i > 2:
            raise IndexError
        return self.v[i]
    
    def angle(self, other):
        if not isinstance(other, vector):
            raise TypeError
        return degrees(acos(vector.dot(self, other)/(abs(self)*abs(other))))

    def area3(self, other):
        if not isinstance(other, vector):
            raise TypeError
        return abs((abs(self)*abs(other)*sin(vector.angle(self, other)))/2)

    def area4(self, other):
        if not isinstance(other, vector):
            raise TypeError
        return abs(abs(self)*abs(other)*sin(vector.angle(self, other)))

    def cross(v1, v2):
        if not isinstance(v2, vector):
            raise TypeError
        _cross = [v1[1]*v2[2]-v1[2]*v2[1], v1[2]*v2[0]-v1[0]*v2[1], v1[0]*v2[1]-v1[1]*v2[0]]
        return vector.invert(_cross)

    def dot(self, other):
        if not isinstance(other, vector):
            raise TypeError
        return sum(v_x*v_y for (v_x, v_y) in zip(self, other))

    def is_unit(self):
        if self.size() == 1:
            return True
        else:
            return False

    def one():
        return vector(1, 1, 1)

    def reverse(self):
        return vector(-self.x, -self.y, -self.z)

    def size(self):
        return sum([x**2 for x in self.v])**0.5

    def to_vector(pt1=point, pt2=point): # pt1: from / pt2: to
        _v = [v2-v1 for (v1, v2) in zip(pt1, pt2)]
        return vector.invert(_v)

    def zero():
        return vector(0, 0, 0)

class tools:
    # calculate area of convex polygon(only 2D)
    def area(pset):
        if len(pset) != len(tools.find_hull(pset)):
            return
        
        area = 0
        xset, yset, zset = zip(*pset)
        if any(zset):
            return
        
        xset, yset = list(xset), list(yset)
        xset.append(xset[0])
        yset.append(yset[0])

        for i in range(len(pset)):
            area += xset[i]*yset[i+1] - xset[i+1]*yset[i]

        return abs(area/2)
    
    # calculate distance from dot(p) to line(ab)
    def dot_to_line(p, a, b): 
        hyp = sqrt((a.x-b.x)**2 + (a.y-b.y)**2)
        area = abs(p.x*(b.y-a.y) - p.y*(b.x-a.x) + vector.cross(a, b))
        return area / hyp

    # find convex hull of points set
    def find_hull(pset):
        upper = []; lower = []

        for i in sorted(pset):
            while len(upper) > 1 and point.ccw(upper[-2], upper[-1], i) <= 0:
                upper.pop()
            upper.append(i)
            while len(lower) > 1 and point.ccw(lower[-2], lower[-1], i) >= 0:
                lower.pop()
            lower.append(i)

        return upper+lower[-2:0:-1]

    # determine if all points exist on a single line
    def in_one_line(pset):
        ...

def test():
    n = int(input())
    lst = []
    for i in range(n):
        a, b = map(int, input().split())
        lst.append(point(a, b))
