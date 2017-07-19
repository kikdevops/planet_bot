class Operator:
   def __init__(self):
       self.__ids = []

   def rotate(self, l, n):
    return l[n:] + l[:n]

   @property
   def id(self):
       self.__ids = self.rotate(self.__ids, 1)
       return self.__ids[1]

   @id.setter
   def id(self, mas):
       for k in mas:
           self.__ids.append(k.lower())
