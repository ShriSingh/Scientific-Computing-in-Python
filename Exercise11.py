# Learn Special Methods by Building a Vector Space

'''
A vector is an object that has a length(or magnitude), a direction,
and it cannot be expressed by a single number
    -> Is represented as a tuple of numbers
    -> Can have multiple dimensions(implemented through inheritance)
In physics, vectors are commonly used to represent forces, 
velocities, accelerations, and other quantities

Methods like __init__, __str__ etc. (also called special/magic methods) 
affect the behavior of that class
    -> __dict__ : Dictionary that stores the object's attributes
        -> vars() : Built-in function, returns the __dict__ attribute 
        of an object
    -> __str__ : Returns the string representation of the object
    -> __init__ : Initializes the object
    -> __repr__ : Returns the string needed to instantiate the object 
    -> __getattribute__ : Called when an instance attribute is accessed
        -> Raises 'AttributeError' when requested attributed is not 
        found/doesn't exist and calls __getattr__
    -> __add__ : Implemented to override what happens by default when two
    are added together using the '+' operator

Inheritance enables you to define a class from existing one.
    -> The new class(child) inherits all the methods & properties of the 
    existing class(parent)
'''

class R2Vector:
    """
    A class to represent a vector in a 2D space.
    """
    def __init__(self, *, x, y) -> None:
        """
        Initialize the vector with the given x and y coordinates.

        Args:
            :x: x-axis coordinate of the vector
            :y: y-axis coordinate of the vector

        Returns: 
            None
        """
        self.x = x
        self.y = y

    def norm(self):
        """
        Calculates the length or the magnitude of the vector.

        Args:
            :self: The object itself

        Returns:
            The length of the vector
        """
        sum_length = 0

        for val in self.__dict__.values():
            sum_length += val ** 2

        magnitude = sum_length ** 0.5

        # Alternative: return sum(val ** 2 for val in vars(self).values()) ** 0.5
        return magnitude

    def __str__(self):
        """
        Returns the string representation of the vector.

        Args:
            :self: The object itself

        Returns:
            The string representation of the vector
        """
        # vector = f"({self.x}, {self.y})"
        vector = str(tuple(getattr(self, i) for i in vars(self)))
        return vector

    def __repr__(self):
        """
        Returns the string needed to instantiate the object.

        Args:
            :self: The object itself

        Returns:
            The string needed to instantiate the object
        """
        # Creating a list of key-value pairs
        arg_list = [f"{key}={val}" for key, val in vars(self).items()]
        # Joining the elements together
        args = ", ".join(arg_list)

        # Returning the class name and the return
        return f"{self.__class__.__name__}({args})"

    """
    def __getattr__(self, attr):
        '''
        Called when instance attribute is accessed.
        Searches for it at the class level(both parent and class).
        Returns the value of the named attribute of an object. 
        If not found, it returns the default value provided to the function.
        
        Args:
            :attr: The attribute to be accessed
        Returns:
            Value of the named attribute
        '''
        return 'calling __getattr__'
    """

    def __add__(self, other):
        """
        Adds two vectors together.

        Args:
            :self: The object itself
            :other: The other vector to be added

        Returns:
            A new vector that is the sum of the two vectors
        """
        # Making sure that the two vectors are of the same type
        if type(self) != type(other):
            # Asks other operand to perform the operation
            return NotImplemented # Doesn't raise an exception immediately

        # Store the sum of the two vectors in a key-value pair
        kwargs = {i : (getattr(self, i) + getattr(other, i)) for i in vars(self)}

        # Returning an instance of the current class for unpacking the dictionary
        return self.__class__(**kwargs)

    def __sub__(self, other):
        """
        Subtracts one vector from another.

        Args:
            :self: The object itself
            :other: The other vector to be subtracted

        Returns:
            :tuple: A new vector that is the difference of the two vectors
        """
        # Making sure that the two vectors are of the same type
        if type(self) != type(other):
            # Asks other operand to perform the operation
            return NotImplemented # Doesn't raise an exception immediately

        # Store the difference of the two vectors in a key-value pair
        kwargs = {i : (getattr(self, i) - getattr(other, i)) for i in vars(self)}

        # Returning an instance of the current class for unpacking the dictionary
        return self.__class__(**kwargs)

    def __mul__(self, other):
        """
        Multiplies a vector by a scalar or another vector.

        Args:
            :self: The object itself
            :other: The scalar or vector to multiply the vector by

        Returns:
            A integer or tuple obtained from multipleication
        """
        # Checking if the other operand is a scalar
        if type(other) in (int, float):
            # Store the product of the vector and the scalar in a key-value pair
            kwargs = {i: (getattr(self, i) * other) for i in vars(self)}
            # Returning an instance of the current class for unpacking the dictionary
            return self.__class__(**kwargs)
        elif type(self) == type(other): # Checking if the other operand is also a vector
            # Store the product of two vectors, or dot/scalar product
            kwargs = sum([getattr(self, i) * getattr(other, i) for i in vars(self)])
            # Returning the dot product
            return kwargs

        # Asks other operand to perform the operation to not raise an exception otherwise
        return NotImplemented

    def __eq__(self, other) -> bool:
        """
        Works as an equality operator; Compares 
        two vectors to see if they're equal or not

        Args:
            :self: The object itself
            :other: The other vector to be compared by

        Returns:
            :boolean: Indicate whether comparison leads True or False
        """
        # Checking if the object belong in the same class
        if type(self) != type(other): 
            return NotImplemented
        # If each attribute of current instance = each attribute of other instance
        return all(type(getattr(self, i)) == type(getattr(other, i)) for i in vars(self))

    def __ne__(self, other) -> bool:
        """
        Works as a negation operator; checks if two 
        vectors are not equal

        Args:
            :self: The object itself
            :other: The other object

        Returns:
            :boolean: Indicate if the values are unequal or not
        """
        # Statement to store the result of whether two objects are equal
        equality = self == other
        # Returning the opposite result
        return not equality

    def __lt__(self, other) -> bool:
        """
        Works as '<' operator; Used to compare
        an object with something else

        Args:
            :self: The object itself
            :other: The object being compared

        Returns:
            :boolean: Indicates if one object is 
            less than the other object
        """
        # Checking if the object belong in the same class
        if type(self) != type(other): 
            return NotImplemented
        # If each attribute of current instance < each attribute of other instance
        return self.norm() < other.norm()


    def __gt__(self, other) -> bool:
        """
        Works as '>' operator; Used to compare
        an object with something else

        Args:
            :self: The object itself
            :other: The object being compared

        Returns:
            :boolean: Indicates if one object is 
            greater than the other object
        """
        # Checking if the object belong in the same class
        if type(self) != type(other): 
            return NotImplemented
        # If each attribute of current instance > each attribute of other instance
        return self.norm() > other.norm()

    def __le__(self, other) -> bool:
        """
        Works as '<=' operator; Used to compare
        an object with something else

        Args:
            :self: The object itself
            :other: The object being compared

        Returns:
            :boolean: Indicates if one object is 
            less than or equal to the other object
        """
        # Checking if the object belong in the same class
        if type(self) != type(other): 
            return NotImplemented
        # Returning the opposite of greater than(less than or equal to)
        return not(self.norm() > other.norm())

    def __ge__(self, other) -> bool:
        """
        Works as '>=' operator; Used to compare
        an object with something else

        Args:
            :self: The object itself
            :other: The object being compared

        Returns:
            :boolean: Indicates if one object is 
            greater than or equal to the other object
        """
        # Checking if the object belong in the same class
        if type(self) != type(other): 
            return NotImplemented
        # Returning the opposite of greater than(less than or equal to)
        return not(self.norm() < other.norm())

class R3Vector(R2Vector):
    """
    A class to represent a vector in a 3D space.
    Inherits from the R2Vector class to extend a 2D vector to 3D.
    """
    def __init__(self, *, x, y, z) -> None: # * -> keyword-only arguments
        """
        Initialize the vector with the given x, y, and z coordinates.

        Args:
            :self: The object itself
            :x: x-axis coordinate of the vector
            :y: y-axis coordinate of the vector
            :z: z-axis coordinate of the vector
        """
        # Call the __init__ method of the R2Vector class
        super().__init__(x=x, y=y)
        self.z = z

    def cross(self, other):
        """
        Conducts cross, or vector product. Defined between 3-d
        vectors and results in a 3rd vector perpendicular to 
        both of them.

        Args:
            :self: The object itself
            :other: The other object

        Returns:
            :tuple: The cross product
        """
        # Checking if both objects are of the same type
        if type(self) != type(other):
            return NotImplemented

        # Conducting the cross product in a dictionary format
        kwargs = {
            'x': self.y * other.z - self.z * other.y,
            'y': self.z * other.x - self.x * other.z,
            'z': self.x * other.y - self.y * other.x,
        }

        # Returning an instance of the current class for unpacking the dictionary
        return self.__class__(**kwargs)



if __name__ == "__main__":
    # Creating a vector object
    # v_2D_1 = R2Vector(x=5, y=7)
    v_2D_1 = R3Vector(x=5, y=7, z=-8)
    print(f"1st v_2D: {v_2D_1}") # Should print out (2, 3)
    # print(f"{v_2D_1}'s magnitude: {v_2D_1.norm()}") # Prints out magnitude
    # print(f"v_2D = {v_2D}", f"\nrepr = {repr(v_2D)}") # Should print out (2, 3)
    # print(v_2D.norm()) # Should print out 3.605551275463989
    # print(v_2D.__dict__) # Should print out {'x': 2, 'y': 3}

    # Both return the 'x' coordinate of the vector
    # print(v_2D.z)
    # print(getattr(v_2D, 'z'))

    # v_2D_2 = R2Vector(x=3.4, y=1.25)
    v_2D_2 = R3Vector(x=3.4, y=1.25, z=7.75)
    print(f"2nd v_2D: {v_2D_2}") # Should print out (0.5, 1.25)
    # print(f"{v_2D_2}'s magnitude: {v_2D_2.norm()}") # Prints out magnitude

    print()
    '''
    print("v_2D_1 = v_2D_2?:", v_2D_1 == v_2D_2)
    print("v_2D_1 != v_2D_2?:", v_2D_1 != v_2D_2)
    print("v_2D_1 < v_2D_2?:", v_2D_1 < v_2D_2)
    print("v_2D_1 > v_2D_2?:", v_2D_1 > v_2D_2)
    print("v_2D_1 <= v_2D_2?:", v_2D_1 <= v_2D_2)
    print("v_2D_1 >= v_2D_2?:", v_2D_1 >= v_2D_2)

    # Creating a 3D vector object
    v_3D = R3Vector(x=3, y=2, z=4)
    print(f"v_3D: {v_3D}") # Should print out (2, 3)
    # print(f"v_3D = {v_3D}", f"\nrepr = {repr(v_3D)}") # Should print out (2, 2, 4)
    # print(v_3D.norm()) # Should print out 2.8284271247461903(for now)
    # print(v_3D.__dict__) # Should print out {'x': 2, 'y': 2, 'z': 4}

    # Both return the 'x' coordinate of the vector
    print(v_3D.x)
    print(getattr(v_3D, 'x'))
    '''

    v3 = v_2D_1 + v_2D_2
    v4 = v_2D_1 - v_2D_2
    v5 = v_2D_1 * v_2D_2
    v6 = v_2D_1 * 6
    v7 = v_2D_2 * 7
    v8 = v_2D_1.cross(v_2D_2)

    print(f"v3: {v_2D_1} + {v_2D_2} = {v3}") # Should print out (2.5, 4.25)
    print(f"v4: {v_2D_1} - {v_2D_2} = {v4}") # Should print out (1.5, 1.75)
    print(f"v5: {v_2D_1} * {v_2D_2} = {v5}") # Should print out 
    print(f"v6: {v_2D_1} * 6 = {v6}")
    print(f"v7: {v_2D_2} * 7 = {v7}")
    print(f"{v_2D_1} x {v_2D_2} = {v8}")
    print()
