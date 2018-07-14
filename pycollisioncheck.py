""" 


author Atsushi Sakai
"""

import matplotlib.pyplot as plt
import random
import numpy.linalg
import numpy


class position2d():
    def __init__(self, x, y):
        self.x = x
        self.y = y


def orient2d(A, B, C):
    a = numpy.array([[A.x - C.x, A.y - C.y],
                     [B.x - C.x, B.y - C.y]])

    if numpy.linalg.det(a) >= 0:
        return True  # upper
    else:
        return False  # lower


def test_orient2d():

    A = position2d(3.0, 5.0)
    B = position2d(6.0, 1.0)

    for i in range(30):
        x = random.uniform(-10, 10)
        y = random.uniform(-10, 10)
        C = position2d(x, y)

        if orient2d(A, B, C):
            plt.plot(x, y, "xb")

    plt.plot([A.x, B.x], [A.y, B.y], "-r")
    plt.axis("equal")
    plt.show()


def main():
    print("start!!")

    test_orient2d()

    print("done!!")


if __name__ == '__main__':
    main()
