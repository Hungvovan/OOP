class PhanSo:
    def __init__(self, tu=1, mau=1):
        self.tu = tu
        self.mau = mau

    def get_tu(self):
        return self.tu

    def get_mau(self):
        return self.mau

    def nhap(self):
        self.tu = int(input())
        self.mau = int(input())

    def display(self):
        if self.mau == 1:
            print(self.tu)
        else:
            print(f"{self.tu}/{self.mau}")

    def __add__(self, other):
        new_tu = self.tu * other.mau + self.mau * other.tu
        new_mau = self.mau * other.mau
        return PhanSo(new_tu, new_mau)

    def __gt__(self, other):
        return self.tu * other.mau > self.mau * other.tu


def main():
    # s1 = PhanSo()
    # s2 = PhanSo()
    # s1.nhap()
    # s2.nhap()
    # s1.display()
    # s2.display()
    # s3 = s1 + s2
    # s3.display()
    # if s1 > s2:
    #     print("s1 big")
    # else:
    #     print("s2 small")

    n = int(input())
    danhsach = []
    for i in range(n):
        ps = PhanSo()
        ps.nhap()
        danhsach.append(ps)

    for ps in danhsach:
        ps.display()


if __name__ == "__main__":
    main()
