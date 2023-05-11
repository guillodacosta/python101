first_string = 'he-s'
second_string = 'probably '
third_string = 'pining'
# because string is a sequence of characters I can do below thing
print("strings are operables ex he-s * 4 -> he-she-she-she-s", (first_string * 4))

for i in range(2, 10, 4):
    print(i)
print('------')
for i in range(2, 6):
    print(i)
print("we can add width to value by second param on {{}}, ej No. {{0:2}} means param 0 with 2 of width")
for i in range(1, 6):
    print("No. without spaces {0} is diff to No. {0:2}".format(i))
print('For floating numbers applies something similar, second position width, third position if there are 3 float')
print("Pi is approx {0}".format(22 / 7))
print('{{0:12}}', "Pi is approx {0:2f}".format(22 / 7))
print('%% D and S work for params too %d %s' % (4, 'string'))
param = 'value_x_from_memory'
print(f'the same with f\"strings\" {param} ')
print('Mon, Tue, Wed, Thu, Fri, Sat, Sun'[::5])
