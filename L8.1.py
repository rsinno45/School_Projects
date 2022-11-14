class GradesFile:
    def __init__(self, filename, gradesList):
        self.__filename = filename

    def get_filename(self):
        return self.__filename

    def set_filename(self, filename):
        self.__filename = filename

    def get_gradesList(self):
        return self.__gradesList

    def set_gradesList(self, gradesList):
        self.__gradesList = gradesList

    def calculateAverage(self):
        a=0
        testFile = open('Grades.txt', 'r')
        nums = testFile.readline()
        for line in nums:
            for i in line:
                if i.isdigit()==True:
                    a += (int(i))/10

        print(a)
        testFile.close()

    def loadGradesData(self):
        fileobj=open('Grades.txt')
        lines=[]
        for line in fileobj:
            lines.append(line.strip())
        print(lines)





def main():
    import random
    stu1 = random.randint(1, 100)
    stu2 = random.randint(1, 100)
    stu3 = random.randint(1, 100)
    stu4 = random.randint(1, 100)
    stu5 = random.randint(1, 100)
    stu6 = random.randint(1, 100)
    stu7 = random.randint(1, 100)
    stu8 = random.randint(1, 100)
    stu9 = random.randint(1, 100)
    stu10 = random.randint(1, 100)
    testFile = open('Grades.txt','w')
    testFile.write(str(stu1))
    testFile.write(str(stu2))
    testFile.write(str(stu3))
    testFile.write(str(stu4))
    testFile.write(str(stu5))
    testFile.write(str(stu6))
    testFile.write(str(stu7))
    testFile.write(str(stu8))
    testFile.write(str(stu9))
    testFile.write(str(stu10))
    testFile.close()

main()
calc = GradesFile
calc.calculateAverage('Grades.txt')
calc.loadGradesData('Grades.txt')