class Job:
    def __init__(self, name, salary, hours_worked):
        self.name, self.salary, self.hours_worked = name, salary, hours_worked

    def print_details(self):
        print(f"{self.name}: ${self.salary}/month, {self.hours_worked} hours/week")

class Doctor(Job):
    def __init__(self, name, salary, hours_worked, specialty, years_experience):
        super().__init__(name, salary, hours_worked)
        self.specialty, self.years_experience = specialty, years_experience

    def print_details(self):
        super().print_details()
        print(f"Specialty: {self.specialty}, Experience: {self.years_experience} years")

class Teacher(Job):
    def __init__(self, name, salary, hours_worked, subject, position):
        super().__init__(name, salary, hours_worked)
        self.subject, self.position = subject, position

    def print_details(self):
        super().print_details()
        print(f"Subject: {self.subject}, Position: {self.position}")

#please replace zeros with your information
lawyer = Job("Lawyer", 0, 0)
cs_teacher = Teacher("Computer Science Teacher", 0, 0, "Computer Science", "Senior Teacher")
pediatric_doctor = Doctor("Pediatric Doctor", 0, 0, "Pediatrics", 0)

lawyer.print_details()
cs_teacher.print_details()
pediatric_doctor.print_details()
