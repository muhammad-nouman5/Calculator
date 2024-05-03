while True:
    print(
        '''
    + Addition
    - Subtraction
    * Multiplication
    / Division
        '''
        )
    num1 = float(input("Enter Number 1 :- "))
    num2 = float(input("Enter Number 2 :- "))
    opr = input("Enter Operator +,-,*,/ :- ")

    if opr=="+":
        add = num1 + num2
        print("Result of Addition :-", add)
    elif opr=="-":
        sub = num1 - num2
        print("Result of Subtraction :- ", sub)
    elif opr=="*":
        mul = num1 * num2
        print("Result of Multiplication :- ", mul)
    elif opr=="/":
        div = num1 / num2
        print("Result of Division :- ", div)
    else:
        print("Enter Wrong Information")
