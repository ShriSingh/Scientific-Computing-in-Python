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
        diagonal_length = (((self.width ** 2) + (self.height ** 2)) ** 0.5)

        return diagonal_length