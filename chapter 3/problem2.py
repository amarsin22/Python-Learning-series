letter = '''Dear <|NAME|>,
You are selected!
Date: <|DATE|>'''
print(letter.replace("<|NAME|>","AMAR").replace("<|DATE|>","24th SEPTEMBER 2025"))

name = "Amar is a good boy and he is a talented boy"
print(name.find("goo"))
print(name.replace("good","bad"))
print(name) #String are immutable which means that you cannoit change the them by running functions on them