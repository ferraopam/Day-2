def armstrong_num(num):
    num_1 = num
    res = 0
    while num != 0:
        r = num % 10
        res = res + r ** 3
        num = num / 10
    return num_1 = res
input_num = int(input("Enter type number:"))
if armstrong_num(input_num)