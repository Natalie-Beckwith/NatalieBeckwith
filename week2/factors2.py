# factors in a class

class factors2:
  def __call__(self, n):
    factors = []
    for value in range(1, n + 1):
      if n % value == 0:
        factors.append(value)
    return(factors)
