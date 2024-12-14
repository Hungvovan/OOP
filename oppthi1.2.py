class Student:
    subject = "Python"

    def __init__(self, id="", name="", score1=1, score2=1):
        self.id = id
        self.name = name
        self.score1 = score1
        self.score2 = score2

    def inp(self):
        self.id = input("Nhập ID: ").strip()
        if self.id == "":
            return False
        self.name = input("Nhập tên: ").strip()
        self.score1 = int(input("Nhập điểm 1: ").strip())
        self.score2 = int(input("Nhập điểm 2: ").strip())
        return True

    def display(self):
        return f"{self.id};{self.name};{self.dtb()}"

    def dtb(self):
        return (self.score1 + self.score2) / 2

    def __lt__(self, other):
        return self.dtb() < other.dtb()

    def __str__(self):
        return self.display()


if __name__ == "__main__":
    lst = []
    while True:
        sv = Student()
        if not sv.inp():
            break
        lst.append(sv)

    try:
        with open("sv.txt", "w", encoding="utf-8") as f:
            for sv in lst:
                f.write(f"{sv.id};{sv.name};{sv.score1};{sv.score2}\n")
    except Exception as e:
        print(e)

    try:
        with open("sv.txt", "r", encoding="utf-8") as f:
            lines = f.readlines()

        students = []
        for line in lines:
            id, name, score1, score2 = line.strip().split(";")
            students.append(Student(id, name, int(score1), int(score2)))

        students.sort()

        with open("ketqua.txt", "w", encoding="utf-8") as f:
            for sv in students:
                f.write(f"{sv.id};{sv.name};{sv.dtb():.1f}\n")

    except Exception as e:
        print(f"Lỗi: {e}")
