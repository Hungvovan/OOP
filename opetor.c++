#include <iostream>
using namespace std;

class ClassName {
private:
    // Các thuộc tính (Attributes)
    int attribute;

public:
    // Hàm thiết lập mặc định
    ClassName() : attribute(0) {}

    // Hàm thiết lập có tham số
    ClassName(int val) : attribute(val) {}

    // Hàm thiết lập sao chép
    ClassName(const ClassName &other) : attribute(other.attribute) {}

    // Hàm huỷ
    ~ClassName() {}

    // Phương thức nhập
    void input() {
        cout << "Nhập giá trị: ";
        cin >> attribute;
    }

    // Phương thức hiển thị
    void display() const {
        cout << "Giá trị: " << attribute << endl;
    }

    // Toán tử gán
    ClassName& operator=(const ClassName &other) {
        if (this != &other) {
            attribute = other.attribute;
        }
        return *this;
    }

    // Định nghĩa các toán tử
    friend ClassName operator+(const ClassName &a, const ClassName &b);
    friend ClassName operator-(const ClassName &a, const ClassName &b);
    friend ClassName operator*(const ClassName &a, const ClassName &b);
    friend ClassName operator/(const ClassName &a, const ClassName &b);
    friend bool operator>(const ClassName &a, const ClassName &b);
    friend bool operator<(const ClassName &a, const ClassName &b);
    friend bool operator==(const ClassName &a, const ClassName &b);
    friend ostream& operator<<(ostream &out, const ClassName &obj);
    friend istream& operator>>(istream &in, ClassName &obj);
};

// Toán tử cộng
ClassName operator+(const ClassName &a, const ClassName &b) {
    return ClassName(a.attribute + b.attribute);
}

// Toán tử trừ
ClassName operator-(const ClassName &a, const ClassName &b) {
    return ClassName(a.attribute - b.attribute);
}

// Toán tử nhân
ClassName operator*(const ClassName &a, const ClassName &b) {
    return ClassName(a.attribute * b.attribute);
}

// Toán tử chia
ClassName operator/(const ClassName &a, const ClassName &b) {
    if (b.attribute == 0) {
        cout << "Lỗi: Chia cho 0!" << endl;
        return ClassName();
    }
    return ClassName(a.attribute / b.attribute);
}

// Toán tử lớn hơn
bool operator>(const ClassName &a, const ClassName &b) {
    return a.attribute > b.attribute;
}

// Toán tử nhỏ hơn
bool operator<(const ClassName &a, const ClassName &b) {
    return a.attribute < b.attribute;
}

// Toán tử bằng
bool operator==(const ClassName &a, const ClassName &b) {
    return a.attribute == b.attribute;
}

// Toán tử xuất (<<)
ostream& operator<<(ostream &out, const ClassName &obj) {
    out << "Giá trị: " << obj.attribute;
    return out;
}

// Toán tử nhập (>>)
istream& operator>>(istream &in, ClassName &obj) {
    cout << "Nhập giá trị: ";
    in >> obj.attribute;
    return in;
}

int main() {
    ClassName obj1, obj2;

    cout << "Nhập đối tượng 1:" << endl;
    cin >> obj1;
    cout << "Nhập đối tượng 2:" << endl;
    cin >> obj2;

    cout << "Đối tượng 1: " << obj1 << endl;
    cout << "Đối tượng 2: " << obj2 << endl;

    ClassName obj3 = obj1 + obj2;
    cout << "Tổng của đối tượng 1 và 2: " << obj3 << endl;

    ClassName obj4 = obj1 - obj2;
    cout << "Hiệu của đối tượng 1 và 2: " << obj4 << endl;

    ClassName obj5 = obj1 * obj2;
    cout << "Tích của đối tượng 1 và 2: " << obj5 << endl;

    ClassName obj6 = obj1 / obj2;
    cout << "Thương của đối tượng 1 và 2: " << obj6 << endl;

    if (obj1 > obj2)
        cout << "Đối tượng 1 lớn hơn đối tượng 2" << endl;
    if (obj1 < obj2)
        cout << "Đối tượng 1 nhỏ hơn đối tượng 2" << endl;
    if (obj1 == obj2)
        cout << "Đối tượng 1 bằng đối tượng 2" << endl;

    return 0;
}

in mảng và tổng các phân tử
vector<Complex>danhsach;
for(int i=0;i<n;i++){
	Complex sp;
	sp.nhap();
  danhsach.push_back(sp); }

for(const auto& sp:danhsach){
	sp.in();
}
Complex tong(0,0);
for(const auto& sp:danhsach){
	tong=tong+sp;
}

tong.in();

