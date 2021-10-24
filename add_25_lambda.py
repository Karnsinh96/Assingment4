'''def add_25(num):
    a=num+25
    return a
num=int(input("Enter the Number:- "))
b=add_25(num)
print(b)'''

add_25= lambda x:x+25
num=int(input("Enter the Number:- "))
print(add_25(num))