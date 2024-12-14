data = input("Nhập dữ liệu: ")

try:
    # Ghi dữ liệu vào file chuoi.txt
    with open("chuoi.txt", "w", encoding="utf-8") as f:
        f.write(data + "\n")

    # Đọc dữ liệu từ chuoi.txt
    with open("chuoi.txt", "r", encoding="utf-8") as f:
        dchuoi = f.read()

    # Phân loại ký tự
    so = "".join([x for x in dchuoi if x.isdigit()])  # Chỉ lấy các số
    chu = "".join([x for x in dchuoi if x.isalpha()])  # Chỉ lấy các chữ cái
    kitu = "".join([x for x in dchuoi if not x.isalnum()])


    with open("ketqua.txt", "w", encoding="utf-8") as f:
        f.write(so + "\n")
        f.write(chu + "\n")
        f.write(kitu + "\n")


except Exception as e:
    print(f"Đã xảy ra lỗi: {e}")
