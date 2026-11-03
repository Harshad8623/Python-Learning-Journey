class Student:
        def __init__(
            self,
            name: str,
            age: int,
            marks: list[int]
        ) -> None:
            self.name = name
            self.age = age
            self.marks = marks

        def total_marks(self) -> int:
            return sum(self.marks)

        def average_marks(self) -> float:
            return self.total_marks() / len(self.marks)

        def demo():
            print("This is demo")

        def display_grade(self) -> None:
            average = self.average_marks()


            if average >= 90:
                print("Grade A")
            elif average >= 50:
                print("Grade B")
            else:
                print("Grade C")


student1 = Student("Aniruddh", 20, [78, 54, 19, 63])

print("Total:", student1.total_marks())
print("Average:", student1.average_marks())
student1.display_grade()
Student.deom()
student1.demo()