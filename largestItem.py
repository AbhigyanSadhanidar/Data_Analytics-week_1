def findLargestItem(lst):
    if not lst:  
        return "The list is empty."
    return max(lst)

numbers = [3, 1, 45, 6, 90, 2]
print(f"The largest item in the list is: {findLargestItem(numbers)}")
