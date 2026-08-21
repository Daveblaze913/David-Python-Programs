name = input("Enter your name: ")

revStr = ""

for i in name:
    revStr = i + revStr
print("Original string : ",name )
print("Reverse string: ", revStr)