
# Source: https://github.com/gisalgs/indexing/blob/master/extent.py

from libc.math cimport (
    fmax,
    fmin,
    sqrt
)

cdef class Extent(object):
    __slots__ = [
        "xmin",
        "xmax",
        "ymin",
        "ymax",
        "swapped_x",
        "swapped_y",
    ]

    def __cinit__(self,
                  double xmin,
                  double xmax,
                  double ymin,
                  double ymax):
        self.swapped_x = (xmax < xmin)
        self.swapped_y = (ymax < ymin)
        self.xmin = xmin
        self.xmax = xmax
        self.ymin = ymin
        self.ymax = ymax

        if self.swapped_x:
            self.xmin, self.xmax = xmax, xmin
        if self.swapped_y:
            self.ymin, self.ymax = ymax, ymin

    def __getitem__(self, const int i):
        if i==0:
            return self.xmin
        if i==1:
            return self.xmax
        if i==2:
            return self.ymin
        if i==3:
            return self.ymax
        return None

    def __eq__(self, Extent other):
        return self.xmin == other.xmin and \
            self.xmax == other.xmax and \
            self.ymin == other.ymin and \
            self.ymax == other.ymax

    cpdef touches(self, Extent other):
        return not (
            self.xmin>other.xmax or \
            self.xmax<other.xmin or \
            self.ymin>other.ymax or \
            self.ymax<other.ymin
        )

    cpdef intersect(self, Extent other):
        cdef double _xmin, _xmax, _ymin, _ymax
        if not self.touches(other):
            return 0
        _xmin = fmax(self.xmin, other.xmin)
        _xmax = fmin(self.xmax, other.xmax)
        _ymin = fmax(self.ymin, other.ymin)
        _ymax = fmin(self.ymax, other.ymax)
        return (_xmax-_xmin) * (_ymax-_ymin)

    cpdef distance(self, Extent other):
        cdef double x1, y1, x2, y2
        x1 = self.xmin+(self.xmax-self.xmin)/2.0
        y1 = self.ymin+(self.ymax-self.ymin)/2.0
        x2 = other.xmin+(other.xmax-other.xmin)/2.0
        y2 = other.ymin+(other.ymax-other.ymin)/2.0
        return sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2))

    cpdef area(self):
        return (self.xmax-self.xmin)*(self.ymax-self.ymin)

cpdef Extent union(Extent e1, Extent e2):
    cdef double _xmin, _xmax, _ymin, _ymax
    _xmin = fmin(e1.xmin, e2.xmin)
    _xmax = fmax(e1.xmax, e2.xmax)
    _ymin = fmin(e1.ymin, e2.ymin)
    _ymax = fmax(e1.ymax, e2.ymax)
    return Extent(_xmin, _xmax, _ymin, _ymax)
