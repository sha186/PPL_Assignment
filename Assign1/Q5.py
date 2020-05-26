def missing_numbers(num_list):
    print(num_list)
    original_list = [x for x in range(num_list[0], num_list[-1] + 1)]
    num_list = set(num_list)
    return (list(num_list ^ set(original_list)))


print("The missing numbers are:")
print(missing_numbers([1, 3, 4, 6, 7, 10, 14, 17, 21, 25]))
