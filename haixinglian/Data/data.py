# coding:utf-8
import random


def create_phone():
    # 第二位数字
    second = [3, 4, 5, 7, 8,9][random.randint(0, 5)]
    '''
    # 第三位数字
    third = {
        3: random.randint(0, 9),
        4: [5, 7, 9][random.randint(0, 2)],
        5: [i for i in range(10) if i != 4][random.randint(0, 8)],
        7: [i for i in range(10) if i not in [4, 9]][random.randint(0, 7)],
        8: random.randint(0, 9),
    }[second]
    '''

    # 最后八位数字
    suffix = random.randint(99999999,1000000000)

    # 拼接手机号
    return "1{}{}".format(second, suffix)
    #return "1{}{}{}".format(second, third, suffix)

# 生成手机号
phone_num = create_phone()
print(phone_num)
