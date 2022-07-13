# i)convert to upppercase
my_string="hello world welcome to Python"
print(f"{my_string}".upper())

# ii)replace the word in a string
print(f"{my_string}".replace("Python","Python Programming"))

# iii) reverse the string and print it
print(f"{my_string}".replace("welcome",f"{my_string[18:11:-1]}"))

# iv)Reverse the entire string
print(f"Using Slicing : \n{my_string[::-1]}")
reverse = ''.join(reversed(my_string))
print(f"Without slicing : \n{reverse}")

# v)slice operation

lastindex=len(my_string)
print(f"{my_string[4:lastindex]}")

# vi) reverse the string 
reverse = my_string[:10:-1]
value_0 = reverse[0]
print(f"String in reverse :: {reverse}\n 0th value is {value_0}")

# vii)