List_ = sorted(list(map(int, input("Enter numbers divided by space:").split())))
Number_ = int(input("Enter any number: "))


def binary_search(array, element, left, right):
    if left > right:
        return False

    middle = (right + left) // 2  # searching middle
    if array[middle] == element:  # if element is equal middle
        return middle
    elif element < array[middle]:  # searching in left half
        return binary_search(array, element, left, middle - 1)
    else:  # searching in right half
        return binary_search(array, element, middle + 1, right)


print("Your sorted entry: ", List_)
print("Your Number: ", Number_)
number_index = binary_search(List_, Number_, 0, len(List_) - 1)

if isinstance(number_index, bool):
    print(f"Your Number {Number_} is not in List")
else:
    print("Your number index in list:", number_index)
