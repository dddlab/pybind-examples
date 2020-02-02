import cppimport
import numpy as np

code = cppimport.imp("code")

if __name__ == '__main__':
    A = np.array([[1,2,1],
                  [2,1,0],
                  [-1,1,2]])

    print(A)
    print(code.det(A))
    print(code.inv(A))
