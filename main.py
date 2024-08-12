import numpy as np
import pandas as pd

Students = pd.DataFrame(columns= ("Name", "Age", "Roll Number") )
courses_df = pd.DataFrame(columns= ("courses", "Roll Number"))

class Student:
    
    def __init__(self, name, age, roll_number):
        self.name = name
        self.age = age
        self.roll_number = roll_number

class student_manager:

    def add_student(self, name, age, roll_number):
        global Students

        data = {
            "Name" : [name],
            "Age" : [age],
            "Roll Number" : [roll_number]
        }

        Students = pd.concat([Students, pd.DataFrame(data)], ignore_index=True)

        return "Student data has been recorded successfully, proceed to course registration"

    def find_student(self, roll_number):
    
        if roll_number in Students["Roll Number"].values:
            result = Students['Roll Number'] == roll_number
            return result
        else:
            return "Student Not found"
       



class Course_manager:

    def register_course(self, roll_number, course):
        global courses_df
        
        course_data = {
            "courses" : course,
            "Roll Number" : [roll_number] * len (course)
        }

        courses_df = pd.concat([courses_df, pd.DataFrame(course_data)], ignore_index = True)

        return "Course registration complete"
    
    def new_course(self, course):
        with open("courses.txt", "a") as file:
            file.write("\n" + course + "\n")
        return "successful"
    
    def remove_course(self, course):
        with open ("courses.txt", "r") as file:
            content = file.read()

        lst = content.split("\n")
        for x in lst:
            if course in lst:
                lst.remove(course)
                with open ("courses.txt", "w") as file:
                    file.write("\n".join(lst))
                return "Course removed successfully"
            else:
                return "Course is not in database"
        
    def find_course(self, item):
        if item in courses_df["courses"].values:
            return courses_df[courses_df['courses'] == item]
    
    def course_averager(self, course_name):

        if course_name in courses_df["courses"].values:
            course_datas = courses_df[courses_df["courses"] == course_name]
            roll_numbers = course_datas["Roll Number"]
            students_in_course = Students[Students["Roll Number"].isin(roll_numbers)]
            average_age = students_in_course["Age"].mean()
            return average_age
        else:
            return "Course not found"
    def offered_courses (self, roll_number):
        if roll_number in courses_df["Roll Number"].values:
            courses_offered = courses_df[courses_df["Roll Number"] == roll_number]
            refined_list = courses_offered["courses"]
            return refined_list
        else:
            return "Student Not found"

StudentHandler = student_manager()
CourseHandler = Course_manager()

print("School Management system")

while True:

    try:
        print("Select Category \n1. ADMIN \n2. STUDENT")
        category = int(input("\nWhat category do you belong -- "))

        if category == 1:

            password = "BrightHeights0979"
            admin_id = input("Enter password -- ")

            if admin_id == password:
                print("\nWelcome Admin \n1. Print Student Database \n2. Find student \n3. Print course list \n4. Add course to system \n5. Print list of students offering a course \n6. Calculate average age of students offering a course \n7. Exit ")
                admin_task = int(input("\nSelect an operation by index Boss -- "))

                if admin_task == 1:
                    print(Students)

                elif admin_task == 2:
                    roll_number_to_find = int(input("Enter student roll_number -- "))
                    print(StudentHandler.find_student(roll_number_to_find))
                
                elif admin_task == 3:
                    print(courses_df)

                elif admin_task == 4:
                    course_name = input("Enter new course title -- ")
                    print(CourseHandler.new_course(course_name))

                elif admin_task == 5:
                    course_to_find = input("Enter the name of the course to be found -- ")
                    print(CourseHandler.find_course(course_to_find))
                
                elif admin_task == 6:
                    course_to_average = input("Enter the name of the course -- ")
                    print(CourseHandler.course_averager(course_to_average))
                    
                elif admin_task == 7:
                    break
                else:
                    print("Invalid operation")

            else:
                print("Incorrect password")
                continue

        elif category == 2:

            print("\n1. Student registration \n2. Course registration \n3. View courses offered \n4. Exit")
            operation = int(input("Select an operation by index -- "))

            if operation == 1:
                student_name = input("Enter your name -- ")
                student_age = int(input("Enter your age -- "))
                student_roll_no = int(input("Enter your roll number -- "))

                print(StudentHandler.add_student(student_name, student_age, student_roll_no))

            elif operation == 2:

                student_RollNumber = int(input("Enter your Roll number -- "))

                if student_RollNumber in Students["Roll Number"].values:

                    with open("courses.txt", "r") as file:
                        content = file.read()
                    courses_list = content.split("\n")

                    for index, item in enumerate(courses_list):
                        print(f"\n{index}: {item}")
                
                    student_desired_courses = input("Enter your desired courses seperated with a comma -- ").split(",")
                    print(CourseHandler.register_course(roll_number= student_RollNumber, course= student_desired_courses))

                else:
                    print("Student does not exist in database, please proceed to student registration")
            
            elif operation == 3:
              student_no = int(input("Enter your roll number -- "))
              print(CourseHandler.offered_courses(student_no))
              pass
            
            elif operation == 4:
                break

            else:
                print("Please ensure you have entered the correct index for your operation")
            
        else:
            print("Invalid category")

    except ValueError:
        print("You have entered an invalid value, Please check your entry")