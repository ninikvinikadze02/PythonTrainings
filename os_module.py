import os

# if os.path.exists('main1.py'):
#     os.rename('main1.py', 'main.py')
#
# if os.path.exists('monacemebi.txt'):
#     os.remove('data.txt')

# os.rename('main1.py', 'main.py')


# try:
#     num_one = int(input("Enter a number: "))
#     num_two = int(input("Enter a number: "))
#     print(num_one / num_two)
# except ZeroDivisionError as e:
#     print(e)


try:
    age = int(input("Enter age: "))
    if age < 18: raise Exception("Age must be greater than 18")
except:
    print("Invalid age")
