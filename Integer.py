print('Int has not limits')
print('Since Python 3 Long and Int are used as int')
first_int = 12
second_int = 3

print(first_int + second_int)   # 15 addition
print(first_int - second_int)   # 9 subtraction
print(first_int * second_int)   # 36 multiplication
print(first_int / second_int)   # 4.0 division
print(type(first_int / second_int))   # class 'float'
print('the normal / return in float values')
print(first_int // second_int)  # 4 int division
print(type(first_int // second_int))   # class 'int'
print(first_int % second_int)   # modulus operation
print('--')
for range_val in range(1, first_int // second_int):
    print(range_val)
print('--')
print('Precedence for operators is \n 1. parentheses, \n 2. multiplication and division \n 3. addition and subtraction')
print('4 * 3 / 3 + 1 = 5.0, test', 4 * 3 / 3 + 1)
print('4 / 2 * 3 + 1 = 7.0, test', 4 / 2 * 3 + 1)