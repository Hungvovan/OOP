const prompt = require('prompt-sync')();

class Canbo {
    constructor(mcb = "", hoten = "", gender = "") {
        this._mcb = mcb;
        this._hoten = hoten;
        this._gender = gender;
    }

    inp() {
        this._mcb = prompt("Nhập MCB: ");
        this._hoten = prompt("Nhập Họ Tên: ");
        this._gender = prompt("Nhập Giới Tính: ");
    }

    display() {
        console.log(`MCB: ${this._mcb}`);
        console.log(`Họ tên: ${this._hoten}`);
        console.log(`Giới tính: ${this._gender}`);
    }

    getGender() {
        return this._gender;
    }
}

class Congnhan extends Canbo {
    constructor(mcb = "", hoten = "", gender = "", bac = 1, ngaylam = 0, day = 1, month = 1, year = 2000) {
        super(mcb, hoten, gender);
        this._bac = bac;
        this._ngaylam = ngaylam;
        this._day = day;
        this._month = month;
        this._year = year;
    }

    inp() {
        super.inp();
        this._bac = parseInt(prompt("Nhập Bậc: "));
        this._ngaylam = parseInt(prompt("Nhập Ngày làm: "));
        this._day = parseInt(prompt("Nhập Ngày hợp đồng: "));
        this._month = parseInt(prompt("Nhập Tháng hợp đồng: "));
        this._year = parseInt(prompt("Nhập Năm hợp đồng: "));
    }

    display() {
        super.display();
        console.log(`Bậc: ${this._bac}`);
        console.log(`Ngày làm: ${this._ngaylam}`);
        console.log(`Hợp đồng: ${this._day}/${this._month}/${this._year}`);
        console.log(`Lương: ${this.luong()} VND`);
    }

    luong() {
        let cong = this._bac === 1 ? 300000 : this._bac === 2 ? 350000 : 400000;
        return this._ngaylam * cong;
    }
}

function main() {
    let n = parseInt(prompt("Nhập số lượng công nhân: "));
    if (n < 1 || n > 50) {
        console.log("Không hợp lệ");
        return;
    }

    let mang = [];
    for (let i = 0; i < n; i++) {
        let cn = new Congnhan();
        cn.inp();
        mang.push(cn);
    }

    mang.forEach(cn => {
        cn.display();
        console.log("<------------>");
    });

    let maxluong = Math.max(...mang.filter(cn => cn.getGender().toLowerCase() === "nam").map(cn => cn.luong()), 0);

    mang.forEach(cn => {
        if (cn.getGender().toLowerCase() === "nam" && cn.luong() === maxluong) {
            cn.display();
            console.log("-----------------------");
        }
    });
}

main();
