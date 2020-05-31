import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
f = 'https://www.flipkart.com/beerock-oxygen-running-shoes-men/p/itmfhgh9snhtrjae?pid=SHOEGWUDHHGQZTGM&lid=LSTSHOEGWUDHHGQZTGM2K1BGB&marketplace=FLIPKART&srno=b_1_5&otracker=nmenu_sub_Men_0_Sports%20Shoes&fm=organic&iid=21473891-8453-44f6-bfa5-01604504ffcd.SHOEGWUDHHGQZTGM.SEARCH&ppt=browse&ppn=browse&ssid=c9kbqf68280000001586093793776'
url = 'https://www.flipkart.com/redmi-k20-pro-glacier-blue-128-gb/p/itmfgfjthe3dyjp3'
hand = urllib.request.urlopen(url,None).read().decode()
soup = BeautifulSoup(hand,'html.parser')

price = soup.find('div',class_='_1vC4OE _3qQ9m1').text
product_name = soup.find('span',class_='_35KyD6').text
print(product_name,'\n',price)
#<h1 class="_9E25nV"><span class="_35KyD6">Apple iPhone 8 Plus (Space Grey, 256 GB)</span></h1>
#<div class="_1vC4OE _3qQ9m1">₹8,999</div>'

