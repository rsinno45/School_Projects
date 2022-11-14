class Course:
    def __init__(self, name, subject, courseNumber):
        self.name = name
        self.subject = subject
        self.courseNumber = courseNumber

    def __str__(self):
        return (self.subject + " " + self.courseNumber + ": " + self.name)

class CourseInfo:
    def __init__(self, credits, classNum, schedule, className):
        self.credits = credits
        self.classNum = classNum
        self.schedule = schedule
        self.className = className
        self.students = []

    def students(self, *args):
        for arg in args:
            self.students.append(arg)
            arg.courseList.append(self)

    def getStudents(self):
        return self.students

    def __str__(self):
        if self.professor:
            return (self.className + "- " + self.credits + ", " + self.professor)
        else:
            return (self.className + "- " + self.credits)

