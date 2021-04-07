def student_func(x):
    if x%3==0 and x%5!=0:
        return 'three'
    elif x%5==0 and x%3!=0:
        return 'five'
    elif x%3==0 and x%5==0:
        return 'threefive'
    else:
        return x

from bwsi_grader.python.three_five import grader
grader(student_func)