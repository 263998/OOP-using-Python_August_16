import re
'''def isAlphaNumericStr(text):
   if(re.match("^[a-zA-Z0-9]*$", text) != None):
     return True
   return False
fname = input("Enter file name: ")
userinput = input("what you want to search")
with open(fname, 'r', encoding="utf8") as f:
    for line in f:
        words = line.split()
        for i in words:
            for userinput in i:
                if(isAlphaNumericStr(userinput)):
                    print("userinput found")'''
#fname = 'test.txt'
with open('test.txt', 'r', encoding="utf8") as f:
    text_to_search = f.read()
#usrip = input("enter to serch")
pattern = re.compile(r'Patna')
matches = pattern.finditer(text_to_search)

for match in matches:
    print(match)