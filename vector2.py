import math


class Vector2:
    '''Recreation of Unity's Vector2.
    \nSource: https://docs.unity3d.com/ScriptReference/Vector2.html
    '''

    normalized: 'Vector2'
    x: float
    y: float

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f"Vector2(x: {self.x}\ny: {self.y}\nmagnitude: {self.magnitude})"

    def __sub__(self, other: 'Vector2'):
        return Vector2(self.x - other.x, self.y - other.y)

    def __add__(self, other: 'Vector2'):
        return Vector2(self.x + other.x, self.y + other.y)

    def __mul__(self, other):
        if isinstance(other, Vector2):
            return Vector2.Dot(self, other)
        elif isinstance(other, int | float | bytes):
            return Vector2(self.x*other, self.y*other)
        else:
            raise ValueError("Only Vector2, int, float and bytes are accepted")

    def __truediv__(self, other):
        if isinstance(other, int | float | bytes):
            return Vector2(self.x/other, self.y/other)
        else:
            raise ValueError("Only int, float and bytes are accepted")

    def __eq__(self, other: 'Vector2') -> bool:
        return isinstance(other, Vector2) & self.x == other.x & self.y == other.y

    def __ne__(self, other: 'Vector2') -> bool:
        return isinstance(other, Vector2) & (self.x != other.x or self.y != other.y)

    @staticmethod
    def Dot(va: 'Vector2', vb: 'Vector2'):
        return va.x*vb.x + va.y*vb.y

    @staticmethod
    def Distance(va: 'Vector2', vb: 'Vector2'):
        return math.sqrt((va.x-vb.x)**2 + (va.y-vb.y)**2)

    @property
    def magnitude(self):
        '''norm of the vector'''
        return math.sqrt(self.x**2+self.y**2)

    @staticmethod
    def Angle(va: 'Vector2', vb: 'Vector2'):
        '''Returns the minimum angle between the 2 vectors in degrees'''
        return math.acos(Vector2.Dot(va, vb) / (va.magnitude * vb.magnitude))*180/math.pi

    @staticmethod
    def Lerp(va: 'Vector2', vb: 'Vector2', t: float) -> 'Vector2':
        '''Lerp between vector A and vector B
        \nt represents the percentage clamped between 0 and 1'''
        return va + (vb - va) * max(min(t, 1), 0)

    @staticmethod
    def MoveTowards(va: 'Vector2', vb: 'Vector2', maxDistanceDelta: float) -> 'Vector2':
        '''Lerp between vector A and vector B
        \nt represents the percentage clamped between 0 and 1'''
        return va + (vb - va) * maxDistanceDelta

    @staticmethod
    def zero():
        return Vector2(0, 0)

    @staticmethod
    def left():
        return Vector2(-1, 0)

    @staticmethod
    def right():
        return Vector2(1, 0)

    @staticmethod
    def down():
        return Vector2(0, -1)

    @staticmethod
    def up():
        return Vector2(0, 1)

    @staticmethod
    def one():
        return Vector2(1, 1)
