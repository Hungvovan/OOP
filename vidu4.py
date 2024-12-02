class Nguoi:
    def __init__(self,hodem="",ten="",day=1,month=1,year=2000):
        self.__hodem=hodem
        self.__ten=ten
        self.__day=day
        self.__month=month
        self.__year=year


    def inp(self):
        self.__hodem=input()
        self.__ten=input()
        self.__day=int(input())
        self.__month =int(input())
        self.__year = int(input())


    def display(self):
        print(f"Ho dem: {self.__hodem}")
        print(f"Ten: {self.__ten}")
        print(f"Ngay sinh: {self.__day}/{self.__month}/{self.__year}")


    def __gt__(self, other):
        if self.__ten > other.__ten:
            return True
        elif self.__ten < other.__ten:
            return False
        else:
            return self.__hodem > other.__hodem


class SinhVien(Nguoi):
    def __init__(self,hodem="",ten="",day=1,month=1,year=2000,msv="",dtb=1):
        super().__init__(hodem,ten,day,month,year)
        self.__msv=msv
        self.__dtb=dtb

    def inp(self):
        super().inp()
        self.__msv =input()
        self.__dtb =int(input())


    def display(self):
        super().display()
        print(f"MSV: {self.__msv}")
        print(f"DTB: {self.__dtb}")


if __name__=="__main__":
    sv=SinhVien()
    sv.inp()
    sv.display()