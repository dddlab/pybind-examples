import cppimport
import numpy as np

code = cppimport.imp("code")

if __name__ == '__main__':
    n = int(1e9)

    print(code.calc_pi(n))
