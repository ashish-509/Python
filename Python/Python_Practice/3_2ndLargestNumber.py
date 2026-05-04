# Given a list of integers, return:
    # second largest number
    # without using built-in sort


def second_largest (nums):

    if len(nums)<2:
        return None

    largest = nums[0]
    second = None

    for i in range(1, len(nums)):
        if nums[i] > largest:
            second = largest
            largest = nums[i]
        elif second is None or nums[i] > second:
            second = nums[i]

    return second

# Test Cases
print(second_largest([1, 2, 3, 4, 5]))
print(second_largest([5, 4, 3, 2, 1]))
print(second_largest([1, 1, 1, 1, 1]))
print(second_largest([1]))
print(second_largest([]))   