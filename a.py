import random
from pathlib import Path

# Đọc dữ liệu từ các file
dateborns = [
    line.strip()
    for line in Path("dateborn.txt").read_text(encoding="utf-8").splitlines()
    if line.strip()
]

names = [
    line.strip()
    for line in Path("Names.txt").read_text(encoding="utf-8").splitlines()
    if line.strip()
]

students = [
    line.strip()
    for line in Path("Students.txt").read_text(encoding="utf-8").splitlines()
    if line.strip()
]

# Kiểm tra dữ liệu đầu vào
if not dateborns or not names:
    raise ValueError("dateborn.txt hoặc Names.txt không có dữ liệu.")

if len(students) < 100000:
    raise ValueError(
        f"Students.txt chỉ có {len(students)} dòng, chưa đủ 100000 dòng."
    )

# Tạo thông tin cho 100000 sinh viên
info = []

for line in students[:100000]:
    parts = line.split(",", 1)

    if len(parts) != 2:
        raise ValueError(f"Dòng Students.txt không hợp lệ: {line}")

    ma_sv, ma_lop = parts

    ngay_sinh = random.choice(dateborns)
    ho_ten = random.choice(names)

    info.append(f"{ma_sv},{ma_lop},{ho_ten},{ngay_sinh}")

# Ghi ra Info.txt
Path("data/Info.txt").write_text(
    "\n".join(info) + "\n",
    encoding="utf-8"
)

print(f"Đã tạo {len(info)} dòng trong Info.txt")