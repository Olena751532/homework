def sorter(textbooks):
    # Cramming before a test can't be that bad?
    return sorted(textbooks,key=str.lower)

subject = ['Algebra', 'English', 'Geometry', 'History']
print(sorter(subject))
