from bwsi_grader.python.palindrome import grader

def student_func(x):
  x = "".join(x.split()).lower()
  return x==x[::-1]


if __name__ == "__main__":
  grader(student_func)
