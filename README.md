# Vector

Recreation of Unity's Vectors structs in python.
Can be used for maths, physic, simulations, games...

it's composed of 2 main classes:

- Vector2 (2D)
- Vector3 (3D)

_Might not be 100% accurate, this is still in devloppment._  
_Feel free to open issue request if you find bugs._

## Vector 2

Representation of 2D vectors and points.
<https://docs.unity3d.com/ScriptReference/Vector2.html>

### Constructor

> ### Vector2(x, y)
>
> x -> _float_  
> y -> _float_

### Properties

> ### magnitude
>
> Returns the length/intensity/norm of this vector (Read Only)  
> -> _float_

> ### x
>
> X Component of the vector  
> -> _float | int | bytes_

> ### y
>
> Y Component of the vector  
> -> _float | int | bytes_

### Static Properties

> ### down
>
> Vector2(0, -1)

> ### left
>
> Vector2(-1, 0)

> ### one
>
> Vector2(1, 1)

> ### right
>
> Vector2(1, 0)

> ### up
>
> Vector2(0, 1)

> ### zero
>
> Vector2(0, 0)

### Static Methods

> ### Angle(va, vb)
>
> Calculates the lowest angle between **va** and **vb** in degrees  
> va -> _Vector2_  
> vb -> _Vector2_  
> --> _float_

> ### Distance(va, vb)
>
> Calculates the distance between **va** and **vb**  
> va -> _Vector2_  
> vb -> _Vector2_  
> --> _float_

> ### Lerp(va, vb, t)
>
> Lerp between vector A and vector B  
> va -> _Vector2_  
> vb -> _Vector2_  
> t -> _float_ clamped between 0 and 1  
> --> _Vector2_

## Vector3

Representation of 3D vectors and points.
<https://docs.unity3d.com/ScriptReference/Vector3.html>

### Constructor

> ### Vector3(x, y, z)
>
> x -> _float_  
> y -> _float_  
> z -> _float_

### Properties

> ### magnitude
>
> Returns the length (norm) of this vector (Read Only)  
> --> _float_

> ### x
>
> X Component of the vector  
> -> _float | int | bytes_

> ### y
>
> Y Component of the vector  
> -> _float | int | bytes_

> ### z
>
> Z Component of the vector  
> -> _float | int | bytes_

### Static Properties

> ### back
>
> Vector3(0, 0, -1)

> ### down
>
> Vector3(0, -1, 0)

> ### forward
>
> Vector3(0, 0, 1)

> ### left
>
> Vector3(-1, 0, 0)

> ### one
>
> Vector3(1, 1, 1)

> ### right
>
> Vector3(1, 0, 0)

> ### up
>
> Vector3(0, 1, 0)

> ### zero
>
> Vector3(0, 0, 0)

### Static Methods

> ### Angle(va, vb)
>
> Calculates the lowest angle between **va** and **vb** in degrees  
> va -> _Vector3_  
> vb -> _Vector3_  
> --> _float_

> ### Distance(va, vb)
>
> Calculates the distance between **va** and **vb**  
> va -> _Vector3_  
> vb -> _Vector3_  
> --> _float_

> ### Lerp(va, vb, t)
>
> Lerp between vector A and vector B  
> va -> _Vector3_  
> vb -> _Vector3_  
> t -> _float_ clamped between 0 and 1  
> --> _Vector3_

> ### Dot(va, vb)
>
> return the dot product of **va.vb**  
> --> _float_
