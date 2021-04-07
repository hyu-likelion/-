def student_func(x):
    # `x` is a string
    # this function should return either `True` or `False`
    x = "".join(x.split()).lower()
    return x==x[::-1]
from bwsi_grader.python.palindrome import grader
grader(student_func)

