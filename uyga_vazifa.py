class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.x}, {self.y})'  # (10, 8)

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        return Vector(x, y)

    def __mul__(self, other):
        x = self.x * other.x
        y = self.y * other.y
        return Vector(x, y)

    def __len__(self):
        return self.x - self.y

    def __int__(self):
        return int(self.x + self.y)

    def __bool__(self):
        return bool(self.x or self.y)

    def __iter__(self):
        return iter([self.x, self.y])

    def __pow__(self, power):
        if isinstance(power, int):
            return Vector(self.x ** power, self.y ** power)
        elif isinstance(power, Vector):
            return Vector(self.x ** power.x, self.y ** power.y)
        else:
            raise ValueError("Power must be an integer or a Vector")

v1 = Vector(10, 8)
v2 = Vector(5, 3)

v3 = v1 + v2
v4 = v1 - v2
v5 = v1 * v2

print(v5)
print(len(v1))  # 2
print(list(v1))  # [10, 8]
print(tuple(v1))  # (10, 8)
print(v1 ** 2)  # (100, 64)
print(v1 ** v2)  # (100000, 512)