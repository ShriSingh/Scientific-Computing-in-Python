# Learning Recursion by Solving the Towe of Hanoi Puzzle
NUMBER_OF_DISKS = 5
A = list(range(NUMBER_OF_DISKS, 0, -1))
B = []
C = []

def move(n, source, auxiliary, target):
    """
    Moves the disks by popping them off and appending them in the last position
    Then calls itself recursively to move the next disk
    :param n: int - number of disks
    :param source: list - source list
    :param auxiliary: list - auxiliary list
    :param target: list - target list
    """
    # If there are no disks to move, return and exit the function
    if n <= 0:
        return
    # move n - 1 disks from source to auxiliary, so they are out of the way
    move(n - 1, source, target, auxiliary)
    # move the nth disk from source to target
    target.append(source.pop())
    # display our progress
    print(A, B, C, '\n')
    # move the n - 1 disks that we left on auxiliary onto target
    move(n - 1,  auxiliary, source, target)


# initiate call from source A to target C with auxiliary B
print(move(NUMBER_OF_DISKS, A, B, C))
