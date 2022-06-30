from collections import Counter

# The list of numbers
numberList = [99,86,87,88,111,86,103,87,94,78,77,85,86]

# Calculate the total count
count = len(numberList)

val = Counter(numberList)
findMode = dict(val)
mode = [i for i, v in findMode.items() if v == max(list(val.values()))]
if len(mode) == count:
    findMode = "The group of number do not have any mode"
else:
    findMode = "The mode of a number is / are: " + ', '.join(map(str, mode))

# Print Results
print(findMode)