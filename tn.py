#!/usr/bin/python3
#1 All countries,but 1 mistake

# import random;

# countries = {
#         "Armenia" : "Yerevan",
#         "France" : "Paris",
#         "China" : "Pekin",
#         "USA" : "Washington",
#         "Brazil" : "Brazil"
# }

# ml = list(countries.items())
# random.shuffle(ml)

# for el in ml:
#     print('WHat is the capital of %s' %el[0])
#     answer = input('Enter your answer: ')
#     if answer.lower() == el[1].lower():
#         print('correct')
#     else:
#         print('boom')
#         break

# #2. All countries,but 3 mistakes

# import random;
# countries = {
#         "Armenia" : "Yerevan",
#         "France" : "Paris",
#         "China" : "Pekin",
#         "USA" : "Washington",
#         "Brazil" : "Brazil"
# }
# ml = list(countries.items())
# random.shuffle(ml)
# count = 3
# for el in ml:
#     print('What is the capital of %s' % el[0])
#     if (count == 0):
#         print('Game over')
#         break
#     answer = input('Enter your answer: ')
#     if answer.lower() == el[1].lower():
#         print('Correct!')
#     else:
#         count -= 1
#         print('Incorrect.You have %d attend' %count)

# # All countries, but 1 mistake (with 10 seconds timer)
# import random
# import threading
# import time

# def get_user_input():
#     global answer
#     answer = input('Enter your answer: ')

# countries = {
#     "Armenia": "Yerevan",
#     "France": "Paris",
#     "China": "Pekin",
#     "USA": "Washington",
#     "Brazil": "Brazil"
# }

# ml = list(countries.items())
# random.shuffle(ml)

# for el in ml:
#     print('What is the capital of %s' % el[0])
#     answer = None

#     input_thread = threading.Thread(target=get_user_input)
#     input_thread.start()
#     input_thread.join(timeout=10)

#     if answer is None:
#         print('Time is up! Game over.')
#         break

#     if answer.lower() == el[1].lower():
#         print('Correct!')
#     else:
#         print('Boom')
#         break

