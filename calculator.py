print("=== Simple Calculator ===")
while True:
    a=float(input("Enter first number: "))
    b=float(input("Enter second number: "))
    print("\nChoose operation: ")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    choice=input("Enter choice (1/2/3/4): ")
    if choice== '1':
        result=a+b;
        print("Result is: ",result)
    elif choice== '2':
        result=a-b;
        print("Result is: ",result)
    elif choice== '3':
        result=a*b;
        print("Result is: ",result)
    elif choice== '4':
        if b!=0:
            result=a/b;
            print("Result is: ",result)
        else:
            print("Cannot divide by zero")
    else:
        print("Ivalid choice")
    again=input("\nDo you want to continue? (yes/no): ")
    if again.lower()!= 'yes':
        print("Calculator ended")
        break
        
