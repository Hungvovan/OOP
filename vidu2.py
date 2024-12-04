class Computer:
    def __init__(self, ma='', hang='', namsx=2000, giaban=1):
        self.ma = ma
        self.hang = hang
        self.namsx = namsx
        self.giaban = giaban

    def set_ma(self, ma):
        self.ma = ma

    def get_ma(self):
        return self.ma

    def set_hang(self, hang):
        self.hang = hang

    def get_hang(self):
        return self.hang

    def set_nam(self, namsx):
        self.namsx = namsx

    def get_nam(self):
        return self.namsx

    def set_gia(self, giaban):
        self.giaban = giaban

    def get_gia(self):
        return self.giaban

    def nhap(self):
        self.ma = input("Nhap ma: ")
        self.hang = input("Nhap hang: ")
        self.namsx = int(input("Nhap nam san xuat: "))
        self.giaban = int(input("Nhap gia ban: "))

    def display(self):
        print(f"Ma MT: {self.ma}")
        print(f"Hang: {self.hang}")
        print(f"Nam SX: {self.namsx}")
        print(f"Gia ban: {self.giaban}")


class Laptop(Computer):
    def __init__(self, ma='', hang='', namsx=2000, giaban=1, can=0, doday=0, ktmanhinh=0, hedh='None'):
        super().__init__(ma, hang, namsx, giaban)
        self.can = can
        self.doday = doday
        self.ktmanhinh = ktmanhinh
        self.hedh = hedh

    def set_can(self, can):
        self.can = can

    def get_can(self):
        return self.can

    def set_doday(self, doday):
        self.doday = doday

    def get_doday(self):
        return self.doday

    def set_kich_thuoc_man_hinh(self, ktmanhinh):
        self.ktmanhinh = ktmanhinh

    def get_kich_thuoc_man_hinh(self):
        return self.ktmanhinh

    def set_he_dh(self, hedh):
        self.hedh = hedh

    def get_he_dh(self):
        return self.hedh

    def nhap(self):
        super().nhap()
        self.can = int(input("Nhap can nang: "))
        self.doday = int(input("Nhap do day: "))
        self.ktmanhinh = int(input("Nhap kich thuoc man hinh: "))
        self.hedh = input("Nhap he dieu hanh: ")

    def display(self):
        super().display()
        print(f"Can nang: {self.can} gram")
        print(f"Do day: {self.doday} mm")
        print(f"Kich thuoc man hinh: {self.ktmanhinh} inch")
        namsuudung = max(0, 2024 - self.get_nam())
        print(f"So nam su dung: {namsuudung} nam")
        depreciation_rate = 0.1 if self.hedh == 'Windows' else 0.05
        giatri_con_lai = self.get_gia() - namsuudung * depreciation_rate * self.get_gia()
        print(f"Gia tri con lai: {giatri_con_lai:.2f} VND")

    def gia_tri_con_lai(self):
        namsuudung = max(0, 2024 - self.get_nam())
        depreciation_rate = 0.1 if self.hedh == 'Windows' else 0.05
        return self.get_gia() - namsuudung * depreciation_rate * self.get_gia()

    def so_nam_su_dung(self):
        return max(0, 2024 - self.get_nam())

    def __gt__(self, other):
        return self.gia_tri_con_lai() > other.gia_tri_con_lai()


def main():
    n = int(input("Nhap so luong laptop: "))
    laptops = [Laptop() for _ in range(n)]

    for laptop in laptops:
        laptop.nhap()

    laptops.sort(key=lambda x: x.gia_tri_con_lai())

    print("\nDanh sach laptop:")
    for laptop in laptops:
        laptop.display()

    max_nam_su_dung = max(laptop.so_nam_su_dung() for laptop in laptops)

    print("\nLaptop co so nam su dung nhieu nhat:")
    for laptop in laptops:
        if laptop.so_nam_su_dung() == max_nam_su_dung:
            laptop.display()


if __name__ == "__main__":
    main()
