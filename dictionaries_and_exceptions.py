student = {
"name":"Mark",
"student_id":15163,
"feedback":None
}

student["last_name"] = "Kowlaski"

print(student)
print(student["name"])
print(student.get("last_name","Unknown"))

print(student.keys())


try:
    last_name = student["last_name"]
    numbered_last_name = 3 + last_name
except KeyError:
    print("Eroor finding last_name")
except TypeError as error:
    print("I can't add these two together")
    print(error)
    #need to add module to print the line the error occurs

all_students=[
{"name":"Mark", "student_id":15463},
{"name":"Katarina", "student_id":63112},
{"name":"Jessica","student_id":30021}
]

print(all_students)
