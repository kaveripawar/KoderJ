a=int(input("enter the first number"))
b=int(input("enter the second number"))
def calculator(a,b):
    if(a>=0 and b>=0):
        print("add",a+b)
        print("\n sub",a-b)
        print("\n mul",a*b)
        print("\n div",a/b)
print(calculator(a,b))
