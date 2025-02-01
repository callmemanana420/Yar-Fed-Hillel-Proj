class Fraction():
    def __init__(self, up, down):
        self.up = up
        self.down = down

    def __str__(self):
        return f'Fraction: {self.up}, {self.down}'
    
    def __bigest_num_gen(self, num):
        num_to_yield = 0

        while True:
            yield num_to_yield
            num_to_yield += num

    def __find_lcm(self, first_num, second_num):
        if first_num > second_num:
            bigest_num_gen = self.__bigest_num_gen(first_num)
            fewer_num = second_num
        else:
            bigest_num_gen = self.__bigest_num_gen(second_num)
            fewer_num = first_num
        
        current_num = next(bigest_num_gen)
        while True:
            current_num = next(bigest_num_gen)
            if current_num % fewer_num == 0:
                return current_num

    def __float__(self):
        return self.up / self.down

    def __mul__(self, other):
        new_up = self.up * other.up
        new_down = self.down * other.down
        return Fraction(new_up, new_down)
    
    def __sub__(self, other):
        lcm = int(self.__find_lcm(self.down, other.down))

        self_multiplier = lcm / self.down
        other_multiplier = lcm / other.down

        self_new = self_multiplier * self.up
        other_new = other_multiplier * other.up

        return_up = int(self_new - other_new)

        return Fraction(return_up, lcm)
        
    def __add__(self, other):
        lcm = int(self.__find_lcm(self.down, other.down))

        self_multiplier = lcm / self.down
        other_multiplier = lcm / other.down

        self_new = self_multiplier * self.up
        other_new = other_multiplier * other.up

        return_up = int(self_new + other_new)

        return Fraction(return_up, lcm)
    
    def __eq__(self, other):
        return self.__float__() == other.__float__()
    
    def __ne__(self, other):
        return not self.__eq__(other)
    
    def __gt__(self, other):
        return self.__float__() > other.__float__()

    def __lt__(self, other):
        return self.__float__() < other.__float__()

# def __gt__(self, other):
#     return self.__float__() > other.__float__()

f_a = Fraction(2, 3)
f_b = Fraction(3, 6)

f_c = f_b + f_a
# assert str(f_c) == 'Fraction: 21, 18'
assert str(f_c) == 'Fraction: 7, 6'#та же самая дробь, но сокращенная
f_d = f_b * f_a
assert str(f_d) == 'Fraction: 6, 18'
f_e = f_a - f_b
# assert str(f_e) == 'Fraction: 3, 18'
assert str(f_e) == 'Fraction: 1, 6' #та же самая дробь, но сокращенная

assert f_d < f_c  # True
assert f_d > f_e  # True
assert f_a != f_b  # True
f_1 = Fraction(2, 4)
f_2 = Fraction(3, 6)
assert f_1 == f_2  # True

print('OK')
