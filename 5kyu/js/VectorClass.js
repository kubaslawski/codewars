/*
Create a Vector object that supports addition, subtraction, dot products, and norms. So, for example:

a = Vector([1, 2, 3])
b = Vector([3, 4, 5])
c = Vector([5, 6, 7, 8])

a.add(b)      # should return a new Vector([4, 6, 8])
a.subtract(b) # should return a new Vector([-2, -2, -2])
a.dot(b)      # should return 1*3 + 2*4 + 3*5 = 26
a.norm()      # should return sqrt(1^2 + 2^2 + 3^2) = sqrt(14)
a.add(c)      # raises an exception
If you try to add, subtract, or dot two vectors with different lengths, you must throw an error!

Also provide:

a toString method, so that using the vectors from above, a.toString() === '(1,2,3)' (in Python, this is a __str__ method, so that str(a) == '(1,2,3)')
an equals method, to check that two vectors that have the same components are equal
Note: the test cases will utilize the user-provided equals method.
**/


class Vector {
    constructor(arr) {
        this.arr = arr;
    }
    add(obj) {
        if (obj.arr.length !== this.arr.length) {
            throw new Error('Vectors must have the same length');
        };
        return new Vector(obj.arr.map((x, i) => x + obj.arr[i]));
    }
    subtract(obj) {
        if (obj.arr.length !== this.arr.length) {
            throw new Error('Vectors must have the same length');
        };
        return new Vector(this.arr.map((x, i) => x - obj.arr[i]));
    }
    dot(obj) {
        if (obj.arr.length !== this.arr.length) {
            throw new Error('Vectors must have the same length');
        };
        return this.arr.reduce((sum, x, i) => sum + x * obj.arr[i], 0);
    }
    norm() {
        return Math.sqrt(this.arr.reduce((sum, x) => sum + x ** 2, 0));
    }
    toString() {
        return `(${this.arr.join(",")})`;
    }
    equals(obj) {
        return this.arr == obj.arr;
    }
}

const a = new Vector([1, 2, 3]);
const b = new Vector([3, 4, 5]);
const c = new Vector([5, 6, 7, 8]);

console.log(a.add(b))

