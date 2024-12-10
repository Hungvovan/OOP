from idna import check_nfc


class Vehicle:
    def __init__(self,mpt="",tpt="",nsx=2000,giaban=1):
        self.mpt=mpt
        self.tpt=tpt
        self.nsx=nsx
        self.giaban=giaban

    def inp(self):
        self.mpt=input()
        self.tpt=input()
        self.nsx=int(input())
        self.giaban=int(input())

    def display(self):
        print(f"{self.mpt}")
        print(f"{self.tpt}")
        print(f"{self.nsx}")
        print(f"{self.giaban}")

class Car(Vehicle):
    def __init__(self,mpt="",tpt="",nsx=2000,giaban=1,cng=1,dc=1,nl=""):
        super().__init__(mpt, tpt, nsx, giaban)
        self.cng=cng
        self.dc=dc
        self.nl=nl


    def inp(self):
        super().inp()
        self.cng=int(input())
        self.dc=int(input())
        self.nl=input()

    def display(self):
        super().display()
        print(f"{self.cng}")
        print(f"{self.dc}")
        print(f"{self.nl}")

    def __gt__(self, other):
        return self.cng>other.cng







def main():
        n=int(input())
        lst=[]
        for _ in range(n):
            c=Car()
            c.inp()
            lst.append(c)

        lst.sort(key=lambda x:x.cng)

        for c in lst:
            c.display()
            print("-----")



if __name__=="__main__":
  """ c1=Car()
    c2=Car()
    c1.inp()
    c2.inp()
    c1.display()
    c2.display()
    if c1>c2:
        print("C1 lon hon")
    else:
        print("C2 lon hon")"""
  main()




