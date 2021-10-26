#import EAN13 from barcode module
from barcode import EAN13

#Lets make sure to pass the number as a String
number  = '5901234123457'

#Now, lets create an object of EAN13
#Class and pass the number
my_code = EAN13(number)

# Now, let's create an object of EAN13
# class and pass the number
my_code = EAN13(number)
  
# Our barcode is ready. Let's save it.
my_code.save("new_code")
