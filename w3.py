#!/usr/bin/python3
# #19
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400, 'e':500} 
for key in d2:
    if key in d1:
        d1[key]+=d2[key]
    else:
        d1[key]=d2[key]
print(d1)


#23
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