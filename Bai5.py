import pandas as pd
import numpy as np
import math
data_frame=pd.read_csv('Student_Performance (1).csv')
data=np.array(data_frame)
Gio_hoc=data[:,:1]
Diem=data[:,1]
Ngoai_Khoa=data[:,2]
Gio_Ngu=data[:,3]
Diem_Moi=data[:,5]
Gio_hoc_cao=[]
Gio_Ngu_cao=[]
Diem_cao=[]
Diem_dat=[]
Sinh_Vien_Tien_Bo=[]
Gio_hoc_TB=np.mean(Gio_hoc)
for i in range(len(Gio_hoc)):
  if Gio_hoc[i]== np.max(Gio_hoc): Gio_hoc_cao.append(i)
ti_le_gio_hoc_cao=(len(Gio_hoc_cao)/len(Gio_hoc))*100
for i in range(len(Diem)):
  if Diem[i]==np.max(Diem): Diem_cao.append(i)
hoc_sinh_hieu_qua=np.intersect1d(Gio_hoc_cao,Diem_cao)
for i in range(len(Diem)):
  if Diem[i]>=50: Diem_dat.append(i)
Phan_tram_hoc_sinh_dat=(len(Diem_dat)/len(Diem))*100
for i in range(len(Gio_Ngu)):
  if Gio_Ngu[i]==np.min(Gio_Ngu):
    Gio_hoc_cao.append(i)
hoc_sinh_luoi=np.intersect1d(Gio_Ngu_cao,Gio_hoc_cao)
for i in range(len(Diem)):
  if Diem[i]<=Diem_Moi[i]: Sinh_Vien_Tien_Bo.append(i)
print('Tỉ lệ phần trăm sinh viên có giờ học cao nhất : ',ti_le_gio_hoc_cao,'%')
print('Các sinh viên hcoj tập hiệu quả(Giờ học cao và điểm cao): ',hoc_sinh_hieu_qua)
print('Tỉ lệ các sinh viên đạt bài kiểm tra thường xuyên 1 : ',Phan_tram_hoc_sinh_dat,'%')
print('Các sinh viên lười học(Giờ học thấp và Giờ Ngủ cao : )',hoc_sinh_luoi)
print('Các sinh viên tiến bộ trong kì kiểm tra : ',Sinh_Vien_Tien_Bo)




