# Create a dictionary with the roll number, name and marks of n students in a class
# and display the names of students who have scored marks above 75.

n = int(input("Enter the number of students in a class"))
print("Enter the roll number ,name and marks of each student")
dic_class = dict()
for i in range(0, n, 1):
    print("Enter the details of student ", i + 1)
    s_roll_number = int(input("Roll number: "))
    s_name = input("Name: ")
    s_marks = int(input("Marks: "))
    dic_s = {"roll number": s_roll_number, "name": s_name, "marks": s_marks}

    dic_class["s{}".format(i + 1)] = dic_s

print("The Students who scored marks above 75 are")
for s_info in dic_class.values():
    if s_info["marks"] > 75:
        print(s_info["name"])
