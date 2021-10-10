# Program to handle multiple errors with one except statement
try : 
    a = 3
    if a < 4 :
 
        # throws ZeroDivisionError for a = 3 
        b = a/(a-3)
     
    # throws NameError if a >= 4
    print ("Value of b = ", b)
 
# note that braces () are necessary here for multiple exceptions
#except (ZeroDivisionError , NameError ) as e:
#	print(e)

except ZeroDivisionError as e1:
	print(e1)
except NameError as e2:
	print(e2)
