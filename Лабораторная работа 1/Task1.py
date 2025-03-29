numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
len_ = len(numbers)
sum_ = sum(numbers[:4]) + sum(numbers[5:])
odd_elem = sum_ / len_
numbers[4] = odd_elem
print("Измененный список:", numbers)
