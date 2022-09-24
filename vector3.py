import math


class Vector3:
    '''Recreation of Unity's Vector3.
    \nSource: https://docs.unity3d.com/ScriptReference/Vector3.html
    '''

    normalized: 'Vector3'
    x: float
    y: float
    z: float

    def __init__(self, x: float, y: float, z: float):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self) -> str:
        return f"Vector3(\nx: {self.x}\ny: {self.y}\nx: {self.x}\nmagnitude: {self.magnitude})"

    def __sub__(self, other: 'Vector3'):
        return Vector3(self.x - other.x, self.y - other.y, self.z - other.z)

    def __add__(self, other: 'Vector3'):
        return Vector3(self.x + other.x, self.y + other.y, self.z + other.z)

    def __mul__(self, other):
        if isinstance(other, Vector3):
            return Vector3.Dot(self, other)
        elif isinstance(other, int | float | bytes):
            return Vector3(self.x*other, self.y*other, self.z - other)
        else:
            raise ValueError("Only Vector3, int, float and bytes are accepted")

    def __truediv__(self, other):
        if isinstance(other, int | float | bytes):
            return Vector3(self.x/other, self.y/other, self.z/other)
        else:
            raise ValueError("Only int, float and bytes are accepted")

    def __eq__(self, other: 'Vector3') -> bool:
        return isinstance(other, Vector3) & self.x == other.x & self.y == other.y & self.z == other.z

    def __ne__(self, other: 'Vector3') -> bool:
        return isinstance(other, Vector3) & (self.x != other.x or self.y != other.y or self.z != other.z)

    @staticmethod
    def Dot(va: 'Vector3', vb: 'Vector3'):
        return va.x*vb.x + va.y*vb.y + va.z*vb.z

    @staticmethod
    def Distance(va: 'Vector3', vb: 'Vector3'):
        return math.sqrt((va.x-vb.x)**2 + (va.y-vb.y)**2 + (va.z-vb.z)**2)

    @property
    def magnitude(self):
        '''norm of the vector'''
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    @staticmethod
    def Angle(va: 'Vector3', vb: 'Vector3'):
        '''Returns the minimum angle between the 2 vectors in degrees'''
        return math.acos(Vector3.Dot(va, vb) / (va.magnitude * vb.magnitude))*180/math.pi

    @staticmethod
    def Lerp(va: 'Vector3', vb: 'Vector3', t: float) -> 'Vector3':
        '''Lerp between vector A and vector B
        \nt represents the percentage clamped between 0 and 1'''
        return va + (vb - va) * max(min(t, 1), 0)

    @staticmethod
    def MoveTowards(va: 'Vector3', vb: 'Vector3', maxDistanceDelta: float) -> 'Vector3':
        return va + (vb - va) * maxDistanceDelta

    @staticmethod
    def zero():
        return Vector3(0, 0, 0)

    @staticmethod
    def left():
        return Vector3(-1, 0, 0)

    @staticmethod
    def right():
        return Vector3(1, 0, 0)

    @staticmethod
    def down():
        return Vector3(0, -1, 0)

    @staticmethod
    def up():
        return Vector3(0, 1, 0)

    @staticmethod
    def forward():
        return Vector3(0, 0, 1)

    @staticmethod
    def back():
        return Vector3(0, 0, -1)

    @staticmethod
    def one():
        return Vector3(1, 1, 1)
