import pyperclip
print("hello")  # This will print "hello" directly.
CO = input("Enter something: ")  # Changed prompt for clarity.
pyperclip.copy(CO)
pasty = pyperclip.paste() + "hello"
print(pasty)