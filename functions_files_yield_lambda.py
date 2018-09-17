#try to make it 1 function does only 1 thing

print("Hello World")
str(3) == '3'
int("15") == 15
username = input("Enter user's name: ")

students=[]
#functions
def get_students_titlecase():
    student_titlecase = []
    for student in students:
        student_titlecase = student.title()
    return student_titlecase


def print_student_titlecase():
    # student_titlecase = []
    # for student in students:
    #     student_titlecase =  student.title()
    student_titlecase = get_students_titlecase()
    print(student_titlecase)


def add_student(name, student_id=332):
    student = {"name": name, "student_id": student_id}
    # students.append(name)
    students.append(student)


def var_args(name, *args):
    print(name)
    print(args)


def var_args2(name, **kwargs):
    print(name)
    print(kwargs["description"], kwargs["feedback"])


student_list = get_students_titlecase()

# add_student("Mark", 332)
add_student("Mark")
# add_student("Mark2", 15)
add_student(name="Mark", student_id=15)

var_args("Mark3", "loves python", None, "hello", True)

var_args2("Mark4", description="loves python", feedback=None, pluralsight_subscriber=True)
