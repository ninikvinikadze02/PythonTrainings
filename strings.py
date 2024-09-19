name = input("Enter your name: ")
age = input("Enter your age: ")

text = "Hello, {0} Your age is {1}. Bye {0}".format(name, age)
text_one = f"Hello, {name} Your age is {age}. Bye {name}"

print(text_one)
