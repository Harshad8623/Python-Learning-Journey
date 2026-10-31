class Student:
    def __init__(self, name: str, age: int, gender: str, marks: list[int]):
        self.name = name
        self.gender = gender
        self.age = age
        self.marks = marks

    def display(self):
        print(f"Name   : {self.name}")
        print(f"Gender : {self.gender}")
        print(f"Age    : {self.age}")
        print(f"Marks  : {self.marks}")

    def calculate_total(self):
        total = 0
        for i in self.marks:
            total += i
        return total


    def calculate_average(self):
        total = self.calculate_total()
        average = total / len(self.marks)
        return average

    def get_highest_marks(self):
        maximum = self.marks[0]
        for i in self.marks:
            if maximum < i:
                maximum = i
        return maximum
    
    def get_lowest_marks(self):
        minimum = self.marks[0]
        for i in self.marks:
            if minimum > i:
                minimum = i
        return minimum
    
    def has_passed(self):
        for i in self.marks:
            if i < 35:
                return "Fail"
        return "Pass"
    

student1 = Student("Harshad", 21, "Male", [98, 100, 96, 97])
student1.display()
print(f"Total : {student1.calculate_total()}")
print(f"Average : {student1.calculate_average():.2f}")
print(f"Maximum : {student1.get_highest_marks()}")
print(f"Maximum : {student1.get_lowest_marks()}")
print(f"Status : {student1.has_passed()}")

print()

student2 = Student("Vedant", 18, "Male", [89, 90, 94, 95])
student2.display()
print(f"Total : {student2.calculate_total()}")
print(f"Average : {student2.calculate_average():.2f}")
print(f"Maximum : {student2.get_highest_marks()}")
print(f"Maximum : {student2.get_lowest_marks()}")
print(f"Status : {student2.has_passed()}")
