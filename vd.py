import pandas
import numpy as np 
import pandas as pd

# Đường dẫn đến file Excel
path=('data.csv')
# Đọc file Excel
df = pd.read_csv(path)
data=np.array(df)
print(df)
dlm=[]
kc=[]
for i in range(2):
  gt=float(input("moi nhap du lieu moi : "))
  dlm.append(gt)
dlm=np.array(dlm)
print("du lieu moi : ",dlm)
def khoang_cach(x,y):
  return np.power(x[0]-y[0],2)+np.power(x[1]-y[1],2)
datat=data[:,:2]
n=len(datat)
dataout=data[:,-1]
for i in range(n):  
    kc.append(khoang_cach(dlm,datat[i]))

for i in range(0,n-1):
  for j in range(i+1,n):
    if(kc[i]>kc[j]):
      tmp=kc[i]
      kc[i]=kc[j]
      kc[j]=tmp 
print('khoang cach sau khi sap xep: ',kc)
dataout=np.where(dataout == 'kim_loai',1,0)
print(dataout)
      

