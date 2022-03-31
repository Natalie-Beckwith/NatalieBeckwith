class factorial:
  def __call__(self, n):
    f = 1
    for i in range(1, n + 1):
      f = f * i
    return(f)
    