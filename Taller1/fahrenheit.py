
def conv():
    fa = float(input('Write the Fahrenheit degrees: '))   #input to enter Fahrenheit degrees
    ce = round((fa - 32)*(5/9),2)  # Convert Fahrenheit to Celsius using the formula (Fahrenheit - 32) * (5/9)
    print(f'The conversion of {fa} degrees Fahrenheit is {ce} degrees Celsius.') # Print the conversion result

if __name__=='__main__':
   conv()
   
    