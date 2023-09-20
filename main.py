def are_strictly_identical(list1, list2):
    if len(list1) != len(list2):
        return False

    for i in range(len(list1)):
        if list1[i] != list2[i]:
            return False

    return True

def display_results(list1, list2):
    if are_strictly_identical(list1, list2):
        print("Two lists are strictly identical!")
    else:
        print("Two lists aren't strictly identical!")
    print(f"List 1: {list1}")
    print(f"List 2: {list2}\n")

if __name__ == '__main__':
    lists_to_check = [
        (['E', 'B', 'E', 'F', 'A', 'F'], ['E', 'B', 'E', 'F', 'A', 'F']),
        (['E', 'B', 'E', 'F', 'A', 'C'], ['E', 'B', 'E', 'F', 'A', 'F']),
        (['E', 'B', 'E', 'F', 'A', 'F', 'C'], ['E', 'B', 'E', 'F', 'A', 'F'])
    ]

    for list1, list2 in lists_to_check:
        display_results(list1, list2)
