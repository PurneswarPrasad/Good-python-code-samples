# Errors and Exception
x=-5
assert (x>=0), "Since assertion is wrong, error is thrown"

#Try and Except
try:
  a=5/0
  b=1+'4'
except ZeroDivisionError as e1:
  print(e1)
except TypeError as e2:
  print(e2)
#Among these upper two except blocks, the first error is caught
else:
  print('Everything\'s fine') #Run if there's no error
finally:
  print('Cleaning up...') #Run everytime
---------------------------------------------------------
#User-defined Error function
#We defined a 'ValueTooHighError' function
class ValueTooHighError(Exception):
  def __init__(self, message, value):
    self.message=message
    self.value=value

#We defined a 'ValueTooSmallError' function
class ValueTooSmallError(Exception):
  pass

def test_value(x):
  if x>200:
    raise ValueTooHighError('Value is too high', x)
  if x<5:
    raise ValueTooSmallError('Value is too small')

try:
  test_value(201)
except ValueTooHighError as e1:
  print(e1.message, e1.value)
except ValueTooSmallError as e2:
  print(e2)
---------------------------------------------------------
