def double_char(s):
    result = ""
    for i in range(len(s)):
        result += s[i]*2
    return result


a = "Hello World"
print(double_char(a))
