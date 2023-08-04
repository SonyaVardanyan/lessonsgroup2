#!/usr/bin/python3
# #1
# a = "hello world"
# b = 'k'

# c = ""
# for el in a:
#     if el== 'l':
#         c+= b
#     else:
#         c += el

# print(c)


# #2
# string = input("Enter a string: ")
# w= string.split()
# a = [''.join(sorted(word)) for word in w]
# b= ' '.join(a)

# print(b)

# #3
# num_count = 6
# max_sum = 0    
# result_num = 0 
# for _ in range(num_count):
#     num = int(input("Enter a number: "))
#     sum_of_digits = 0
#     num_str = str(num)
#     for d in num_str:
#         sum_of_digits += int(d)
    
#     if sum_of_digits > max_sum:
#         max_sum = sum_of_digits
#         result_num = num
# print(result_num)




# #4
# def filter_pairs(input_dict):
#     string_pairs = {}

#     for key, value in input_dict.items():
#         if isinstance(key, str) and isinstance(value, str):
#             string_pairs[key] = value

#     return string_pairs

# data = {
#     "name": "Ani",
#     "age": 30,
#     "city": "Gyumri",
    
# }

# result = filter_pairs(data)
# print(result)
