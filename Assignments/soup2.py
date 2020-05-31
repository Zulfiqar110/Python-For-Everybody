"""
This is without using contents function
"""

# import urllib.request, urllib.parse, urllib.error
# from bs4 import BeautifulSoup
# import re
# hand = urllib.request.urlopen('http://py4e-data.dr-chuck.net/comments_402689.html').read()
# soup = BeautifulSoup(hand,'html.parser')
# tags = soup('span')
# num_list = list()
# for data in tags:
#     num = re.findall(">([0-9]+)<", str(data))
#     num_list.append(int(num[0]))
# sum_num = 0
# for element in num_list:
#     sum_num = sum_num + element
# print(sum_num)
#
#
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import re
hand = urllib.request.urlopen('http://py4e-data.dr-chuck.net/comments_402689.html').read()
soup = BeautifulSoup(hand,'html.parser')
tags = soup('span')
num_list = list()
for data in tags:
    num = data.contents[0]
    num_list.append(int(num))
sum_num = 0
for element in num_list:    sum_num = sum_num + element
print(sum_num)
