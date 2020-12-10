first_num = float(input('Enter first number: '))
operator = input('Enter operator: ')
second_num = float(input('Enter second number: '))


if operator == '+':
   print(first_num + second_num)
elif operator == '-':
     print(first_num - second_num)
elif operator == '*':
     print(first_num * second_num)
elif operator == '/':
     print(first_num / second_num)
elif operator == '+':
     print(first_num + second_num)
else:
     print("Invalid operator")	 


quit = input("Press 'q' to exit")

if quit == 'q':
   quit()	
