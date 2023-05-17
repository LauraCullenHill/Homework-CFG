"""
A] Write a program that takes in an input file and prints out a list with the final
order of who’s in the queue.
You are expected to use the provided input file hw3_q1.txt to develop and test your
solution.
The first word on each line will either be “JUMP” or “JOIN” and the second word the
name of the person, the word “JUMP” means the person in question has gone to
the front of the queue, if the word is “JOIN” it means they have joined the back of
the queue.
You are expected to identify and use a container from the collections module for
your solution.
"""


from collections import deque


class JumpJoinQueue:
    def __init__(self):
        self.queue = deque()

    def append(self, x): # O(1)
        self.queue.append(x)  # Inserting element x to the end of the queue

    def is_empty(self): # O(1)
        return len(self.queue) == 0

    def process_queue(self, input_file): # O(n)
        with open(input_file, 'r') as file:
            for line in file:
                operation, name = line.strip().split()
                if operation == 'JUMP':
                    self.append(name)  # Add person to the back of the queue
                elif operation == 'JOIN':
                    self.queue.append(name)  # add the person from the front of the queue

    def print_list(self): # O(n)
        print(list(self.queue))


# Create an instance of QueueProcessor
processor = JumpJoinQueue()

# Process the queue from the txt file
processor.process_queue('hw3_q1.txt')

# Get the final order and print it
output = processor.print_list()


"""
B] What is the time and space complexity of your solution? If you are making
any assumptions, list them.
Add your answer to this as a comment above or below your solution to Part A.
"""

"""
Assumptions:
- Input file exists and is entered correctly
- Input file is in the correct format with JUMP or JOIN



Time and Space Complexity: O(n)
(see comments on code)
"""
