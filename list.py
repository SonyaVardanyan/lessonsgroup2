#!/usr/bin/python3
def longest_increasing_sublist(arr):
    if not arr:
        return []

    longest_sublist = [arr[0]]
    current_sublist = [arr[0]]

    for i in range(1, len(arr)):
        if arr[i] > arr[i - 1]:
            current_sublist.append(arr[i])
        else:
            current_sublist = [arr[i]]

        if len(current_sublist) > len(longest_sublist):
            longest_sublist = current_sublist

    return longest_sublist

# Example usage
input_list = [1, 3, 5, 2, 8, 4, 7, 9,10]
result = longest_increasing_sublist(input_list)
print("Longest increasing sublist:", result)
