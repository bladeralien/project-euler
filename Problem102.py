class Point:
    def __init__(self, a, b):
        self.x = a
        self.y = b
    def coordinatex(self):
        return self.x
    def coordinatey(self):
        return self.y

class Vector:
    def __init__(self, a, b = Point(0, 0)):
        self.a = a.coordinatex() - b.coordinatex()
        self.b = a.coordinatey() - b.coordinatey()
    def coordinatea(self):
        return self.a
    def coordinateb(self):
        return self.b    
    def __add__(self, other):
        return Vector(Point(self.coordinatea() + other.coordinatea(), self.coordinateb() + other.coordinateb()))
    def __sub__(self, other):
        return Vector(Point(self.coordinatea() - other.coordinatea(), self.coordinateb() - other.coordinateb()))
    def dot(self, other):
        return self.coordinatea() * other.coordinatea() + self.coordinateb() * other.coordinateb()
    def corss(self, other):
        pass

def PointInTriangle(a, b, c, p = Point(0, 0)):
    ab = (Vector(a) - Vector(p)).dot(Vector(b) - Vector(p))
    ac = (Vector(a) - Vector(p)).dot(Vector(c) - Vector(p))
    bb = (Vector(b) - Vector(p)).dot(Vector(b) - Vector(p))
    bc = (Vector(b) - Vector(p)).dot(Vector(c) - Vector(p))
    cc = (Vector(c) - Vector(p)).dot(Vector(c) - Vector(p))
    if bc * ac - cc * ab >= 0 and ab * bc - ac * bb >= 0:
        return True
    else:
        return False

source = [[int(x) for x in line.strip().split(',')] for line in open('Problem102.txt').readlines()]
count = 0
for aline in source:
    if PointInTriangle(Point(aline[0], aline[1]), Point(aline[2], aline[3]), Point(aline[4], aline[5])):
        count += 1
print(count)
