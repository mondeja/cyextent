from .main import Extent

from math import sqrt

class PyExtent():
    def __init__(self, xmin=0, xmax=0, ymin=0, ymax=0):
        self.xmin = xmin
        self.xmax = xmax
        self.ymin = ymin
        self.ymax = ymax

    def __getitem__(self, i):
        if i==0:
            return self.xmin
        if i==1:
            return self.xmax
        if i==2:
            return self.ymin
        if i==3:
            return self.ymax
        return None

    def __eq__(self, other):
        return self.xmin == other.xmin and \
            self.xmax == other.xmax and \
            self.ymin == other.ymin and \
            self.ymax == other.ymax

    def touches(self, other):
        return not (
            self.xmin > other.xmax or \
            self.xmax < other.xmin or \
            self.ymin > other.ymax or \
            self.ymax < other.ymin)

    def contains(self, point):
        return not (
            self.xmin > point.x or \
            self.xmax < point.x or \
            self.ymin > point.y or \
            self.ymax < point.y)

    def area(self):
        return (self.xmax-self.xmin)*(self.ymax-self.ymin)

    def intersect(self, other):
        if not self.touches(other):
            return 0
        xmin = max(self.xmin, other.xmin)
        xmax = min(self.xmax, other.xmax)
        ymin = max(self.ymin, other.ymin)
        ymax = min(self.ymax, other.ymax)
        return (xmax-xmin)*(ymax-ymin)

    def distance(self, other):
        x1 = self.xmin+(self.xmax-self.xmin)/2.0
        y1 = self.ymin+(self.ymax-self.ymin)/2.0
        x2 = other.xmin+(other.xmax-other.xmin)/2.0
        y2 = other.ymin+(other.ymax-other.ymin)/2.0
        return sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2))
