def plus_num(a,b):
    sum = a + b
    print("Answer is", sum)
    

def min_num(a,b):
    sum = a - b
    print("Answer is", sum)

def mul_num(a,b):
    sum = a * b
    print("Answer is", sum)
    
def div_num(a,b):
    sum = a / b
    print("Answer is", sum)
    
action = input("Enter the action :")
a = int(input("Enter the first number :"))
b = int(input("Enter the second number :"))

if action == "+":
    print(plus_num(a,b))
elif action == "-":
    print( min_num(a,b))
elif action == "*":
    print(mul_num(a,b))
elif action == "/":
    print(div_num(a,b))

if b == "0":
    print("Game over")
elif a == "0":
    print("Game over")
