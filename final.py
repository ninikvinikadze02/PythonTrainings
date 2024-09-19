# # 1.
#
# def function_1(ideal_number):
#     dividers_1 = [i for i in range(1, ideal_number) if ideal_number % i == 0]
#     if sum(dividers_1) == ideal_number and ideal_number > 1:
#         return True
#     else:
#         return False
#
#
# input_number = int(input("enter a number: "))
# result = function_1(input_number)
# print(result)  # აქ გავიჭედე ეს result მიემართება return True-ს დააბრუნებს ფუნქცია თუ False-ს ხო (ანუ if-else-ის ტანში რაც მიწერია მაგას)?
#
# if result is True:
#     with open("Data.txt", "w") as f:
#         content = f.write(str(input_number))

# 2.
#
# try:
#     list_1 = [5, 78, 45, 7, 12, 18, 15]
#     list_2 = [4, 54, 23, 14, 534, 10, 19]
#     list_3 = []
#
#     for i in range(
#             len(list_1)):  # აქ ეს რეინჯი რომ მიმეთითებინა ვერ ვხვდებოდი და ჩატჯიპიტი დამეხმარა. ვცდილობდი,
#         # ეგრევე კონკრეტული ინდექსებით მივწვდომოდი ლისთების ელემენტებს.
#         if i % 2 == 0:
#             list_3.append(list_1[i])
#         else:
#             list_3.append(list_2[i])
#
#     str_list_3 = [str(n) for n in list_3]
#     result_str = ', '.join(str_list_3)
#     print(result_str)
#
#     with open('Data.txt', 'w') as f:
#         content = f.write(result_str)
#         print(content)
# except IndexError as msg1:
#     print(msg1)
# except IndentationError as msg2:
#     print(msg2)
# except Exception as msg3:
#     print("An error occurred")  # სხვა ერორები თუა საჭრო? ან ესენი სწორია?
