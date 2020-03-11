def summation(num):
    # a = 0
    # for i in range(num + 1):
    #     a += i
    # return a
    if num ==  1:
        return num
    else:
        return num + summation(num - 1)




numbers1 = 13
print(summation(numbers1))
