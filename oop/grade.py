'''
클래스에 학생 이름을 입려하면
해당 학생이 얻은 3과목의 평균 점수에 따라 A - F까지 출력하시오.
해당 문제 해결을 위해서 교재 72페이지의 리스트를 참조하세요.
'''
class Grade:
    def __init__(self, name):
        self.name = name
        self.marks = []

    def addMarks(self, mark):
        self.marks.append(mark)

    def avg(self):
        return sum(self.marks) / len(self.marks)

    @staticmethod
    def main():
        student = Grade(input("학생 이름 입력 : "))
        for subject in ['국어', '영어', '수학']:
            student.addMarks(int(input(subject+"점수 입력 : ")))
        avg = student.avg()

        if avg >= 90:
            grade = "A"
        elif avg >= 80:
            grade = "B"
        elif avg >= 70:
            grade = "C"
        elif avg >= 60:
            grade = "D"
        elif avg >= 50:
            grade = "E"
        else :
            grade = "F"

        print(f'{student.name}의 과목 평균 : {int(avg)}. 학점은 {grade}입니다.')


if __name__ == "__main__":
    Grade.main()
