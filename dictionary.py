#example of dict
student = {"name" : "Aryan", "Age" : 17, "id" : 20}
print(student)

#Access value by key
student = {"name" : "Aryan", "Age" : 17, "id" : 20}
x = student["name"]
print(x)

#update key value
student = {"name" : "Aryan", "Age" : 17, "id" : 20}
student["id"] = 1
print(student)

#Find length
student = {"name" : "Aryan", "Age" : 17, "id" : 20}
print(len(student))

#Add item
student = {"name" : "Aryan", "Age" : 17, "id" : 20}
student["Mob no"] = 9702850829
print(student)

#remove an item
student = {"name" : "Aryan", "Age" : 17, "id" : 20}
student.pop("id")
print(student)

#copy
student = {"name" : "Aryan", "Age" : 17, "id" : 20}
Teacher = student.copy()
print(Teacher)