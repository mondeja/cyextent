# -*- coding: utf-8 -*-

# Source: https://github.com/gisalgs/indexing/blob/master/extent.py

from timeit import timeit
import random
from math import sqrt

def instanciation():
    print("_____________________________________________\n")
    print("     -----  Test 1: Instanciation  -----     \n")

    py_t = timeit(
        "PyExtent(" \
          + "random.uniform(5.0, 15.0)," \
          + "random.uniform(20.0, 60.0)," \
          + "random.uniform(5.0, 15.0)," \
          + "random.uniform(20.0, 60.0))",
        setup="import random; from cyextent import PyExtent",
        number=20000,
    )

    cy_t = timeit(
        "CyExtent(" \
          + "random.uniform(5.0, 15.0)," \
          + "random.uniform(20.0, 60.0)," \
          + "random.uniform(5.0, 15.0)," \
          + "random.uniform(20.0, 60.0))",
        setup="import random;from cyextent import Extent as CyExtent",
        number=20000,
    )

    print("Python:", py_t)
    print("Cython:", cy_t, end="\n")

    print("_____________________________________________\n\n\n")

def getitem():
    print("_____________________________________________\n")
    print("     -----  Test 2: __getitem__  -----     \n")

    py_t = timeit(
        "PyExtent(" \
          + "random.uniform(5.0, 15.0)," \
          + "random.uniform(20.0, 60.0)," \
          + "random.uniform(5.0, 15.0)," \
          + "random.uniform(20.0, 60.0))[random.randint(0,3)]",
        setup="import random; from cyextent import PyExtent",
        number=20000,
    )

    cy_t = timeit(
        "CyExtent(" \
          + "random.uniform(5.0, 15.0)," \
          + "random.uniform(20.0, 60.0)," \
          + "random.uniform(5.0, 15.0)," \
          + "random.uniform(20.0, 60.0))[random.randint(0,3)]",
        setup="import random;from cyextent import Extent as CyExtent",
        number=20000,
    )

    print("Python:", py_t)
    print("Cython:", cy_t, end="\n")

    print("_____________________________________________\n\n\n")

def eq():
    print("_____________________________________________\n")
    print("     -----  Test 3: __eq__  -----     \n")


    py_t = timeit(
       "PyExtent(" \
          + "random.uniform(5.0, 15.0)," \
          + "random.uniform(20.0, 60.0)," \
          + "random.uniform(5.0, 15.0)," \
          + "random.uniform(20.0, 60.0)" \
          + ") == " \
        + "PyExtent(" \
          + "random.uniform(5.0, 15.0)," \
          + "random.uniform(20.0, 60.0)," \
          + "random.uniform(5.0, 15.0)," \
          + "random.uniform(20.0, 60.0)" \
          + ")",
        setup="import random; from cyextent import PyExtent",
        number=20000,
    )

    cy_t = timeit(
        "CyExtent(" \
          + "random.uniform(5.0, 15.0)," \
          + "random.uniform(20.0, 60.0)," \
          + "random.uniform(5.0, 15.0)," \
          + "random.uniform(20.0, 60.0)" \
          + ") == " \
        + "CyExtent(" \
          + "random.uniform(5.0, 15.0)," \
          + "random.uniform(20.0, 60.0)," \
          + "random.uniform(5.0, 15.0)," \
          + "random.uniform(20.0, 60.0)" \
          + ")",
        setup="import random;from cyextent import Extent as CyExtent",
        number=20000,
    )

    print("Python:", py_t)
    print("Cython:", cy_t, end="\n")

    print("_____________________________________________\n\n\n")

def touches():
    print("_____________________________________________\n")
    print("     -----  Test 4: touches  -----     \n")


    py_t = timeit(
       "PyExtent(" \
          + "random.uniform(5.0, 15.0)," \
          + "random.uniform(20.0, 60.0)," \
          + "random.uniform(5.0, 15.0)," \
          + "random.uniform(20.0, 60.0)" \
          + ").touches(" \
        + "PyExtent(" \
          + "random.uniform(5.0, 15.0)," \
          + "random.uniform(20.0, 60.0)," \
          + "random.uniform(5.0, 15.0)," \
          + "random.uniform(20.0, 60.0)" \
          + ")" \
        + ")",
        setup="import random; from cyextent import PyExtent",
        number=20000,
    )

    cy_t = timeit(
        "CyExtent(" \
          + "random.uniform(5.0, 15.0)," \
          + "random.uniform(20.0, 60.0)," \
          + "random.uniform(5.0, 15.0)," \
          + "random.uniform(20.0, 60.0)" \
          + ").touches(" \
        + "CyExtent(" \
          + "random.uniform(5.0, 15.0)," \
          + "random.uniform(20.0, 60.0)," \
          + "random.uniform(5.0, 15.0)," \
          + "random.uniform(20.0, 60.0)" \
          + ")" \
        + ")",
        setup="import random;from cyextent import Extent as CyExtent",
        number=20000,
    )

    print("Python:", py_t)
    print("Cython:", cy_t, end="\n")

    print("_____________________________________________\n\n\n")


def intersect():
    print("_____________________________________________\n")
    print("     -----  Test 5: intersect  -----     \n")

    print("Intersection:")
    py_t = timeit(
       "PyExtent(" \
          + "random.uniform(5.0, 15.0)," \
          + "random.uniform(20.0, 60.0)," \
          + "random.uniform(5.0, 15.0)," \
          + "random.uniform(20.0, 60.0)" \
          + ").intersect(" \
        + "PyExtent(" \
          + "random.uniform(600.0, 1400.0)," \
          + "random.uniform(2000.0, 6000.0)," \
          + "random.uniform(500.0, 1500.0)," \
          + "random.uniform(2000.0, 6000.0)" \
          + ")" \
        + ")",
        setup="import random; from cyextent import PyExtent",
        number=20000,
    )

    cy_t = timeit(
        "CyExtent(" \
          + "random.uniform(5.0, 15.0)," \
          + "random.uniform(20.0, 60.0)," \
          + "random.uniform(5.0, 15.0)," \
          + "random.uniform(20.0, 60.0)" \
          + ").intersect(" \
        + "CyExtent(" \
          + "random.uniform(500.0, 1500.0)," \
          + "random.uniform(2000.0, 6000.0)," \
          + "random.uniform(500.0, 1500.0)," \
          + "random.uniform(2000.0, 6000.0)" \
          + ")" \
        + ")",
        setup="import random;from cyextent import Extent as CyExtent",
        number=20000,
    )

    print("Python:", py_t)
    print("Cython:", cy_t, end="\n\n")


    print("No intersection:")
    py_t = timeit(
       "PyExtent(" \
          + "5," \
          + "20," \
          + "15," \
          + "60" \
          + ").intersect(" \
        + "PyExtent(" \
          + "random.uniform(6.0, 14.0)," \
          + "random.uniform(15.0, 19.0)," \
          + "random.uniform(16.0, 19.0)," \
          + "random.uniform(55.0, 59.0)" \
          + ")" \
        + ")",
        setup="import random; from cyextent import PyExtent",
        number=20000,
    )

    cy_t = timeit(
        "CyExtent(" \
           + "5," \
          + "20," \
          + "15," \
          + "60" \
          + ").intersect(" \
        + "CyExtent(" \
          + "random.uniform(6.0, 14.0)," \
          + "random.uniform(15.0, 19.0)," \
          + "random.uniform(16.0, 19.0)," \
          + "random.uniform(55.0, 59.0)" \
          + ")" \
        + ")",
        setup="import random;from cyextent import Extent as CyExtent",
        number=20000,
    )

    print("Python:", py_t)
    print("Cython:", cy_t, end="\n")

    print("_____________________________________________\n\n\n")

def distance():
    print("_____________________________________________\n")
    print("     -----  Test 6: distance  -----     \n")


    py_t = timeit(
       "PyExtent(" \
          + "random.uniform(5.0, 15.0)," \
          + "random.uniform(20.0, 60.0)," \
          + "random.uniform(5.0, 15.0)," \
          + "random.uniform(20.0, 60.0)" \
          + ").distance(" \
        + "PyExtent(" \
          + "random.uniform(5.0, 15.0)," \
          + "random.uniform(20.0, 60.0)," \
          + "random.uniform(5.0, 15.0)," \
          + "random.uniform(20.0, 60.0)" \
          + ")" \
        + ")",
        setup="import random; from cyextent import PyExtent",
        number=20000,
    )

    cy_t = timeit(
        "CyExtent(" \
          + "random.uniform(5.0, 15.0)," \
          + "random.uniform(20.0, 60.0)," \
          + "random.uniform(5.0, 15.0)," \
          + "random.uniform(20.0, 60.0)" \
          + ").distance(" \
        + "CyExtent(" \
          + "random.uniform(5.0, 15.0)," \
          + "random.uniform(20.0, 60.0)," \
          + "random.uniform(5.0, 15.0)," \
          + "random.uniform(20.0, 60.0)" \
          + ")" \
        + ")",
        setup="import random;from cyextent import Extent as CyExtent",
        number=20000,
    )

    print("Python:", py_t)
    print("Cython:", cy_t, end="\n")

    print("_____________________________________________\n\n\n")

def area():
    print("_____________________________________________\n")
    print("     -----  Test 7: area  -----     \n")

    py_t = timeit(
        "PyExtent(" \
          + "random.uniform(5.0, 15.0)," \
          + "random.uniform(20.0, 60.0)," \
          + "random.uniform(5.0, 15.0)," \
          + "random.uniform(20.0, 60.0)).area()",
        setup="import random; from cyextent import PyExtent",
        number=20000,
    )

    cy_t = timeit(
        "CyExtent(" \
          + "random.uniform(5.0, 15.0)," \
          + "random.uniform(20.0, 60.0)," \
          + "random.uniform(5.0, 15.0)," \
          + "random.uniform(20.0, 60.0)).area()",
        setup="import random;from cyextent import Extent as CyExtent",
        number=20000,
    )

    print("Python:", py_t)
    print("Cython:", cy_t, end="\n")

    print("_____________________________________________\n\n\n")

def main():
    instanciation()
    getitem()
    eq()
    touches()
    intersect()
    distance()
    area()


if __name__ == "__main__":
    main()
