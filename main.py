from selectionsort2 import sort

names = ['Emma', 'Brian', 'Evelyn', 'Frank', 'Alex', 'Felecia', 'Carl']
grades = ['A', 'B', 'D', 'C', 'A', 'F', 'B']

print("Original:")
print("Names   Grades")
for i in range(len(names)):
    print(f"{names[i]:<8} {grades[i]}") # I used 'f-string' formatting to align names and grades neatly side by side.

first = 0  
sort(names, grades, first)

print("\nSorted:")
print("Names   Grades")
for i in range(len(names)):
    print(f"{names[i]:<8} {grades[i]}")
