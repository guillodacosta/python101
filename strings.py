parrot = "Norwegian Blux"
print('strings separated by "commas", "spaces" or "+"', ' on print are concatenated', '\'string x\',', 234)
print('we can tab characters with \\t ' + 'tabbing 1\t 2 \t3')
print("""many lines could be written within \"\"\" 
asfdjar = open(os \
we can do new lines by \\
new line example
""")
print("Norwegian " * 4)
print(parrot)
print(parrot[0])
print(parrot[1])
print(parrot[11])
print(parrot[-1])
print(parrot[-2])
print(parrot[-9])
print('slice parrot[5:9] -> gian, ', parrot[5:9])
print('slice parrot[0:9] -> Norwe, ', parrot[0:6])
print('slice parrot[:4] -> Norw, ', parrot[:4])
print('slice parrot[11:] -> lux, ', parrot[11:])
print('slice parrot[:] -> Norwegian Blux, ', parrot[:])
print('third param is used for step "hola slice"[0:9:2]', "hola slice"[0:9:2])
print('backward the text print(backward)[::-1]', 'backward'[::-1])

print('to find a string inside other the in world, ex "ho" in "hola"', "ho" in "hola")
age = 30
print('I am {{0}}<-param {0} years old'.format(age))
print('I can repeat the {{0}} {{0}}<-param {0} {0} many times I want'.format(age))
print('or use N params {{0}}  {{1}}<-params {0} {1} '.format(age, 3))