from bwsi_grader.python.three_five import grader

def student_func(x):
  if x%3==0 or x%5==0:
    if x%3==0 and x%5==0:
      return "threefive"
    else:
      if x%3==0:
        return "three"
      elif x%5==0:
        return "five"

  else:
    return x
  
if __name__ == "__main__":
  grader(student_func)
