import re
name = input("Enter file name :")
if len(name) < 3 :  name = "regex_sum_402687.txt"
handle = open(name)
num_list = list()
for lines in handle:
    num = re.findall("([0-9]+)",lines)
    for i in num:
        num_list.append(int(i))
_sum = 0
for j in num_list : _sum = _sum + j
print(_sum)


# import re
# a = "The Quick brow : 745 fox jumps: 34 56  234 over a lazy dog"
# y = re.findall("([0-9]+)",a)
# print(y)