first_input = int(input("Enter your first number:"))
second_input = int(input("Enter your second number: "))
result = first_input * second_input

print(f"{first_input} * {second_input} = {result}")

if result < 0 :
    print("The result is negative")
elif result > 0 :
    print ("The result is positive")
elif result == 0 :
    print ("The result is positive and negative")