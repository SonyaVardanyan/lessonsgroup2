#!/usr/bin/python3
# #1
# def sum_of_numbers(*args):
#     msum = 0
#     for num in args:
#         msum += num
#     return msum
# result = sum_of_numbers(10, 20, 30, 40)
# print(result)

# #2
# def count_rows(*args):
#     return len(args)

# a= count_rows([1, 2, 3], ['a', 'b'], [True, False, True, False])
# print(a)

# #3
# def a(*args):
#     if not args:
#         return None
#     return sum(args) / len(args)
# b = a(10, 20, 30, 40, 50)
# print(b)

# #4
# def math_operations(a, b):
#     gumar= a + b
#     tarb = a - b
#     art = a * b
#     qanord = a / b 
#     return gumar, tarb, art, qanord

# result = math_operations(10, 5)
# print("Gumar:", result[0])         
# print("Tarberutyun:", result[1])      
# print("Artadryal:", result[2])   
# print("Qanord:", result[3])      

# #5
# def my_upper(input_string):
#     a= ""
#     for char in input_string:
#         if 'a' <= char <= 'z':
#             mec = chr(ord(char) - 32)
#         else:
#             mec = char
#         a += mec
#     return a

# result = my_upper("Hello, World!")
# print(result) 

# #6
# def my_lower(input_string):
#     a = ""
#     for char in input_string:
#         if 'A' <= char <= 'Z':
#             poqr = chr(ord(char) + 32)
#         else:
#             poqr = char
#         a+= poqr
#     return a

# result = my_lower("Hello, World!")
# print(result)  

# #7
# def my_title(input_string):
#     a= ""
#     words = input_string.split()
#     for word in words:
#         if word:
#             a += word[0].upper() + word[1:] + " "
#     return a 

# result = my_title("hello world, how are you?")
# print(result)  

# #8
# def reverse_string(input_string):
#     return input_string[::-1]

# result = reverse_string("hello world")
# print(result)  

# #9
# def ml(input_string, start_index, end_index):
#     return input_string[start_index:end_index]

# result = ml("Hello, World!", 7, 12)
# print(result)  

# #10
# def longest_word(sentence):
#     words = sentence.split()
#     longest = ""
#     for el in words:
#         if len(el) > len(longest):
#             longest = el
#     return longest

# result = longest_word("hello good worldde")
# print(result)  

#11
#12
# #13
# def my_index(input_string, index):
#     return input_string[index:]

# result = my_index("Hello, World!", 4)
# print(result) 

# #15
# def is_palindrome(number):
#     a = str(number)
#     return a == a[::-1]

# result1 = is_palindrome(1213)
# print(result1)

# #16?
# def is_palindrome(number):
#     num_str = str(number)
#     return num_str == num_str[::-1]

# def closest_palindrome(number):
#     if number < 0:
#         return None  

#     lower = number - 1
#     upper = number + 1

#     while True:
#         if is_palindrome(lower):
#             return lower
#         elif is_palindrome(upper):
#             return upper

#         lower -= 1
#         upper += 1


# result1 = closest_palindrome(123595858)
# print(result1)  

# #17
# def ml(number):
#     num_str = str(number)
#     first_digit = int(num_str[0])
#     last_digit = int(num_str[-1])
#     return first_digit * last_digit

# result = ml(12345)
# print(result) 

# #18
# def number_of_rows(list):
#     return len(list)

# list= [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# result = number_of_rows(list)
# print(result)  

# #19
# def max_number(list):
#     return max(list)

# numbers = [10, 5, 20, 15, 25]
# result = max_number(numbers)
# print(result) 

# #20
# def even_numbers(numbers_list):
#     return [num for num in numbers_list if 10 <= num <= 99 and num % 2 == 0]

# numbers = [15, 28, 37, 46, 99, 64]
# result = even_numbers(numbers)
# print(result)

# #21
# def mij_tv(numbers_list):
#     if not numbers_list:
#         return None

#     a = sum(numbers_list)
#     b = a / len(numbers_list)
#     return b

# numbers = [10, 20, 30, 40, 50]
# result = mij_tv(numbers)
# print(result)  

# #22
# def string_lengths(strings_list):
#     return [len(string) for string in strings_list]

# strings = ["apple", "banana", "orange", "grapefruit"]
# result = string_lengths(strings)
# print(result)  

# #23
# def descending_order(numbers_list):
#     return sorted(numbers_list, reverse=True)

# numbers = [10, 5, 20, 15, 25]
# result = descending_order(numbers)
# print(result) 

# #24
# def ml(lines_list):
#     return sorted(lines_list, key=len, reverse=True)

# lines = ["apple", "banana", "orange", "grapefruit"]
# result = ml(lines)
# print(result)  

#25
#26
#27

# #28
# def ml(person):
#     return person.get('age', 0)

# def max_age(people_list):
#     if not people_list:
#         return None

#     a= max(people_list, key=ml)
#     return a

# people = [
#     {"name": "Ani", "age": 25},
#     {"name": "Armen", "age": 30},
#     {"name": "Mane", "age": 20},
#     {"name": "David", "age": 35}
# ]
# result = max_age(people)
# print(result)  

# #29
# def ml(students_list):
#     return sorted(students_list, key=lambda student: student['units'])

# students = [
#     {"name": "Ani", "units": 10},
#     {"name": "Armen", "units": 7},
#     {"name": "Mane", "units": 12},
#     {"name": "David", "units": 5}
# ]
# sorted_students = ml(students)
# print(sorted_students)

#30



   

