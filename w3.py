#!/usr/bin/python3
# #19
# d1 = {'a': 100, 'b': 200, 'c':300}
# d2 = {'a': 300, 'b': 200, 'd':400, 'e':500} 
# for key in d2:
#     if key in d1:
#         d1[key]+=d2[key]
#     else:
#         d1[key]=d2[key]
# print(d1)


# # #23
# data = [{'item': 'item1', 'amount': 400},
#         {'item': 'item2', 'amount': 300},
#         {'item': 'item1', 'amount': 750}]

# combined_data = {}
# for entry in data:
#     item = entry['item']
#     amount = entry['amount']
#     if item in combined_data:
#         combined_data[item] += amount
#     else:
#         combined_data[item] = amount

# print(combined_data)


#30
# data = {'item1': 45.50, 'item2': 35, 'item3': 41.30, 'item4': 55, 'item5': 24}
# top1, top2, top3 = None, None, None
# for item, price in data.items():
#     if top1 is None or price > data[top1]:
#         top3 = top2
#         top2 = top1
#         top1 = item
#     elif top2 is None or price > data[top2]:
#         top3 = top2
#         top2 = item
#     elif top3 is None or price > data[top3]:
#         top3 = item
# print("Top three items in the shop:")
# print(f"{top1}: {data[top1]}")
# print(f"{top2}: {data[top2]}")
# print(f"{top3}: {data[top3]}")

data = {'item1': 45.50, 'item2': 35, 'item3': 41.30, 'item4': 55, 'item5': 24}
sorted_data = sorted(data.items())
top_three = sorted_data[:3]

print("Top three items in the shop:" ,top_three)




