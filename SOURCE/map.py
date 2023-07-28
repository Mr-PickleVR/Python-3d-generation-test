import random
I=True
_=False
lvl_1 = [[I,I,I,I,I,I,I,I,I],
          [I,_,_,_,_,_,_,_,I],
          [I,I,_,I,I,I,I,_,I],
          [I,I,_,I,_,_,I,_,I],
          [I,I,_,_,_,I,_,_,I],
          [I,I,I,I,I,I,_,I,I],
          [I,I,_,_,_,I,_,I,I],
          [I,_,_,I,_,_,_,_,I],
          [I,I,I,I,I,I,I,I,I]]
lvl_2 = [[I,I,I,I,I,I,I,I,I],
          [I,_,I,_,_,_,I,I,I],
          [I,_,_,_,I,_,I,I,I],
          [I,I,I,_,I,_,_,_,I],
          [I,_,_,_,_,_,I,I,I],
          [I,_,I,I,I,I,2,_,I],
          [I,_,I,_,_,_,I,_,I],
          [I,_,_,_,I,_,_,_,I],
          [I,I,I,I,I,I,I,I,I]]
def getMap():
  _=False
  I = True
  border = [[I,I,I,I,I,I,I,I,I],
          [I,_,_,_,_,_,_,_,I],
          [I,_,_,_,_,_,_,_,I],
          [I,_,_,_,_,_,_,_,I],
          [I,_,_,_,_,_,_,_,I],
          [I,_,_,_,_,_,_,_,I],
          [I,_,_,_,_,_,_,_,I],
          [I,_,_,_,_,_,_,_,I],
          [I,I,I,I,I,I,I,I,I]]
  for i in range(1, 8):
    for j in range(1,8):
      if random.randint(0,2) == 1:
        border[j][i] = I
      else: 
        border[j][i] = _
  print(border)
  return border
