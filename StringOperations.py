#Taking user input
a=input()

#Displaying character at 3rd position
print("Character at 3rd position",a[2])

#Displaying character at 4th position 
print("Character at 4th position",a[3])

#Displaying characters at 3rd and 4th position together   
print(a[2:4])

print("6th position onwards along with next two characters",a[5:8])

#Displaying length of the string
print(len(a))

#Removing extra spaces on left side of the string
a=a.lstrip()
#Removing extra spaces on right side of the string
a=a.rstrip()

print(a)

#Replacing character at 5th position of the string
a=a[:4]+'p'+a[5:]
print(a)

#Converting the string to all lower case
a=a.lower()
print(a)