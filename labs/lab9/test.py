visitors = {tuple(input("visitor a").split(" ")): 0, tuple(input("visitor b").split(" ")): 0}
all_students = (tuple(input("visitor all students").split(" ")))
vist_keys = list(visitors.keys())

for student in all_students:
    visitors[vist_keys[0]] += vist_keys[0].count(student)
    visitors[vist_keys[1]] += vist_keys[1].count(student)

print(visitors[vist_keys[1]], visitors[vist_keys[1]])