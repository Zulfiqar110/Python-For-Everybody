import xml.etree.ElementTree as e
data = """<frnds>
<frnd>
  <f x='1'>
   <name>"Vasim"</name>
   <id type='intl'>12</id>
  </f>
  <f x='2'>
   <name>"Aman"</name>
   <id type='intl'>10</id>
  </f>
  <f x='3'>
   <name>"Kat"</name>
   <id type='intl'>1</id>
  </f>
</frnd>
</frnds> """

tree = e.fromstring(data)
frnd_list = tree.findall("frnd/f")
for item in frnd_list:
    frnd = item.find("name").text
    id = item.find("id").text
    num = item.get("x")
    print(f"Friend : {frnd} \nID : {id}\nX : {num}\n")