class Student:
    subject="Python"
    def __init__(self,id="",name="",score1=1,score2=1):
        self.id=id
        self.name=name
        self.score1=score1
        self.score2=score2

    def inp(self):
        self.id=input()
        self.name=input()
        self.score1=int(input())
        self.score2=int(input())


    def display(self):
        return f"{self.id},{self.name},{self.score1},{self.score2}"


    def dtb(self):
        return (self.score1+self.score2)/2

if __name__=="__main__":
    st=Student()
    st.inp()
    

    with open("sv.txt", "w", encoding="utf-8") as f:
        f.write(st.display() + "\n")

    try:
        with open("sv.txt", "r", encoding="utf-8") as f:
            t = f.read()
            print(t)
    except Exception as e:
        print(f"{e}")
