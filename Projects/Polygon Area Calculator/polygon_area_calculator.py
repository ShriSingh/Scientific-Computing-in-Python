# Building a Polygon Area Calculator

class Rectangle:
    """
    Should initialize a 'rectangle' object with
    'width' and 'height' attributes. Needs to be 
    represented by 'Rectangle(width=5, height=10)'
    
    It should also contain:
        set_width
        set_height
        get_area: returns area (width * height)
        get_perimeter: (2 * width + 2 * height)
        get_diagonal: (width ** 2 + height ** 2) ** .5
        get_picture: Returns a string that represents the shape
        get_amount_inside: Returns the number of times the passed in shape
            could fit inside the shape(with no rotations)
    """

    def __init__(self, width, height):
        """
        Creating a Rectangle class with a constructor 
        that takes in width and height to calculate its 
        various attributes.

        Parameters:
            self (object):
                The rectangle object
            width (float): 
                The width of the rectangle
            height (float): 
                The height of the rectangle
        
        """
        self.width = width
        self.height = height

    def set_width(self, width):
        """
        Sets the width of the rectangle

        Parameters:
            self (object):
                The rectangle object
            width (float): 
                The new width of the rectangle
        """
        self.width = width

    def set_height(self, height):
        """
        Sets the height of the rectangle

        Parameters:
            self (object): 
                The rectangle object
            height (float): 
                The new height of the rectangle
        """
        self.height = height

    def get_area(self):
        """
        Calculates the area of a rectangle

        Parameters:
            self (object):
                The rectangle object

        Returns:
            area (float):
                The area of the rectangle
        """
        area = self.width * self.height

        return area

    def get_perimeter(self):
        """
        Calculates the perimeter, or boundary length, of the rectangle

        Paramters:
            self (object):
                The rectangle object

        Returns:
            perimeter (float):
                The perimeter(or boundary length) of the rectangle
        """
        perimeter = (2 * self.width) + (2 * self.height)

        return perimeter

    def get_diagonal(self):
        """
        Calculates the length of the diagonal of the rectangle

        Parameters:
            self (object):
                The rectangle object

        Returns:
            diagonal_length (float):
                The length of the diagonal of the rectangle
        """
        diagonal_length = round((((self.width ** 2) + (self.height ** 2)) ** 0.5), 3)

        return diagonal_length
    
    def get_picture(self):
        """
        Creating visual of the object using '*'

        Parameters:
            self (object):
                The rectangle object
        
        Returns:
            diagram (string):
                Outputs a figure of the object using '*'
        """
        # Checking if the shape's dimensions are too big
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        else: # Drawing up the diagram
            diagram = ""
            # Adding '*' width-wise based on height of the shape
            for _ in range(0, self.height):
                diagram += ("*" * self.width) + "\n"

            return diagram
        
    def get_amount_inside(self, shape):
        """
        Calculating the number of times a shape(entered by the user)
        can fit inside the object with no rotations

        Parameters:
            self (object):
                The instance of the object
            shape (object):
                The instance of the object to be fitted in the main object
        """
        instance = 0
        # Comparing the dimensions of object to be fitted in the main object
        if (shape.width < self.height) and (shape.height < self.height):
            # calculating the instances 
            instance = (self.height // self.height) * (self.width // shape.width)
            return instance
        # Returning instance as 0, the shape being fitted is bigger than the main object
        return instance

    def __str__(self):
        """
        Providing a string representation of the rectangle
        
        Parameters:
            self (object):
                The rectangle object

            rectangle_object (string):
                String representation of the Rectangle
        """

        rectangle_object = f"Rectangle(width={self.width}, height={self.height})"

        return rectangle_object


class Square(Rectangle):
    """
    Creating a Square class, which is a subclass of the Rectangle class.
    Can access the Rectangle class methods.

    Contains:
        set_side 
    """

    def __init__(self, side):
        """
        Creating a Square class with a constructor 
        that takes 'side' value and assigns it to Rectangle's 
        width and height attributes

        Parameters:
            self (object):
                The square object
            side (float): 
                The length of the side of the square
        """
        super().__init__(side, side)

    def set_side(self, side):
        """
        Setting the sides of the square by overriding
        Rectangle's 'width' and 'height' by Square's 'side'

        Parameters:
            self (object):
                The square object
            side (float):
                The length of the side of the square
        """
        self.width = side
        self.height = side

    def __str__(self):
        """
        Adding a string representation to the square object

        Parameters:
            self (object):
                The square object

        Returns:
            square_object (string):
                String representation of Square
        """

        square_object = f"Square(side={self.width})"

        return square_object


if __name__ == "__main__":
    rect = Rectangle(19, 4)
    print(rect)
    print("Area:", rect.get_area())
    print("Perimeter:", rect.get_perimeter())
    print("Diagonal:", rect.get_diagonal())
    print("Diagram:\n" + rect.get_picture())

    square = Square(7)
    print(square)
    print("Area:", square.get_area())
    print("Perimeter:", square.get_perimeter())
    print("Diagonal:", square.get_diagonal())
    print("Diagram:\n" + square.get_picture())
