class Operator:
   def __init__(self):
       self.__ids = []

   def rotate(self, l, n):
    if len(l) == 1:
        res = l
    else:
        res = l[n:] + l[:n]
    return res

   @property
   def id(self):
       self.__ids = self.rotate(self.__ids, 1)
       return self.__ids[1]

   @id.setter
   def id(self, mas):
       for k in mas:
           self.__ids.append(k.lower())
