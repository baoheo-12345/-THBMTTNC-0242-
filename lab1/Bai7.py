print("Nhập các dòng văn bản")
lines = []
while True:
    line = input()
    if line.lower() == 'done':
        break
    lines.append(line)
print("các dòng sau khi nhập chuyển thành in hoa ")
for line in lines:
    print(line.upper())