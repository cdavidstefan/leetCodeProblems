# Fiind dat un array de numere intregi, si un numar intreg ca si target.
# Sa se returneze index-urile a doua numere din array, care adunate sunt egame cu target-ul
# Se presupune ca fiecare input are exact o solutie si nu se poate utiliza acelasi element
# de doua ori
# ex1: Input: nums = [2,7,11,15], target = 9 -> Output: [0,1]
# ex2: Input: nums = [3,2,4], target = 6 -> Output: [1,2]
# ex3: Input: nums = [3,3], target = 6 -> Output: [0,1]

# First approach O(n^2):
def two_sum(arr, target):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == target and i != j:
                return i, j


output = two_sum([2, 7, 11, 15], 17)
print(output)

# Second approach (for sorted arrays):
# if the array is sorted, the largest sum possible is for the last two items


def two_sum_2(arr, target):
    low = 0
    high = len(arr) - 1

    while low < high:
        s = arr[low] + arr[high]
        if s == target:
            return low, high
        elif arr[low] + arr[high] < target:
            low += 1
        else:
            high -= 1

    return low, high


output_2 = two_sum_2([2, 3, 4], 6)
print(output_2)

# Third approach (not sorted arrays): fastest approach
# using the complement variable


def two_sum_3(arr, target):
    complements_list = {}

    for i in range(len(arr)):
        complement = target - arr[i]

        if arr[i] in complements_list:
            return complements_list[arr[i]], i

        complements_list[complement] = i

    return None


output_3 = two_sum_3([1, 2, 4, 9, 18], 27)
print(output_3)
