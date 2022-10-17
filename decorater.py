def sqvare (f):
    def innar(a, b):
        a = a*a
        b = b*b
        return f(a, b)
    return innar    


@sqvare

def add (a, b):
   return a + b
print(add(5, 3))

@sqvare

def add (a, b):
   return a * b
print(add(2, 3))





def check_denom(f):
   def innar(a, b):
      if b != 0:
         return f(a, b)
      else:
         return 'b value should not be 0'
   return innar 
@check_denom         
def dir (a, b):
   return a / b
print(dir(10, 5)) 
print(dir(0, 2))  
print(dir(2, 0))  # ZeroDivisionError: division by zero





