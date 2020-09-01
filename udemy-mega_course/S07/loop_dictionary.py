
# Example 1
student_grades = {"Marry":9.1,"Jim":5.8,"John":9.4}

for grades in student_grades.items():
    print (grades)

for grades in student_grades.keys():
    print (grades)

# Example 2
phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}

for pair in phone_numbers.items():
    print("{} has as phone number {}".format(pair[0], pair[1]))

for key, value in phone_numbers.items():
    print("{} has as phone number {}".format(key, value))    