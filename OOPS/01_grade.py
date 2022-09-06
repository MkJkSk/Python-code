class student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def Grade_no(self):
        return sum(self.grade) / len(self.grade)   



Result1 = student("John",[20,40,60,90,80])
print(Result1.name)
print(Result1.Grade_no())
