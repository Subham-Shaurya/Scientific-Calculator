print("----------------------Scientific Calculator----------------------\n")
print('''Operators
"+" = add
"-" = substract
"*" = multiply
"/" = divide
"**"= exponential
"%"= remainder
"sqrt" = square root of any number\n

---Trigonometric function---
"sin" = sine of angle
"cos" = cosine of angle
"cosec" = cosec of angle
"rad" = degree to radian
"deg" = radian to degree \n''')
import math
while True:
    opr = input("Enter Operator: ")
    o ="+-*/%**"
    t = ["sin","cos","cosec","sec","tan","cot"]
    if opr in o:
        num = eval(input("Enter num 1:"))
        num_ = eval(input("Enter num 2:"))
        if opr=="+":
            print(num + num_)
        elif opr == "-":
            print(num-num_)
        elif opr == "*":
            print(num*num_)
        elif opr=="/":
            print(num/num_)
        elif opr=="%":
            print(num%num_)
        elif opr=="**":
            print(num**num_)
        #else:
            #print("Invalid input")
    elif opr in t:
        print("Values in Degree")
        num1= eval(input("Enter number:"))
        if opr=="sin":
            print(math.sin(math.radians(num1)))
        elif opr=="cos":
            print(math.cos(math.radians(num1)))
        elif opr=="cosec":
            print(1/math.sin(math.radians(num1)))
        elif opr=="sec":
            print(1/math.cos(math.radians(num1)))
        elif opr=="tan":
            print(math.tan(math.radians(num1)))
        elif opr=="cot":
            print(1/math.tan(math.radians(num1)))
        #else:
         #   print("Invalid Operator")
    elif opr=="rad":
        num1 = eval(input("Enter number: "))
        print(math.radians(num1))
    elif opr=="deg":
        num1 = eval(input("Enter number: "))
        print(math.degrees(num1))
    elif opr=="sqrt":
        num1=eval(input("Enter number: "))
        print(math.sqrt(num1))
    elif opr=="exit":
        break
    else:
        print("Invalid Operator")
print("\nThankYou")
