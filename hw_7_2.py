def list_animals(animals):
    res = ''
    for i in range(len(animals)):
        res += str(i + 1) + '. ' + animals[i] + "\n"
    return res


animals = ['dog', 'cat', 'elephant']
print(list_animals(animals))