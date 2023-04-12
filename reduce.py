""" Reduce Function
    
    This script shows how the 'reduce function' in 'functools lib' works.
    Below are two demo function showing the implementation and results.
    
"""

from functools import reduce

def demo1(alist: list) -> int:
    result = reduce(lambda x, y: x*y, alist)
    return result

def demo2(alist: list) -> str:
    return reduce(lambda x, y: x+y, alist)

if __name__ == "__main__":

    milist1 = [1,2,3,4,5]
    print(f"Demo1: {demo1(milist1)}")
    
    milist2 = ['h','e','l','l','o','o']
    print(f"Demo2: {demo2(milist2)}")


""" Expected Result:
    Demo1: 120
    Demo2: helloo
"""

