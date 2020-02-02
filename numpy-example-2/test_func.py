import cppimport
import numpy as np

code = cppimport.imp("code")

if __name__ == '__main__':
    xs = np.arange(12).reshape(3,4).astype('float')
    print(xs)
    print("np :", xs.sum())
    print("cpp:", code.sum(xs))

    print()
    code.twice(xs)
    print(xs)    
