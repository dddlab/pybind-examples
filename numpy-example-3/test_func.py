import cppimport
import numpy as np

code = cppimport.imp("code")

if __name__ == '__main__':
    xs = np.arange(12)
    print(xs)

    print(code.add_arrays(xs, xs))
