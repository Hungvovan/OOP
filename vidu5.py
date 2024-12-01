class Canbo:
    def __init__(self, mcb="", hoten="", gender=""):
        self.__mcb = mcb
        self.__hoten = hoten
        self.__gender = gender

    def inp(self):
        self.__mcb = input("Nhập MCB: ")
        self.__hoten = input("Nhập Họ Tên: ")
        self.__gender = input("Nhập Giới Tính: ")

    def display(self):
        print(f"MCB: {self.__mcb}")
        print(f"Họ tên: {self.__hoten}")
        print(f"Giới tính: {self.__gender}")

    def get_gender(self):
        return self.__gender

class Congnhan(Canbo):
    def __init__(self, macb="", hoten="", gender="", bac=1, ngaylam=0, day=1, month=1, year=2000):
        super().__init__(macb, hoten, gender)
        self.__bac = bac
        self.__ngaylam = ngaylam
        self.__day = day
        self.__month = month
        self.__year = year

    def inp(self):
        super().inp()
        self.__bac = int(input("Nhập Bậc: "))
        self.__ngaylam = int(input("Nhập Ngày làm: "))
        self.__day = int(input("Nhập Ngày hợp đồng: "))
        self.__month = int(input("Nhập Tháng hợp đồng: "))
        self.__year = int(input("Nhập Năm hợp đồng: "))

    def display(self):
        super().display()
        print(f"Bậc: {self.__bac}")
        print(f"Ngày làm: {self.__ngaylam}")
        print(f"Hợp đồng: {self.__day}/{self.__month}/{self.__year}")
        print(f"Lương: {self.luong()} VND")

    def luong(self):
        cong = 300000 if self.__bac == 1 else 350000 if self.__bac == 2 else 400000
        return self.__ngaylam * cong

def main():
    n = int(input("Nhập số lượng công nhân: "))
    if n < 1 or n > 50:
        print("Không hợp lệ")
        return

    mang = []
    for i in range(n):
        cn = Congnhan()
        cn.inp()
        mang.append(cn)

    for cn in mang:
        cn.display()
        print("<------------>")

    maxluong = max((cn.luong() for cn in mang if cn.get_gender().lower() == "nam"), default=0)

    for cn in mang:
        if cn.get_gender().lower() == "nam" and cn.luong() == maxluong:
            cn.display()
            print("-----------------------")

if __name__ == "__main__":
    main()
