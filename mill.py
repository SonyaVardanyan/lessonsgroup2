#!/usr/bin/python3
file=open('questions.txt', 'w')
file.write('What is the capital of France?Paris,Yerevan,Berlin,Moscow'"\n")
file.write("What is the capital of Armenia?Yerevan,Paris,Berlin,Moscow""\n"),
file.write   ("What is the capital of Germany?Berlin,Yerevan,Paris,Moscow""\n"),
file.write   ("What is the capital of Spain?Madrid,Yerevan,Berlin,Moscow""\n")
file.write  ( "What is the capital of Portugal?Lisbon,Yerevan,Berlin,Moscow""\n"),
file.write   ("What is the capital of Georgia?Tbilisi,Yerevan,Berlin,Moscow""\n"),
file.write   ("What is the capital of Belarus?Minsk,Yerevan,Berlin,Moscow""\n"),
file.write   ("What is the capital of Ukrain?Kiev,Yerevan,Berlin,Moscow""\n"),
file.write   ("What is the capital of Norway?Oslo,Yerevan,Berlin,Moscow""\n"),
file.write   ("What is the capital of Australia?Canberra,Yerevan,Berlin,Moscow""\n"),
file.write   ("What is the capital of Japan?Tokio,Yerevan,Berlin,Moscow""\n"),
file.write   ("What is the capital of China?Beijing,Yerevan,Berlin,Moscow""\n"),
file.write   ("What is the capital of USA?Washington,Yerevan,Berlin,Moscow""\n"),
file.write   ("What is the capital of Canada?Ottawa,Yerevan,Berlin,Moscow""\n")
file.close()

import random


questions = [
    "What is the capital of France?Paris,Yerevan,Berlin,Moscow",
   "What is the capital of Armenia?Yerevan,Paris,Berlin,Moscow",
   "What is the capital of Germany?Berlin,Yerevan,Paris,Moscow",
   "What is the capital of Spain?Madrid,Yerevan,Berlin,Moscow",
   "What is the capital of Portugal?Lisbon,Yerevan,Berlin,Moscow",
   "What is the capital of Georgia?Tbilisi,Yerevan,Berlin,Moscow",
   "What is the capital of Belarus?Minsk,Yerevan,Berlin,Moscow",
   "What is the capital of Ukrain?Kiev,Yerevan,Berlin,Moscow",
   "What is the capital of Norway?Oslo,Yerevan,Berlin,Moscow",
   "What is the capital of Australia?Canberra,Yerevan,Berlin,Moscow",
   "What is the capital of Japan?Tokio,Yerevan,Berlin,Moscow",
   "What is the capital of China?Beijing,Yerevan,Berlin,Moscow",
   "What is the capital of USA?Washington,Yerevan,Berlin,Moscow",
   "What is the capital of Canada?Ottawa,Yerevan,Berlin,Moscow"
]

with open("questions.txt", "w") as file:
    for question in questions:
        file.write(question + "\n")


game_questions = []
with open("questions.txt", "r") as file:
    game_questions = file.read().splitlines()

gquestions = {}
for el in game_questions:
    q, a = el.split("?")
    gquestions[q] = a.split(",")


user_name = input("Please enter your username: ")

top_players = {}
try:
    with open("top_players.txt", "r") as file:
        for line in file:
            name, score = line.strip().split(":")
            top_players[name] = int(score)
except FileNotFoundError:
    pass


if user_name in top_players:
    choice = input("Username already exists. Do you want to continue and update your score? (yes/no): ")
    if choice.lower() == "no":
        user_name = input("Please choose another username: ")
        top_players[user_name] = 0

cnt = 0
variant = ["A", "B", "C", "D"]
cvariant = ""

for q, a in gquestions.items():
    print(q)
    correct = a[0]
    random.shuffle(a)
    for i in range(len(variant)):
        print(variant[i], a[i])
        if a[i] == correct:
            cvariant = variant[i]
    answer = input("Your variant: ")
    if answer.upper() == cvariant:
        cnt += 1
        print("Correct.")
    else:
        print("Not. Correct answer was:", correct)


if user_name in top_players:
    top_players[user_name] = max(top_players[user_name], cnt)
else:
    top_players[user_name] = cnt


sorted_players = sorted(top_players.items(), key=lambda x: x[1], reverse=True)
with open("top_players.txt", "w") as file:
    for name, score in sorted_players:
        file.write(f"{name}:{score}\n")

print("You got %d/10" % cnt)