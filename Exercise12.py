# Learning Interfaces by Building an Equation Solver

# Importing 'abc' library to implement interface
from abc import ABC, abstractmethod
# Importing 're' module for substituting regular expressions the coefficients
import re

"""
'ABC' stands for Abstract Base Classes.
    -> Enables you to turn a regular class into an abstract class
    using 'abstractmethod'
        -> A class that acts as a blueprint for concrete class

In Python, data types are recognized during runtime(when the code is
executed)
    -> Therefore no need to specify the data type of a variable when
    you declare it
    -> You can do it in this format: variable: <data type> = value
    -> Python doesn't enforce type used to annotate

hasattr
    -> Built-in function takes an object as its first argument and
    a string representing an attribute name as its 2nd argument.
    -> Returns a boolean indicating if the object has the specified
    attribute

Regex Expressions:
    -> re.sub(): replaces text inside a string based on a regex pattern
    -> Lookaround
        -> An assertion in regex patterns that matches a certain pattern
        without consuming characters in the string
        -> Lookbehind
            -> (?<=...) : positive 
                -> Used to match character only when preceded by a
                character
                -> E.g.: (?<=l)a : Match 'a' character only when preceded
                by an 'l'
            -> (?<!...) : negative
                -> Used to match character only if isn't preceded by an 'l'
                -> E.g.: (?<!l)a : Match 'a' only when not preceded by an 'l'
        -> Lookahead
            -> (?=...) : positive
                -> Used to match character only when followed by another
                character
                -> E.g.: a(?=t) : Match 'a' only when followed by a 't'
            -> (?!...) : negative
                -> Used to match character only when not followed by another
                character
                -> E.g.: a(?!t) : Match 'a' only when not followed by a 't'

f-strings has the capability of forcing the output to be right/left-aligned,
or centered
    -> Done with the expression inside the curly braces in a f-string, then a
    colon, the alignment option, and the number representing the width
    -> Alignment Options:
        -> Left-Align: '<'
        -> Right-Align: '>'
        -> Center: '^'
    ->  The number is the count of the characyers in which you want to arrange
    the text
    -> E.g.: f'{"Hello World":>20}' - Prints the string from the example above
    would result in right-aligned text arranged in a space of 20 characters

Structural Pattern Matching
    -> A Python construct that enables matching a pattern with a subject value
        -> Specified after 'match' keyword
        -> Pattern is specified after the 'case' statement 
"""

class Equation(ABC):
    """
    Defines an algebraic expression that can be analyzed
    and solved. Uses 'ABC' library and its method to make it
    """

    # Setting class attribute 'degree' & 'type'(describes algebraic expression)
    # Using it for validating arguments passed in the objects
    degree: int
    type: str

    def __init__(self, *args):
        """
        Initializes the Equation object with the given arguments

        Args:
            :self: Equation object
            :*args: Variable number of arguments(degree of the equation)
        """
        # Storing the value of the coefficients present
        coefficient = self.degree + 1
        # Checking if the lengths of arguments or coefficients are equal
        if coefficient != len(args):
            raise ValueError(
                f"'{self.__class__.__name__}' object takes {self.degree + 1} \
                    positional arguments but {len(args)} were given"
            )

        # Checking if the arguments are integers or floats
        if any(not isinstance(argument, (int, float)) for argument in args):
            raise TypeError(
                "Coefficients must be 'int' or 'float'"
            )

        # Checking if the highest degree coefficient is different from zero
        first_arg = args[0]
        if first_arg == 0: # first argument is the highest degree coefficient
            raise ValueError(
                "Highest degree corefficient must be different from zero"
            )

        # Storing the coefficients in a dictionary with their respective indexes
        self.coefficients = {(len(args) - idx - 1): arg for idx, arg in enumerate(args)}

    def __init_subclass__(cls):
        """
        Called whenever a class that defines it is subclassed.
        Enables customization of child classes.

        Args:
            :cls: New child class

        Returns:
            :boolean: Indicates if the object has the specified
            attribute
        """
        # If no 'degree' is present in Equation's child class or object
        if not hasattr(cls, "degree"):
            raise AttributeError(
                f"Cannot create '{cls.__name__}' class: missing required \
                attribute 'degree'"
            )

        # If no 'type' is present in Equation's child class or object
        if not hasattr(cls, "type"):
            raise AttributeError(
                f"Cannot create '{cls.__name__}' class: missing required \
                attribute 'type'"
            )

    def __str__(self):
        """
        Returns a string representation of the Equation object
        
        Args:
            :self: Equation object
        Returns:
            :equation_string: String representation of the 
            Equation object
        """

        # Storing each term (coefficient ^ n) of your equation
        terms = []

        # Iterating over the keys and values stored in the corefficients attribute
        for idx, coef in self.coefficients.items():
            # If the coefficient at the current index has a falsy value(i.e. '0')
            if not coef:
                # Skip over it
                continue

            # If the coefficient has a non-zero value
            if idx == 0:
                # Adding ':+' to display the sign b/w terms
                terms.append(f'{coef:+}')
            elif idx == 1:
                terms.append(f'{coef:+}x')
            else:
                terms.append(f'{coef:+}x**{idx}')

        # Joining the terms in a string
        equation_string = (' '.join(terms) + ' = 0').strip('+')
        # equation_string = re.sub('1', '', equation_string) -> Substituting '+- 1x' for '+- 1'

        # Substituting '1' only when it's no preceded by a digit and followed by x
        equation_string = re.sub(r'(?<!\d)1(?=x)', '', equation_string) # Using both look

        return equation_string

    @abstractmethod
    def solve(self):
        """
        Abstract method that solves the equation and returns the solution
        """
        pass

    @abstractmethod
    def analyze(self):
        """
        Abstract method that analyzes the equation and returns additional info
        """
        pass

class LinearEquation(Equation):
    """
    A type of equation, written in the form of 'ax + b = 0'. Inherits 
    from the Equation class by implementing all its abstract methods
    """

    # Setting the degree of linear equation expressions(1st degree)
    degree = 1
    # Setting the type of equation for the linear expressions
    type = "Linear Equation"

    def solve(self: Equation) -> list:
        """
        Inherited from Equation class. Solves the linear equation
        by solving for 'x' value from the slope and y-intercept

        Args:
            :self: LinearEquation object

        Returns:
            :x_value: Solution for x-value 
        """
        # Extracting the terms from the coefficients attribute
        slope, y_intercept = self.coefficients.values()
        # Getting the solution(x-value) of the linear equation in a list
        x_value = [- y_intercept / slope]

        return x_value

    def analyze(self) -> dict:
        """
        Returns the slope and y-intercept to provide additional
        info about the equation

        Args:
            :self: LinearEquation object
        
        Returns:
            :additional_info: The dictionary returning slope and \
            y-intercept as a label-value pair
        """
        # Storing the slope and y-intercept values from coefficients dictionary
        slope, y_intercept = self.coefficients.values()

        # Creating a new dictionary
        additional_info = {'slope': slope, 'y-intercept': y_intercept}

        return additional_info

class QuadraticEquation(Equation):
    """
    A type of equation, written in the form of 'ax^2 + bx + c = 0'.
    Inherits from the Equation class by implementing all its abstract
    methods
    """

    # Setting the degree of quadratic equation expressions(2nd degree)
    degree = 2
    # Setting the type of equation for the quadratic expressions
    type = "Quadratic Equation"

    def __init__(self, *args):
        # Calling the __init__ class for defining a new attribute
        super().__init__(*args)
        # Extracting the values from quadratic equation
        a, b, c = self.coefficients.values()
        # Calculating the delta or the discriminant
        self.delta = (b ** 2) - (4 * a * c)

    def solve(self) -> list:
        """
        Inherited from Equation class. Solves the quadratic 
        equation by 'x' value to calculate root values

        Args:
            :self: QuadraticEquation object

        Returns:
            :solution: Potential root values/solutions
        """
        # Extracting the values from quadratic equation
        a, b, _ = self.coefficients.values()
        # Calculating the root values
        root_1 = (-b + (self.delta ** 0.5)) / (2 * a)
        root_2 = (-b + (self.delta ** 0.5)) / (2 * a)
        # Intializing the list of solution/root values
        solution = []

        # If the discriminant is negative
        if self.delta < 0:
            return solution # The Equation doesn't have real solutions/roots
        if self.delta == 0:
            solution = [root_1] # Solution is coincident(same root values)

        # Otherwise, there are two unique solutions
        solution = [root_1, root_2]

        return solution

    def analyze(self) -> dict:
        """
        Inherited from Equation class. Solves the quadratic equation
        by 'x' value(vertex) and 'y' coordinate

        Args:
            :self: QuadraticEquation object

        Returns:
            :info_solution: Dictionary of vertex, 'y' coordinate, concavity, or 
        """
        # Extracting values from the equation
        a, b, c = self.coefficients.values()
        # Calculating the vertex
        x_vertex = -b / (2 * a)
        # Calculating the y-coordinate
        y_coordinate = (a * (x_vertex ** 2)) + (b * x_vertex) + c
        # Intializing the concavity & min_max
        concavity, min_max = ''

        if a < 0: # The equation graph(parabola) open downwards
            concavity = 'downwards'
            min_max = 'max'
        elif a > 0: # The equation graph(parabola) open upwards
            concavity = 'upwards'
            min_max = 'min'

        # Storing the calculated info in a dictionary
        info_solution = {'x(vertex)': x_vertex, 'y-coordinate': y_coordinate, 'concavity': concavity, 'min or max': min_max}

        return info_solution

def solver(equation: Equation) -> str:
    """
    Triggers the instance written in the classes
    to solve a given equation. Displays the results in a 
    formatted output.

    Args:
        :equation: The instance object

    Returns:
        :output_string: Prints out the type, solutions, 
        and the details for the equation
    """
    # Checking if 'equation' parameter is an instance of 'Equation' class
    if not isinstance(equation, Equation):
        raise TypeError(
            'Argument must be an Equation object'
        )

    # Centering the equation type with filler '-'s in a width of 24 characters
    output_string = f'\n{equation.type:-^24}'
    # Centering the equation(after converting object -> string) in a width of 24 characters
    output_string += f'\n\n{equation!s:^24}\n\n'
    # Centering 'Solutions' title in a width of 24 characters
    output_string += f'{"Solutions":-^24}\n\n'

    # Assigning the result to a variable
    results = equation.solve()
    # Intializing a list for storing solutions
    result_list = []

    # Using match/case to check the results
    match results:
        case []: # If there are no solutions
            result_list = ['No real roots']
        case [x]: # If there's only one solution
            result_list = [f'x = {x:+.3f}']
        case [x1, x2]: # If there are two solutions
            result_list = [f'x1 = {x1:+.3f}', f'x2 = {x2:+.3f}']

    # Iterating through the solutions in the list
    for result in result_list:
        # Aligning the solution to the equation
        output_string += f'{result:^24}\n'

    # Adding the "Details" title aligned to the center with '-' in a width of 24 characters
    output_string += f'\n{"Details":-^24}\n\n'

    # Assigning the additional info to a variable
    details = equation.analyze()
    # Intializing a list for storing additional info
    details_list = []

    # Using match/case to match the additional info
    match details:
        # If the additional info is from Linear Equation
        case {'slope': slope, 'y-intercept': y_intercept}:
            details_list = [f'slope =  {slope:>15.3f}', f'y-intercept = {y_intercept:>10.3f}']
        # If the additional info is from Quadratic Equation
        case {'x(vertex)': x_vertex, 'y-coordinate': y_coordinate, 'concavity': concavity, 'min or max': min_max}:
            min_max_coord = f'({x_vertex:.3f}, {y_coordinate:.3f})'
            details_list = [f'concavity = {concavity:>12}', f'{min_max} = {min_max_coord:>18}']

    # Iterating through the additional info in the list
    for detail in details_list:
        # Aligning the additional info to the equation
        output_string += f'{detail}\n'

    return output_string

if __name__ == "__main__":
    # eq = Equation() -> No need to instantiate an object with abstract methods
    lin_eq = LinearEquation(2, 3) # Needs to have all the inherited abstract methods
    quadr_eq = QuadraticEquation(-11, -1, 1)

    print(solver(lin_eq))
    print(solver(quadr_eq))

    '''
    print("Equation:", lin_eq)
    print("Solution for x:", lin_eq.solve())
    print("Additional Info:", lin_eq.analyze())

    print(solver(quadr_eq))
    print("Quadratic Equation:", quadr_eq)
    print("Solution for roots:", quadr_eq.solve())
    print("Additional Info:", quadr_eq.analyze())
    '''
