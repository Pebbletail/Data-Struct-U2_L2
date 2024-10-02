#Luke Brudnok
#9/24/24
import ctypes

class DynamicArray:
  
  def __init__(self):
    self.__n = 0
    self.__capacity = 1
    self.__A = self.__make_array(self.__capacity)

  def __make_array(self, c):
    """return new array with capacity c"""
    return (c * ctypes.py_object)()

  def __resize(self):
    if self.__n == self.__capacity:
      self.__capacity *= 2
      temp = self.__make_array(self.__capacity)
      for i in range(self.__n):
        temp[i] = self.__A[i]
      self.__A = temp

  def append(self, element):
    self.__resize()
    ind = self.__n
    self.__A[ind] = element
    self.__n += 1


  def get_cap(self):
    return self.__capacity

  def __len__(self):
    return self.__n

  def __getitem__(self, index):
    """return element at index"""
    if index <= 0 or index >= self.__n:
        raise IndexError("invalid index")
    
    return self.__A[index]

  def __str__(self):
    if self.__n == 0:
        return "[]"

    out = '['
    for i, element in enumerate(self.__A):
        try:
            out += str(element) + ', '
            temp = self.__A[i+1]
        except:
            break
    return out[:-2] + ']'