name = input('write your name')
print(f'name count{len(name)}')
while len(name) == 0:
    name = input('your name is:')
if name == 'Pablo':
    print('we\'ll need to review your bags')
elif name == 'Maria':
    print('please show us your passport')
else:
    print('go ahead')