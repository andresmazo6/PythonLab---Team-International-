def maximum():
    list = [0]   # Initialize a list to store numbers
    
    while True:
        lt_numbers = input('"Hello! Please enter a number (or -q- to quit): ')   # Prompt the user to enter a number or 'q' to quit
        
        if lt_numbers == 'q':
            break
        
        # Convert the user input to a float and add it to the list
        lt_numbers = float(lt_numbers)  
        list.append(lt_numbers)
        
        maxi = max(list)   # Find the maximum number in the list
    
        if lt_numbers <= list[-2]:  #checks if the current number entered by the user is less than or equal to the second-to-last number in the numbers list.
            print(f">>> The maximum number so far is: {maxi}")
        else:
            print(f">>> Now, The maximum number is: {maxi}")   
              
        print('All your numbers: ', list)    # Print all the numbers entered so far
    print(f"The final maximum number is: {maxi}")
    
             
if __name__=='__main__':    
    maximum() 
    
         
        
    
   