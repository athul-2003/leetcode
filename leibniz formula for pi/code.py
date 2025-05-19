def calculatePi(n):
  sign=1
  a=1
  b=1
  sum_num=0
  
  for i in range(n):
    sum_num=sum_num+sign*(a/b)
    sign*=-1
    b=b+2   
    
  return sum_num*4
