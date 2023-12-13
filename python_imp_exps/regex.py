import re
with open("abc.txt", mode="r") as file:
    text = file.read()
    pattern = r"M(?:r|rs|s)\. [a-zA-z]+"

    names = re.findall(pattern, text)
    print(names)

    pattern = r"[a-zA-z0-9]+(?:(?:\.[a-zA-z0-9])|[a-zA-z0-9])+\@[a-zA-Z]+\.[a-z]+"
    emails = re.findall(pattern, text)
    print(emails)

    pattern =r"[0-9]{,10}"
    number = re.findall(pattern, text)
    print([string for string in number if string != ''])

    # pattern = r"(?:(?:https?)://+(?:www\.)+[a-zA-Z0-9._-]+\.+[a-z]+)|(?:www\.)+[a-zA-Z0-9._-]+\.+[a-z]+"
    pattern = r"(?:(?:https?)://+(?:www\.)+[a-z0-9A-Z.-_]+\.+[a-z]+)|(?:www\.)+[a-z0-9A-Z.-_]+\.+[a-z]+"
    sites = re.findall(pattern,text)
    print(sites)









# pattern = r'M(?:r|rs|s)\. [a-zA-Z]+' #?: batata hai ki voh bracket ke andar jo hai voh saath mein hi aane chaiye as a grp
# names = re.findall(pattern,text)
# print(names)
# pattern=r'[a-zA-Z0-9]+\.[a-zA-Z]+\@[a-zA-Z]+\.[a-zA-Z]{2,}' #+ tabhi use karte jab uske pehle compulsory chaiye hi chaiye
# emails= re.findall(pattern,text)
# print(emails)
# pattern=r'^\d{,10}$' #sirf sidha sidha 10 digit hoga line pe toh bataaega
# mobile=[line for line in text.split('\n') if re.match(pattern,line)]
# print(mobile)
# pat = r'^((?:(?:https?):\/\/)|(?:www\.))?[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$' #^ start of line and $ end of line pe use karte
# matching_lines = [line for line in text.split('\n') if re.match(pat, line)]
# print(matching_lines)