# 面试题3（一）：找出数组中重复的数字
# 题目：在一个长度为n的数组里的所有数字都在0到n-1的范围内。数组中某些数字是重复的，但不知道有几个数字重复了，
# 也不知道每个数字重复了几次。请找出数组中任意一个重复的数字。例如，如果输入长度为7的数组{2, 3, 1, 0, 2, 5, 3}，
# 那么对应的输出是重复的数字2或者3。
# /usr/bin/env python3
# -*- coding: utf-8 -*-


def duplicate(numbers, length):

    if not numbers:
        return False

    for i in numbers:
        if i < 0 or i > length-1:
            return False

    for i in range(0, length):
        while i != numbers[i]:
            if numbers[numbers[i]] == numbers[i]:
                return numbers[i]

            numbers[numbers[i]], numbers[i] = numbers[i], numbers[numbers[i]]

    return False

# test case
if __name__ == '__main__':
    # 包含一个或多个重复数字
    arr = [2, 3, 3, 5, 1, 0]
    rst = duplicate(arr, 6)
    print('rst=%s ' % rst)

    # 不包含重复数字
    arr = [2, 3, 1, 4]
    rst = duplicate(arr, 4)
    print('rst=%s ' % rst)

    # 无效输入:空数组、数组指越界
    arr = []
    rst = duplicate(arr, 4)
    print('rst=%s ' % rst)

    arr = [5, 6, 7, 3]
    rst = duplicate(arr, 4)
    print('rst=%s ' % rst)
