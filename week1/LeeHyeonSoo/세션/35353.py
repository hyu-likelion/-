def p(x):
    y=x.lower()
    z=y.split()
    k="".join(z)
    if k==k[::-1]:
        return True
    else :
        return False


def threefive(x):
    if x%3==0 and x%5==0:
        return 'threefive'
    elif x%3==0:
        return 'three'
    elif x%5==0:
        return 'five'
    else:
        return x

from bwsi_grader.python.three_five import grader

grader(threefive)

from bwsi_grader.python.palindrome import grader
grader(p)

