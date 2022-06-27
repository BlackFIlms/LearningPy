def get_max_value_from_list(arr: list) -> int:
    arr.sort()
    print(arr)
    return arr[-1]

print(get_max_value_from_list([1,5,3,87,20,43,11,2,0,-93,59]))