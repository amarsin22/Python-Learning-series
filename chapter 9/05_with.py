f = open("myfile.txt")
print(f.read())
f.close()
  # the same can be written using with statement like this
with open('example.txt', 'w') as file:
    print(file.read())
    
# you don't need to explicitly close the file, it will be closed automatically when the block is exited.