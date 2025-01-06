def soluong(n):
    c=0
    while n>0:
        n//=10
        c+=1
    return c

def dequy(n):
    if n<10:
        return 1
    return 1 + dequy(n//10)
 
## Đếm bao nhiêu chữ số trong số

def gt(n):
    kq=1
    for i in range(1,n+1):
        kq*=i
    return kq

def gt(n):
    if n<1:
        return 1
    return n* gt(n-1)
#Giai thua
def chinh(n, k):
    result = 1 
    for i in range(n, n - k, -1):
        result *= i 
    return result

def tohop(n,k):
    result = 1 
    for i in range(n, n - k, -1):
        result *= i 
    for i in range(1,k+1):
        result//=i
    return result
""" So phong phu
def uocso(n):
    tong=0
    for i in range(1,n):
        if n%i==0:
            tong+=i
    return tong

def tinhtong(n):
    c=0
    for i in range(1,n+1):
        if uocso(i)>i:
            c+=i
    return c

n=int(input())
print(tinhtong(n))
Dictory
def xuli():
    n=int(input())
    students=[]
    for _ in range(n):
        line=input()
        parts=line.split(";")
        student={
            "id":parts[0].strip(),
            "name":parts[1].strip(),
            "gender":parts[2].strip(),
            "class":parts[3].strip()
        }
        students.append(student)

        max_nam=sum(1 for s in students if s["gender"]=="M")
        max_nu=sum(1 for s in students if s["gender"]=="F")
        xapxep=sorted(students,key=lambda x:x["class"])

        print(max_nam,max_nu)
        for s in xapxep:
            print(f"{s['id']},{s['name']},{s['gender']},{s['class']}")


xuli()

def quan_ly_hang_hoa():
    ListMH = []

    print("Nhập thông tin mặt hàng (nhập tên mặt hàng rỗng để dừng):")
    while True:
        ten = input("Tên mặt hàng: ").strip()
        if ten == "":
            break
        so_luong = int(input("Số lượng còn lại: "))
        gia_ban = int(input("Giá bán: "))

        mat_hang = {
            "Ten": ten,
            "SoLuong": so_luong,
            "GiaBan": gia_ban
        }
        ListMH.append(mat_hang)

    print("\nCác mặt hàng có số lượng dưới 5:")
    for mh in ListMH:
        if mh["SoLuong"] < 5:
            print(f"- Tên: {mh['Ten']}, Số lượng: {mh['SoLuong']}, Giá bán: {mh['GiaBan']}")

    tong_tien_hang = sum(mh["SoLuong"] * mh["GiaBan"] for mh in ListMH)
    print(f"\nTổng số tiền hàng: {tong_tien_hang} VND")

quan_ly_hang_hoa()


"""



if __name__=="__main__":
    n=int(input())
    print(soluong(n))
    print(dequy(n))