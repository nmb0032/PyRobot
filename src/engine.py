from math import cos, sin
import numpy as np


def inverse_rotation_matrix(k):
    return np.array([[cos(k), -sin(k), 0],
                     [sin(k),  cos(k), 0],
                     [0     ,       0, 1]], dtype=float)


def main():
    print("Testing inverse rotation matrix")
    print(inverse_rotation_matrix(7))

if __name__ == '__main__':
    main()