
def conv():
    fa = float(input('Write the Fahrenheit degrees: '))
    ce = round((fa - 32)*(5/9),2)
    print(f'The conversion of {fa} degrees Fahrenheit is {ce} degrees Celsius.')

if __name__=='__main__':
   conv()
   
    