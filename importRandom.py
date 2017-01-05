'''
In code, an import statement consists of the following:

The import keyword

The name of the module

Optionally, more module names, as long as they are separated by commas
'''
#The random.randint() function call evaluates to a random integer value
#between the two integers that you pass it.
import random
for i in range(5):
    print(random.randint(1, 10))
