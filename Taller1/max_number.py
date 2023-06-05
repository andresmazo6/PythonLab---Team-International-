def maximum():
    list = [0]
    
    while True:
        lt_numbers = input('"Hello! Please enter a number (or -q- to quit): ')
        
        if lt_numbers == 'q':
            break
        lt_numbers = float(lt_numbers)
        list.append(lt_numbers)
        maxi = max(list)   
    
        if lt_numbers <= list[-2]:
            print(f">>> The maximum number so far is: {maxi}")
        else:
            print(f">>> Now, The maximum number is: {maxi}")     
        print('All your numbers: ', list)    
    print(f"The final maximum number is: {maxi}")
    
             
if __name__=='__main__':    
    maximum() 
    
         
        
    
   