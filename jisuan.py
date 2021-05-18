import numpy
a = numpy.array([[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9]])
print(a)
print(a.ndim)
b = numpy.arange(9,18).reshape(3,3)
print(b)
print(b.size)
print(b.shape)
c = a*b
print(c)
d = numpy.dot(a,b)
print(d)
e = numpy.sqrt(d)
print(e)
print(numpy.add(d,e))
f = numpy.arange(9)
f.shape = (3,3)
print(f)