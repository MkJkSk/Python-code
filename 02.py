class student:
    def __init__(self,name,age,cgpa,percentage,Branch,Phoneno,Pincode,BloodGr):
        self.name = name
        self.age = age
        self.cgpa = cgpa
        self.percentage = percentage
        self.Branch =Branch
        self.Phoneno = Phoneno
        self.Pincode  = Pincode
        self.BloodGr = BloodGr
    def identification(self):
        print(f"Your First name  as per addhar card only  is {self.name}")    
    def Year(self):
        print(f"Your current age is {self.age} ") 
    def Marksheet(self):
            print(f"Your cgpa in Engineering in last year is {self.cgpa} and percentage is {self.percentage}")

    def section(self):
        print(f"Your Branch in Engineering is {self.Branch}")
    def contact(self):
        print(f"Your Phone no is {self.Phoneno}")
    def Postal(self):
        print(f"Your address pincode is {self.Pincode}")
    def Group(self):
        print(f"Your Blood Group is {self.BloodGr}")        
        

college = student("Muzammil Ahmed Khan",23,8.87,74, "Computer science Engineering",
9834338460,444601,"O+")
# print(company.name)
college.identification()
college.Year()
college.Marksheet()
college.section()
college.contact()
college.Postal()
college.Group()