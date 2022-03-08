def palindrome(name):
    str=""
    for i in name:
        str=i+str
    return str
name=input("Enter a string to reverse ")
if(name == palindrome(name)):
    print("The given name {} is a palindrome".format(name))
else:
    print("The given name is not a palindrome")
