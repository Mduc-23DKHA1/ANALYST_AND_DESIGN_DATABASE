Thứ tự ưu tiên: 
1. [Lop,] NhaXuatBan, TheLoai, NoiQuyPhat
2. SinhVien, Sach, TheThuVien, PhieuMuon, PhieuGiaHan
3. BanSaoSach, ChiTietGiaHan, ChiTietPhieuMuon
4. PhieuTra
5. ChiTietPhieuTra
6. PhieuPhat
7. ChiTietPhat

## Prior 1)
- Lop(**MaLop**, TenLop)
- NhaXuatBan(**MaNXB**, TenNXB)
- TheLoai(**MaTL**, TenTL)
- NoiQuyPhat(**MaNQP**, MucPhat, TenViPham)

## Prior 2)
- SinhVien(**MaSV**, Lop, HoTen, NgaySinh)
- Sach(**MaS**, TenSach, SoLuong, #MaTL, #MaNXB)
- TheThuVien(**MaSV**, NgayLap, NgayHetHan)
- PhieuGiaHan(**MaPGH**, NamHoc, NgayGiaHan, NgayHetHanMoi)
- PhieuMuon(**MaPM**, NgayHenTra, NgayMuon, #MaSV)

## Prior 3)
- BanSaoSach(**MaVach**, #MaS)
- ChiTietGiaHan(**#MaPGH**, **#MaSV**, NgayDongTien, PhiGiaHan)
- ChiTietPhieuMuon(**#MaPM**, **#MaVach**, TinhTrang)

## Prior 4)
- PhieuTra(**MaPT**, NgayTiepNhan)

## Prior 5)
- ChiTietPhieuTra(**#MaPM**, **#MaVach**, **#MaPT**, TinhTrang)

## Prior 6)
- PhieuPhat(**MaPP**, NgayLap, TongThanhToan, NgayThanhToan, #MaPT)

## Prior 7)
- ChiTietPhat(**#MaNQP**, **#MaPP**, **#MaVach**)