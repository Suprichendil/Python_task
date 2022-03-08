def pangram(n):
    x="abcdefghijklmnopqrstuvwxyz"
    for i in x:
        if i in n:
            return True
        return False

n=input("enter the n")
if(pangram(n)==True):
    print("is a pangram")
else:
    print("is not a pangram")

