class Student:
    def __init__(self, name="", score1=0.0, score2=0.0):
        self.name = name
        self.score1 = score1
        self.score2 = score2
        self.avg = 0.0
        self.calculate_avg()

    def input(self):
        self.name = input("Nhập họ tên sinh viên: ")
        self.score1 = float(input("Nhập điểm kỳ 1: "))
        self.score2 = float(input("Nhập điểm kỳ 2: "))
        self.calculate_avg()

    def calculate_avg(self):
        self.avg = (self.score1 + 2 * self.score2) / 3

    def display(self):
        print(f"Họ tên: {self.name}")
        print(f"Điểm kỳ 1: {self.score1}")
        print(f"Điểm kỳ 2: {self.score2}")
        print(f"Điểm trung bình: {self.avg}")

    def __gt__(self, other):
        return self.avg > other.avg


def main():
    students = [Student() for _ in range(5)]

    for i in range(5):
        print(f"Nhập thông tin cho sinh viên thứ {i + 1}:")
        students[i].input()
        print()

    print("Danh sách sinh viên trước khi sắp xếp:")
    for student in students:
        student.display()
        print()

    students.sort(reverse=True)

    print("Danh sách sinh viên sau khi sắp xếp:")
    for student in students:
        student.display()
        print()

if __name__ == "__main__":
    main()
