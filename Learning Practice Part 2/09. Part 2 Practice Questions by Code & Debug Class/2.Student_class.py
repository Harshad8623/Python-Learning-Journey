class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def total(self):
        return sum(self.marks)

    def average(self):
        return self.total() / len(self.marks)

    def display_details(self):
        return (
            self.name,
            self.marks,
            self.total(),
            self.average()
        )

student1 = Student("Harshad", [10, 8, 7, 9, 9])
print(student1.display_details())