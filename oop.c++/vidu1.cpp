#include <bits/stdc++.h>
using namespace std;

class Canbo {
private:
    string macb;
    string hoten;
    string gender;

public:
    Canbo(string macb = "", string hoten = "", string gender = "") : macb(macb), hoten(hoten), gender(gender) {}

    string getmacb() const {
        return macb;
    }

    string gethoten() const {
        return hoten;
    }

    string getgender() const {
        return gender;
    }

    virtual void nhap() {
        getline(cin, macb);
        getline(cin, hoten);
        getline(cin, gender);
    }

    virtual void in() {
        cout << "MaCB: " << macb << endl;
        cout << "Ho ten: " << hoten << endl;
        cout << "Gender: " << gender << endl;
    }
};

class Congnhan : public Canbo {
private:
    int bac;
    int ngaylam;
    int day, month, year;

public:
    Congnhan(string macb = "",
             string hoten = "",
             string gender = "",
             int bac = 1,
             int ngaylam = 0,
             int day = 1,
             int month = 1,
             int year = 2000)
        : Canbo(macb, hoten, gender), bac(bac), ngaylam(ngaylam), day(day), month(month), year(year) {}

    int getbac() const {
        return bac;
    }

    int getngaylam() const {
        return ngaylam;
    }

    int getday() const {
        return day;
    }

    int getmonth() const {
        return month;
    }

    int getyear() const {
        return year;
    }

    void nhap() override {
        Canbo::nhap();
        cin >> bac;
        cin >> ngaylam;
        cin >> day >> month >> year;
        cin.ignore();
    }

    void in() override {
        Canbo::in();
        cout << "Bac: " << bac << endl;
        cout << "Ngay lam: " << ngaylam << endl;
        cout << "Ngay ki hop dong: " << day << "/" << month << "/" << year << endl;
        cout << "Luong: " << Luong() << endl;
    }

    int Luong() const {
        int cong;
        if (bac == 1) {
            cong = 300000;
        } else if (bac == 2) {
            cong = 350000;
        } else {
            cong = 400000;
        }
        return ngaylam * cong;
    }

    bool operator>(const Congnhan& other) const {
        if (year != other.year) {
            return year > other.year;
        }
        if (month != other.month) {
            return month > other.month;
        }
        return day > other.day;
    }
};

int main() {
 /*  Congnhan s1;
    s1.nhap();
    s1.in();
    return 0;
    */
    int n;
    cin>>n;
    Congnhan danhsach[50];
    for(int i=0;i<n;i++){
    	danhsach[i].nhap();
	}
	for(int i=0;i<n-1;i++){
		for(int j=i+1;j<n;j++){
			if(danhsach[j]>danhsach[i]){
				swap(danhsach[i],danhsach[j]);
			}
		}
	}
	for (int i = 0; i < n; ++i) { 
	danhsach[i].in(); 
	cout << "-----------------------\n";
    }

	int maxluong = 0;
	for (int i = 0; i < n; ++i) { 
	if (danhsach[i].getgender() == "Nam") { 
	maxluong = max(maxluong, danhsach[i].Luong()); 
		} 
	}
	for(int i = 0; i < n; ++i) { 
	if (danhsach[i].getgender() == "Nam" && danhsach[i].Luong() == maxluong) {
	 	danhsach[i].in(); 
	 	cout << "-----------------------\n"; 
		 } 
	}
	return 0;
}
