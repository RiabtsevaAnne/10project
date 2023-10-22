
list1 = ["Марія", "Катерина", "Елизавета"]
list2 = ["Київ", "Одеса", "Донецьк"]
list3 = [4.5, 3.8, 4.2]

k = [(list1[i], list2[i], list3[i]) for i in range(len(list1))]

for student_info in k:
    print(f"{student_info[0]} - {student_info[1]} - {student_info[2]}")
