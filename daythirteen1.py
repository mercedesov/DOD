def halves(your_tuple):
    length = len(your_tuple)
    middle = (length) // 2
    half1 = your_tuple[:middle]
    half2 = your_tuple[middle:]

    print(f"First half values: {half1}")
    print(f"Second half values: {half2}")


your_tuple = tuple(map(int, input("Enter your tuple: ").split(',')))
halves(your_tuple)
