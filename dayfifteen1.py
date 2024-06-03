def length_sort(str):
    list = [s.strip() for s in str.split(',')]

    sorted_list = sorted(list, key=len)

    return sorted_list


print(length_sort("apple, pie, banana, pear"))
print(length_sort("a, abc, ab"))
print(length_sort("longest, long, longer"))
print(length_sort("one, two, three, four"))
