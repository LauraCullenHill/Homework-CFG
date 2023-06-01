## Section 3: Theory Challenge - Hashing [25 points]

1. Design a basic hash function, keeping in mind memory constraints
and how you would deal with hash collisions.
6 points


def hash_add(a, b):
   return hash(a + b)
     
Could try chaining to avoid hash collisions?


2. Walkthrough your function with an example where there is no hash
collision.
12 points

a is 10 
b is 12
the sum of these is 22
so 22 is assigned a hash value at the 22nd spot
This spot is empty so there is no collision



3. Walkthrough your function with an example of a hash collision 7 points

a is 8
b is 14
the sum of these is 22
There is already a value at 22
There is a collision (two objects/ outputs have the same hash value) 
The next spot in the chain can be taken for one of the values


 
