def swap1(a,b):
    print("Before Swapping : ",a,b)
    a=a+b
    b=a-b
    a=a-b
    print("After Swapping : ",a,b)
def swap2(a,b):
    print("Before Swapping :",a,b)
    a=a^b
    b=a^b
    a=a^b
    print("After Swapping :",a,b)

swap1(30,40)
swap2(30,40)
