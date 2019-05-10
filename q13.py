import math
while True:
   try:
    a = int(float(input('enter a number')))
    break
   except:
    print('invalid')
def sqt(x):
    if x>0:
        print(math.sqrt(x))
    else:
        print('negative')
sqt(a)