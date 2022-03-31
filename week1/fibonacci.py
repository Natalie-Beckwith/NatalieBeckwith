def fibonacci():
  n = int(input('Type the nth term in the fibonacci sequence: '))
  goFibonacci(n)

def goFibonacci(n):
  a=0
  b=1
  fibList = [0]
  
  if n <=0:
    print('Number must be greater than 0.')
    fibonacci()
    
  elif n == 1:
    print(fibList)
    return
  
  else:
    fibList.append(1)
    for i in range(2,n):
      c = a + b
      a = b
      b = c
      fibList.append(c)
  print(fibList)
  