#include<bits/stdc++.h>
using namespace std;
class PhanSo{
	private:
		int tu,mau;
	
	public:
		PhanSo(int tu=1,int mau=1):tu(tu),mau(mau){
		}
		int getTu()const{
			return tu;
		
		}
		int getMau()const{
			return mau;
		}
		void nhap(){
			cin>>tu;
			cin>>mau;
		}
		void display()const{
			if (mau==1){
				cout<<tu<<endl;
			}
			else{
				cout<<tu<<"/"<<mau<<endl;
			}
		}
		PhanSo operator+(const PhanSo& other)const{
			int newtu=tu *other.mau + mau *other.tu;
			int newmau=mau * other.mau;
			return PhanSo(newtu,newmau);
			
		}
		bool operator>(const PhanSo& other)const{
			return tu * other.mau > mau * other.tu;
		
		}
};
int main(){
 /*	PhanSo s1,s2;
	s1.nhap();
	s2.nhap();
	s1.display();
	s2.display();
	PhanSo s3=s1+s2;
	s3.display();
	if (s1>s2){
		cout<<"s1 big"<<endl;
	}
	else{
		cout<<"s2 small"<<endl;
	}  */
	int n;
	cin>>n;
	PhanSo sp[n];
	for(int i=0;i<n;i++){
		sp[i].nhap();
	}

	for(int i=0;i<n-1;i++){
		for(int j=0;j<n-i-1;j++){
			if(sp[j]>sp[j+1]){
				swap(sp[j],sp[j+1]);
			}
			
		}
	}
	for(int i=0;i<n;i++){
		sp[i].display();
	}
	
}
	
