i = 2
while i <= 17:
    print(i, end=", " if i < 17 else "")
    if i == 13:
        i += 1  # ข้าม 13 ไปเพิ่ม 1 เพื่อให้ได้ 14
    else:
        i += 3
