def add (x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide (x, y):
    if y == 0 :
      return "Error: Division by zero"
    
    return x / y

def main():

    print("Welcome To TG's Simple Calculator App")
    print("--------------------------------------")
    
    print("Select An Operation:")
    
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    
    choice = input("Enter Choice (1/2/3/4) :")
    
    if choice == '1':
        num1 = float(input("Enter First Number: "))
        num2 = float (input("Enter Second Number: "))
        print(num1, "+", num2, "=", add(num1, num2))
        
    elif choice == '2' :
        num1 = float(input("Enter First Number:")) 
        num2 = float (input("Enter Second Number: "))
        print(num1, "-", num2, "=", subtract(num1, num2))   
    
    elif choice == '3':
        num1 = float(input("Enter First Number: "))
        num2 = float (input("Enter Second Number: "))
        print(num1, "*", num2, "=", multiply(num1, num2))
    
    elif choice  == '4':
        num1 = float(input("Enter First Number: "))
        num2 = float (input("Enter Second Number: "))
        print(num1, "/", num2, "=", divide(num1, num2)) 
        
    else:
        print("Invalid Input") 
        
    if break_calculation := input("Do You Want To Perform Another Calculation? (yes/no): ").lower() == 'yes':
        main()