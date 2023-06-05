
def fibonacci(n):

    fn = [0,1]
   
    for i in range(2,n):
        next_n = fn[i-1] + fn[i-2]
        fn.append(next_n)
    print(fn)
    
if __name__=='__main__':
   fibonacci(10)
           
    