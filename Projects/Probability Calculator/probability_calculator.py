"""
Building a Probability Calculator project
- Determine the approximate probability of drawing certain
balls randomly from a hat
"""

import copy
import random

class Hat:
    """
    Takes a variable number of arguments that specify the number
    of balls of each color that are in that hat
    """
    def __init__(self, **kwargs):
        """
        Creating a Hat class with a constructor
        that specifies various ball colors and the number
        of balls of each color

        Parameters:
            self (object):
                The instance of the Hat object
            **kwargs:
                Multiple ball colors of various quantities
        """
        # A list to store the collection of ball colors in the "hat"
        self.contents = []
        # Going thru every ball of every color
        for color, amount in kwargs.items():
            # Setting the attributes(color and quantity) of each ball
            setattr(self, color, amount)
            # Adding all the balls to the list
            for _ in range(0, amount):
                self.contents.append(color)

    def draw(self, balls_drawn):
        """
        Method that indicates the number of balls drawn
        from the hat. Removes the balls at random and be returned
        as a list of strings(shouldn't go back into the hat).
        Returns all the balls if the number of balls to draw 
        exceeds the available quantity.

        Parameters:
            self (object):
                The instance of the Hat object
            balls_drawn (int):
                Number of balls drawn from the hat
        """
        # Storing the list of balls drawn from the hat
        draw_list = []
        # Storing the balls list in the hat
        contents = self.contents
        # Comparing the number of balls drawn from the hat to the number of balls in the hat
        if balls_drawn > len(contents):
            return contents
        else:
            while len(draw_list) < balls_drawn:
                index = random.randint(0, len(contents) - 1)
                ball = contents[index]
                contents.remove(ball)
                draw_list.append(contents)
        return draw_list

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    """
    Calculates the probability of certain balls drawn from a hat

    Parameters:
        hat (object):
            Object containing balls
        expected_balls (object):
            Indicates the exact group of balls will be drawn
        num_balls_drawn (int):
            Number of balls to draw out of the hat
        num_experiments (int):
            Number of experiments to perform. The more experiments
            are performed, the more accurate the approximate
            probability will be
    Returns:
        probability (int):
            Probability values for a certain expected balls drawn
            from a hat
    """
    pass

if __name__ == "__main__":
    hat = Hat(red=1, blue=3, green=2)
    print(hat)
