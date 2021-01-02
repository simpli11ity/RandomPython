from math import sqrt

class Rectangle():

    def set_perimeter(self):
        self.perimeter = 2 * (self.length + self.width)

    def set_surface(self):
        self.surface = self.length * self.width

    def set_width(self):
        self.width = self.get_width()

    def set_length(self):
        self.length = self.get_length()

    def get_width(self):
        wid = int(input("Width of rectangle: "))
        return wid

    def get_length(self):
        leng = int(input("Length of rectangle: "))
        return leng

    def update_rectangle(self):
        self.set_perimeter()
        self.set_surface()

    def __init__(self):
        self.set_width()
        self.set_length()
        self.set_perimeter()
        self.set_surface()
        #self.width = width
        #self.length = length
        #self.perimeter = 2 * (self.width + self.length)
        #self.surface = self.width * self.length

    def __str__(self):
        st = ' W: ' + str(self.width) + ' L: ' +  str(self.length)
        st = st + ' Perimeter: ' +  str(self.perimeter) + ' Surface: ' +  str(self.surface)
        return st


class Triangle():
    def __init__(self, line1= 0, line2=0, line3=0):
        self.AB = float(line1)
        self.BC = float(line2)
        self.AC = float(line3)
        self.perimeter = float(self.AB + self.BC + self.AC)
        self.p = float(self.perimeter/2)
        self.surface = 0 #sqrt( int(self.p * ( self.p - self.AB ) * ( self.p - self.BC) * (self.p - self.AC)))
        self.property = ''
        self.det_property()

    def __str__(self):
        st = 'AB: ' +  str(self.AB) + ' BC: ' + str(self.BC)
        st = st + ' AC: ' + str(self.AC)
        st = st + ' P: ' + str(self.perimeter) + ' S: {:.2f} '.format(self.surface)
        st += self.property
        return st

    def c_perimeter(self):
        self.perimeter = self.AB + self.BC + self.AC

    def c_surface(self):
        p = (self.AB + self.BC + self.AC)//2
        self.surface = sqrt( p * ( p - self.AB ) * ( p - self.BC) * (p - self.AC))



    def det_property(self):
        a = self.BC
        b = self.AC
        c = self.AB
        a = a*a
        b = b*b
        c = c*c
        self.property = 'Ordinary'
        if self.AB == self.AC or self.AC == self.BC or self.BC == self.AB :
            self.property = "Isoscel"
        if self.AB == self.AC and self.AC == self.BC:
            self.property = 'Equilateral'
        if (self.AB == self.AC or self.AC == self.BC or self.BC == self.AB) and \
            (a == b + c or b == a + c or c == a+b):
            self.property = " Rectangular Isoscel"
        if a == b + c or b == a + c or c == a+b:
            self.property = 'Rectangular'

def read_rectangle():
    sh = Rectangle()
    return sh


def read_triangle():

    l1, l2, l3 = input("Enter three lines: ").split()
    sh = Triangle(l1, l2, l3)
    return sh


def main():

    #tri=read_triangle()
    #print(tri)
    re = read_rectangle()
    print(re)
    return 0


if __name__ == '__main__':
    main()