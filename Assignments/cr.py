name = input("Enter file:")
if len(name) < 3 : name = "asd.txt"
handle = open(name)
dc = {"Jan":1,"Feb":2,"Mar":3,"Apr":4}
for lines in handle:
    if lines.startswith("From "):
        words = lines.split()
        email,day,month,date,year = words[1], words[2], words[3], words[4], words[6]
        mn = dc.get(month,"Zam")
        print(f'{email} :: {date}/{mn}/{year}, {day}')



