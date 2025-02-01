class Rectangle:
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def get_square(self):
        return self.width * self.height
    
    def find_first_side_from_square(self, square):
        for i in range(2, square):
            if square % i == 0:
                return i

    def find_second_side_from_square(self, square, first_side):
        return square / first_side

    def add_new_rectangle_with_square(self, square):
        first_side = self.find_first_side_from_square(square)
        second_side = self.find_second_side_from_square(square, first_side)
        
        return Rectangle(first_side, second_side)
        
    def __add__(self, other):
        self_square = self.get_square()
        if isinstance(other, Rectangle):
            other = other.get_square()
        add_squares = self_square + other
        
        return self.add_new_rectangle_with_square(add_squares)
    
    def __eq__(self, other):
        return self.get_square() == other.get_square()
    
    def __mul__(self, other):
        self_square = self.get_square()
        if isinstance(other, Rectangle):
            other = other.get_square()
        add_squares = self_square * other
        
        return self.add_new_rectangle_with_square(add_squares)

    def __str__(self):
        return f"Rectangle({self.width}, {self.height})"


r1 = Rectangle(2, 4)
r2 = Rectangle(3, 6)
assert r1.get_square() == 8, 'Test1'
assert r2.get_square() == 18, 'Test2'

r3 = r1 + r2
assert r3.get_square() == 26, 'Test3'

r4 = r1 * 4
assert r4.get_square() == 32, 'Test4'
print(r4.get_square())

assert Rectangle(3, 6) == Rectangle(2, 9), 'Test5'
