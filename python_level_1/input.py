name = input("Enter Name: ")
grade = input("Enter Grade: ")
company = input("Enter Company Name: ")

print(name, grade, company)
print()
number = input("Enter Number: ")
name = input("Enter Name: ")

print("type of number", type(number),number * 3)
print("type of name", type(name))
print()

first_number = int(input("Enter number1 : "))
second_number = int(input("Enter number2 :"))

total = first_number + second_number
print("first_number + second_number : ", total)
print()

float_number = float(input("Enter a float number: "))
print("input float: ", float_number)
print("input type: ", type(float_number))
print()

print("FirstName - {0}, LastName - {1}".format(input("Enter first name: "), input("Enter second name: ")))