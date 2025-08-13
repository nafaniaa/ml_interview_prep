#11
# squares = [x**2 for x in range(1,6)]
# print(squares)

#12

# def reverse_list(lst):
#     lst.reverse()
#     return lst

# print(reverse_list([1, 2, 3]))

# альтерннатива 12
# def reverse_list(lst):
#     return lst[::-1]

# print(reverse_list([1, 2, 3]))

#13
# numbers = [10, 20, 30]
# print(sum(numbers))

#14
# numbers = [1, -2, 3, -4, 5]
# new = []
# for num in numbers:
#     if num > 0:
#         new.append(num)

# print(new)

#15
# numbers = [1, -1, 2, -2, 3]
# i = 0
# for num in numbers:
#     if num > 0:
#         i += 1

# print(i)

#16
# first_list = [1 , 2]
# second_list = [3, 4]

# for num in second_list:
#     first_list.append(num)

# print(first_list)

#17
# numbers =[1, 2, 2, 3, 3, 4]
# print(list(set(numbers)))

# альтернатива 17
# numbers =[1, 2, 2, 3, 3, 4]
# wo_dubles = []

# for num in numbers:
#     if num not in wo_dubles:
#         wo_dubles.append(num)

# print(wo_dubles)

# 18
# nums = [1, 2, 3, 4]
# print(nums.index(3))

#19
# nums = [1, 2, 3, 4]
# reverse_num = []

# while len(nums) != 0:
#     reverse_num.append(nums[-1])
#     del nums[-1]

# print(reverse_num)

#20
# from random import randint
# nums = []
# while len(nums) <= 5:
#     nums.append(randint(1,10))

# print(nums)