so_gio_lam = float(input("Nhập số giờ làm mỗi ngày: "))
luong_gio = float(input("Nhập lương làm mỗi giơ: "))
gio_tieu_chuan = 44
gio_vuot_chuan = max(0,so_gio_lam - gio_tieu_chuan)
thuc_linh = gio_tieu_chuan * luong_gio + gio_vuot_chuan * luong_gio * 1.5
print(f"Số tiền thực lĩnh của nhân viên: {thuc_linh}")