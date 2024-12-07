class Congnhan:
    def __init__(self, mcn="", hoten="", bac=1, ngaylam=0, hopdong=None):
        self.mcn = mcn
        self.hoten = hoten
        self.bac = bac
        self.ngaylam = ngaylam
        self.hopdong = hopdong if hopdong else {'day': 0, 'month': 0, 'year': 0}
        self.tien_luong = self.luong()

    def nhapdata(self):
        self.mcn = input("Nhập mã công nhân: ")
        self.hoten = input("Nhập họ tên: ")
        self.bac = int(input("Nhập bậc (1-3): "))
        self.ngaylam = int(input("Nhập số ngày làm việc: "))
        day = int(input("Nhập ngày ký hợp đồng (ngày): "))
        month = int(input("Nhập ngày ký hợp đồng (tháng): "))
        year = int(input("Nhập ngày ký hợp đồng (năm): "))
        self.hopdong = {'day': day, 'month': month, 'year': year}
        self.tien_luong = self.luong()

    def luong(self):
        if self.bac == 1:
            tien_cong = 300000
        elif self.bac == 2:
            tien_cong = 350000
        elif self.bac == 3:
            tien_cong = 400000
        else:
            tien_cong = 0
        return self.ngaylam * tien_cong

    def display(self):
        print(f"MCN:{self.mcn}")
        print(f"Ho ten:{self.hoten}")
        print(f"Bac:{self.bac}")
        print(f"Ngay lam:{self.ngaylam}")
        print(f"Luong:{self.luong()}")
        print(f"Hop dong:{self.hopdong['day']}/{self.hopdong['month']}/{self.hopdong['year']}")

    def hien_thi_ngan(self):
        print(f"{self.mcn}, {self.hoten}, {self.hopdong['day']}/{self.hopdong['month']}/{self.hopdong['year']}, {self.ngaylam}, {self.luong()}")


    def __gt__(self, other):
        if self.hopdong['year']>other.hopdong['year']:
            return True
        elif self.hopdong['year'] == other.hopdong['year']:
            if self.hopdong['month'] > other.hopdong['month']:
                return True
            elif self.hopdong['month'] == other.hopdong['month']:
                return self.hopdong['day'] > other.hopdong['day']
        return False

def dscn():
    danh_sach = []
    ma_cong_nhan_set = set()

    while True:
        ma_cong_nhan = input("Nhập mã công nhân (hoặc Enter để dừng): ")
        if ma_cong_nhan == "":
            break

        if ma_cong_nhan in ma_cong_nhan_set:
            print("Mã công nhân đã tồn tại, vui lòng nhập lại.")
            continue

        cn = Congnhan()
        cn.nhapdata()
        danh_sach.append(cn)
        ma_cong_nhan_set.add(ma_cong_nhan)

    return danh_sach

def in_thong_tin_cong_nhan(danh_sach):
    for cn in danh_sach:
        cn.display()
        print()

def in_cong_nhan_bac_1(danh_sach):
    for cn in danh_sach:
        if cn.bac == 1:
            cn.hien_thi_ngan()

if __name__ == "__main__":
    lst= dscn()

    in_thong_tin_cong_nhan(lst)

    lst.sort()

    print("Danh sách công nhân sau khi sắp xếp:")
    in_thong_tin_cong_nhan(lst)

    print("\nThông tin các công nhân có bậc 1:")
    in_cong_nhan_bac_1(lst)





