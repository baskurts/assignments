def sort(names, grades, first: int):
    """
    Sorts a list of grades from largest to smallest and
    sorts the list of names according to the order defined by 
    the sorted grades using selection sort
    Args:
        names: list of names
        grades: list of grades
        first (int): the list index at which the sort will begin
    """
    i = len(grades) - first - 1
    j = 0
    big = 0
    temp_grade = 0

    while i > 0:
        big = first
        j = first + 1

        while j <= first + i:
            if grades[big] < grades[j]:
                big = j
            
            j += 1  

        temp_grade = grades[first + i]
        temp_name = names[first + i] 

        grades[first + i] = grades[big]
        names[first + i] = names[big]

        grades[big] = temp_grade
        names[big] = temp_name

        i -= 1
