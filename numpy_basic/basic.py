import numpy as np

# create an class for basic operation of numpy array

class NumpyBasic:
    def __init__(self, array):
        self.array = array

    def add(self, value):
        return self.array + value

    def subtract(self, value):
        return self.array - value

    def multiply(self, value):
        return self.array * value

    def divide(self, value):
        return self.array / value

    def power(self, value):
        return self.array ** value

    def square_root(self):
        return np.sqrt(self.array)

    def log(self):
        return np.log(self.array)

    def exp(self):
        return np.exp(self.array)

    def sin(self):
        return np.sin(self.array)

    def cos(self):
        return np.cos(self.array)

    def tan(self):
        return np.tan(self.array)

    def arcsin(self):
        return np.arcsin(self.array)

    def arccos(self):
        return np.arccos(self.array)

    def arctan(self):
        return np.arctan(self.array)

    def sinh(self):
        return np.sinh(self.array)

    def cosh(self):
        return np.cosh(self.array)

    def tanh(self):
        return np.tanh(self.array)

    def arcsinh(self):
        return np.arcsinh(self.array)

    def arccosh(self):
        return np.arccosh(self.array)

    def arctanh(self):
        return np.arctanh(self.array)

    def dot(self, value):
        return np.dot(self.array, value)

    def cross(self, value):
        return np.cross(self.array, value)

    def inner(self, value):
        return np.inner(self.array, value)

    def outer(self, value):
        return np.outer(self.array, value)

    def matmul(self, value):
        return np.matmul(self.array, value)

    def vdot(self, value):
        return np.vdot(self.array, value)

    def linalg_norm(self):
        return np.linalg.norm(self.array)

    def linalg_inv(self):
        return np.linalg.inv(self.array)

    def linalg_det(self):
        return np.linalg.det(self.array)

    def linalg_svd(self):
        return np.linalg.svd(self.array)

    def linalg_eig(self):
        return np.linalg.eig(self.array)

    def linalg_eigh(self):
        return np.linalg.eigh(self.array)

    def linalg_eigvals(self):
        return np.linalg.eigvals(self.array)
    

# create an object of NumpyBasic class
if __name__ == "__main__":
    array = np.array([1, 2, 3, 4, 5])
    obj = NumpyBasic(array)
    print(obj.add(2))
    print(obj.subtract(2))
    print(obj.multiply(2))
    print(obj.divide(2))
    print(obj.power(2))
    print(obj.square_root())
    print(obj.log())
    print(obj.exp())
    print(obj.sin())
    print(obj.cos())
    print(obj.tan())
    print(obj.arcsin())
    print(obj.arccos())
    print(obj.arctan())
    print(obj.sinh())
    print(obj.cosh())
    print(obj.tanh())
    print(obj.arcsinh())
    print(obj.arccosh())
    print(obj.arctanh())
    print(obj.dot(array))
    print(obj.cross(array))
    print(obj.inner(array))
    print(obj.outer(array))
    print(obj.matmul(array))
    print(obj.vdot(array))
    print(obj.linalg_norm())
    print(obj.linalg_inv())
    print(obj.linalg_det())
    print(obj.linalg_svd())
    print(obj.linalg_eig())
    print(obj.linalg_eigh())
    print(obj.linalg_eigvals())