print("Calculator")
num1=float(input())
operator=input()
num2=float(input())

if operator == "+":
  print(num1+num2)
elif operator == "*":
  print(num1*num2)
elif operator == "/":
  print(num1/num2)
elif operator == "-":
  print(num1-num2)
else:
  print("Operater not found")
  =======
# This function adds two numbers
def add(x, y):
    return x + y

# This function subtracts two numbers
def subtract(x, y):
    return x - y

# This function multiplies two numbers
def multiply(x, y):
    return x * y

# This function divides two numbers
def divide(x, y):
    return x / y


print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    # Take input from the user
    choice = input("Enter choice(1/2/3/4): ")

    # Check if choice is one of the four options
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        break
    else:
        print("Invalid Input")

        
        #basic calculator
print("select operation")
print("1.add")
print("2.subtract")
print("3.multiply")
print("4.division")
choice=input("enter choice 1/2/3/4/: ")
number1=int(input("enter number 1: "))
number2=int(input("enter number 2: "))
if choice == "1":
    
   print(number1 + number2)
elif choice == "2":
    
   print(number1 - number2)
elif choice =="3":
    
   print(number1 * number2)
elif choice == "4":
    
   print(number1 / number2)
else:
    print("invalid")

        
