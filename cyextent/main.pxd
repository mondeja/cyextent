

cdef class Extent:
    cdef readonly double xmin, xmax, ymin, ymax 
    cdef readonly bint swapped_x, swapped_y

    cpdef touches(self, Extent other)
    cpdef intersect(self, Extent other)
    cpdef distance(self, Extent other)
    cpdef area(self)

cpdef Extent union(Extent e1, Extent e2)
