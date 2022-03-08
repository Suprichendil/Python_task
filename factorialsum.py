##Write a Python function to calculate the factorial of a number (a non-negative integer). The function accepts the number as an argument
def fact(n):
    a=1
    if(n>0):
        for i in range(1,n+1):
            a=a*i
        return a
    print("The factorial of n is:",end="")
print(fact(4))

##EX-
##n=3
##a=1 (1,1)
##i=1*1=1
##a=2  (1,2)
##i=1*2=2
##a=3  (1,3)
##i=2*3=6
##a=4 (1,4)
##i=6*4=24
##        
        
