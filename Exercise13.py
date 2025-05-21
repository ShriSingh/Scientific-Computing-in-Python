# Learning Encapsulation by Building a Projectile Trajectory Calculator

"""
    Building a program that calculates and draws the
    trajectory of a projectile given the angle, speed,
    and height of the throw.
"""

"""
    Name-mangling 
        -> Means the attributes aren't directly accessible
        from outside the class using their given names like
            -> 2 underscores before an attribute name triggers 
            name mangling in Python; E.g.: __speed
            -> Name-mangled attributes indicate they are only 
            for internal use, despite being allowed

    Declaring and assigning certain sequence of strings as a tuple
    to __slots__ does:
        -> Efficients attribute access
        -> Prevent creation of __dict__ special attribute

    Encapsulation
        -> Getters
            -> Used to get the values from outside
                -> E.g.: @property def speed(self): return self.__speed
            -> '@property' decorator helps changes the method into a
            property
                -> The method isn't like a regular method, but it's used
                like an attribute
                    -> E.g.: c = Car() print(c.speed)
                        -> Private attribute '__speed' is accessed through
                        'speed' property of 'c'
        -> Setters
            -> Allows you to set the value of an attribute in an indirect
            manner
                -> E.g.: @number_of_eggs.setter def number_of_eggs(self, new_value): 
                self.__number_of_eggs = new_value
            -> Same as the getter, it's not called a method but used like an attribute
                -> E.g.: nest = Nest() nest.number_of_eggs = 12
                    -> This way of writing calls the setter and set the new value
"""

# Importing math module
import math

# Storing values of gravitational acceleration and some special symbols
GRAVITATIONAL_ACCELERATION = 9.81
PROJECTILE = "∙"
X_AXIS_TICK = "T"
Y_AXIS_TICK = "⊣"

class Projectile:
    """
    Defines the 'Projectile' object and its related methods
    """

    # Creating __slots__ tuple to allocate name-mangled attributes
    __slots__ = ('__speed', '__height', '__angle')

    def __init__(self, speed, height, angle):
        """
        Initializes the class using three arguments
        
        Args:
            :self: The initialized object in meters
            :speed: The starting speed in meters 
            :height: The starting height in meters
            :angle: The starting angle of the throw of
                the projectile in degrees
        """
        # Assigning name-mangling attributes to the arguments
        self.__speed = speed
        self.__height = height
        self.__angle = math.radians(angle) # Storing it in radians for calculation

    def __str__(self) -> str:
        """
        Provides proper string representing the Projectile object

        Args:
            :self: The Projectile object

        Returns:
            :output_string: Returns projectile details - speed, 
            height, angle, and displacement
        """
        # Formatting the details of the Projectile
        output_string = '\nProjectile details:\n' + \
            f'speed: {self.speed} m/s\n' + \
            f'height: {self.height} m\n' + \
            f'angle: {self.angle}°\n' + \
            f'displacement: {self.__calculate_displacement():.1f} m\n'

        return output_string

    @property
    def speed(self):
        """
        Getter for __speed attribute
        """
        return self.__speed

    @property
    def height(self):
        """
        Getter for __height attribute
        """
        return self.__height

    @property
    def angle(self):
        """
        Getter for __angle attribute given in degrees
        saved internally as radians
        """
        return round(math.degrees(self.__angle))

    @speed.setter
    def speed(self, s):
        """
        Setter for __speed attribute
        """
        self.__speed = s

    @height.setter
    def height(self, h):
        """
        Setter for __height attribute
        """
        self.__height = h

    @angle.setter
    def angle(self, a):
        """
        Setter for __angle attribute;
        received in degrees, but saved internally as radians
        """
        self.__angle = math.radians(a)

    def __repr__(self):
        """
        A programmer-friendly function provides a string 
        that can be used to recreate the object

        Args:
            :self: The Projectile object

        Returns:
            :repr_string: Returns the instantiated object name
            with the inputs
        """
        repr_string = f"{self.__class__}({self.speed}, {self.height}, {self.angle})"

        return repr_string

    def __calculate_displacement(self) -> float:
        """
        Returns the displacement of the projectile

        Args:
            :self: The Projectile object

        Returns:
            :displacement: Projectile displacement value
        """
        # Calculating the first half of the formula: v * cos(angle)
        horizontal_displacement = self.__speed * math.cos(self.__angle)
        # 1st Part of the second half of the second half of the formula: v * sin(angle)
        vertical_displacement = self.__speed * math.sin(self.__angle)
        # 2nd Part of the second half of the formula: sqrt((v * sin(angle)) ^ 2) + (2 * g * h))
        sqrt_component = math.sqrt((vertical_displacement ** 2)
                                    + (2 * GRAVITATIONAL_ACCELERATION * self.__height))
        # Calculating the total displacement
        displacement = horizontal_displacement * (vertical_displacement +
                                                  sqrt_component) / GRAVITATIONAL_ACCELERATION

        return displacement

    def __calculate_y_coordinate(self, x):
        """
        Calculating the y-coordinate or the vertical position
        in the trajectory of the projectile

        Args:
            :self: The Projectile object
            :x: The horizontal position

        Returns:
            :y_coordinate: The y-coordinate of the 
            projectile's trajectory
        """
        # Storing the height of the projectile
        height = self.__height
        # Storing the calculation with the horizontal position: x * tan(angle)
        horizontal_angle = (x * (math.tan(self.__angle)))
        # Storing the calculation of the complex fraction: (g * x ** 2) /
        # (2 * v ** 2 * (cos(angle)) ** 2)
        acceleration = ((GRAVITATIONAL_ACCELERATION * (x ** 2)) / (2 * (self.__speed ** 2)
                                                           * (math.cos(self.__angle) ** 2)))
        # Combining everything with together: height + (x * tan(angle)) -
        # (g * x ** 2) / (2 * v ** 2 * (cos(angle)) ** 2)
        y_coordinate = height + horizontal_angle - acceleration

        return y_coordinate

    def calculate_all_coordinates(self):
        """
        Calculates the coordinates for all 'x' values from
        '0' up to the displacement rounded up(not exclusive),
        and then returns them as a list of tuples(x, y)

        Args:
            :self: The Projectile object

        :Returns:
            :coordinate_list: The coordinates for all 'x' values
            from '0' to the displacement
        """
        # Calculating the displacment rounded up using math.ceil()
        displacement = math.ceil(self.__calculate_displacement())
        # Intializing the list of coordinates to be returned
        coordinate_list = []

        # Going thru values from 0 to displacement value
        for x in range(displacement):
            # Calculating 'y' value
            y = self.__calculate_y_coordinate(x)
            # Creating a tuple
            coordinate = (x, y)
            # Appending the tuple
            coordinate_list.append(coordinate)

        return coordinate_list

class Graph:
    """
    A class that draws the trajectory of a projectile
    """
    # Storing private attribute '__coordinates' where the list of
    # coordinates will be stored
    __slots__ = ('__coordinates')

    def __init__(self, coordinates):
        self.__coordinates = coordinates

    def __repr__(self):
        return f'Graph({self.__coordinates})'

    def create_coordinates_table(self):
        """
        Creates a table of x & y coordinates of the projectile
        when its speed, angle, and height changes from the throw

        Args:
            :self: The Graph object

        Returns:
            :table: The table with the x & y coordinates
        """
        # Setting the title of the table
        table = '\n  x      y\n'

        # Iterating through the coordinates to add them to the table
        for x, y in self.__coordinates:
            table += f'{x:>3}{y:>7.2f}\n'

        return table

    def create_trajectory(self):
        """
        Create 

        Args:
            :self: The Graph object

        Returns:
            :x_max, y_max: The maximum x & y values
        """
        # Intializing a list to store the rounded coordinates
        rounded_coords = []

        # Iterating through the coordiantes to store the rounded coordinates
        for x, y in self.__coordinates:
            rounded_coords.append((x, round(y)))

        # Storing the maximum x & y values
        x_max = max(x for x, y in rounded_coords) # Max rows needed
        # x_max = max(rounded_coords, key=lambda i: i[0])[0]
        y_max = max(y for x, y in rounded_coords) # Max columns needed
        # y_max = max(rounded_coords, key=lambda j: j[1])[1]

        # Creating a matrix list of the rows and columns
        matrix_list = [[' ' for _ in range(x_max + 1)] for _ in range(y_max + 1)]

        # Changing the elements in 'matrix_list' at the coordinates in the list
        # to the PROJECTILE symbol
        for (x, y) in rounded_coords:
            if 0 <= x <= x_max and 0 <= y <= y_max:
                matrix_list[y_max - y][x] = PROJECTILE

        # Joining the inner lists to hava list of strings
        matrix = [''.join(row) for row in matrix_list]
        # Adding the x & y axis ticks
        matrix_axis = [Y_AXIS_TICK + row for row in matrix]
        matrix_axis.append(" " + X_AXIS_TICK * (len(matrix[0])))

        # Making the final output a multiline string
        matrix = '\n' + '\n'.join(matrix_axis) + '\n'

        return matrix

def projectile_helper(speed, height, angle):
    """
    A utility function to return the projectile object,
    details of the projectile, the table of coordinates, 
    and the graph of the trajectory

    Args:
        :speed: The speed of the projectile
        :height: The height of the projectile
        :angle: The angle of the projectile
    Returns:
        None
    """
    projectile = Projectile(speed, height, angle)
    print(projectile)
    projectile_coordinates = projectile.calculate_all_coordinates()
    projectile_graph = Graph(projectile_coordinates)
    print(projectile_graph.create_coordinates_table())
    print(projectile_graph.create_trajectory())

if __name__ == "__main__":
    # ball = Projectile(10, 3, 45)
    # ball = Projectile(12, 12, 12)
    # ball_1 = Projectile(45, 45, 45)

    # displacement_of_ball = ball._Projectile__calculate_displacement()
    # ball_y_coordinate = ball._Projectile__calculate_y_coordinate(2)
    # ball_all_coordinates = ball.calculate_all_coordinates()
    # ball_repr = ball.__repr__()

    # ball_1_y_coordinate = ball_1._Projectile__calculate_y_coordinate(2)

    # print(ball)
    # print(ball_1)
    # print(ball_repr) # Returns the object

    # graph = Graph(ball_all_coordinates)
    # print(graph.create_coordinates_table())
    # for row in graph.create_trajectory():
        # print(row)

    # print("Displacement of ball to (10, 3, 45):", displacement_of_ball)
    # print(f'Coordinates of ball(10, 3, 45):, {ball_all_coordinates}\n')

    # print("y-Coordinate to (10, 3, 45):", ball_y_coordinate)
    # print("y-Coordinate to (45, 45, 45):", ball_1_y_coordinate)

    projectile_helper(45, 8, 7)
