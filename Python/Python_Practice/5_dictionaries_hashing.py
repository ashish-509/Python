# Given an array, find all elements that appear more than ⌊n/3⌋ times.


def majorityElements(elements):
    count = {}
    result = []
    n = len(elements)

    for element in elements:
        if element in count:
            count[element] += 1
        else:
            count[element] = 1

    for element, frequency in count.items():
        if frequency > n // 3:
            result.append(element)

    return result


# Example usage:# Example usage:

input_array = input("Enter an array of integers (comma-separated): ")
input_array = [int(x.strip()) for x in input_array.split(",")]
result = majorityElements(input_array)  

if result:
    print(f"Elements that appear more than ⌊n/3⌋ times: {result}")
else:
    print("No elements appear more than ⌊n/3⌋ times.")

