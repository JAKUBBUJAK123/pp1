def compare(array1,array2):
    if len(array1) != len(array2):
        return False
    else:
        for i in range(len(array1)):
            if array1[i] != array2[i]:
                return False
            else:
                return True


print(compare(["sky", "book"],["sky","book"]))
compare([3,2,1],[3,3])