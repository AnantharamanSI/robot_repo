#!/usr/bin/env python3
# add import and helper functions here
import numpy as np

if __name__ == "__main__":
    # code goes here
    # print("hello world")

    np.random.seed(42)
    A = np.random.normal(size=(4, 4))
    B = np.random.normal(size=(4, 2))
    C = A @ B
    # print(C)

    np.random.seed(42)
    x = np.random.normal(size=(4, 10))
    inter = x - x[:, None]
    # print(x)
    # print(inter.shape)
    print(np.sum(np.square(inter), axis=-1))

