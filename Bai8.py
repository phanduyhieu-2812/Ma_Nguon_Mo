import tkinter as tk 
from tkinter import filedialog
import cv2 
from PIL import Image,ImageTk

def open_image():
    file_path = filedialog.askopenfilename()
    image= cv2.imread(file_path)
    if image is not  None :
        global image_data
        image_data = image
        display_image(image_data)
    else:
        print('Failed to open image ')
def display_image(image):
    image_pill = Image.fromarray(cv2.cvtColor(image,cv2.COLOR_BGR2RGB))

    image_tk = ImageTk.PhotoImage(image_pill)
    image_label.configure(image=image_tk)
    image_label.image = image_tk
def tachbien():
    if image_data is not None:
        gray = cv2.cvtColor(image_data, cv2.COLOR_BGR2GRAY)

# Áp dụng Gaussian Blur để làm mờ ảnh và giảm nhiễu
        blur = cv2.GaussianBlur(gray, (5, 5), 0)

# Sử dụng phương pháp Canny để phát hiện biên
        edges = cv2.Canny(blur, 50, 150)
        display_image(edges)
    else:
        print('No image selceted')
def resize():
    A_value=int(A.get())
    B_value=int(B.get())
    if image_data is not None:
        resize_image = cv2.resize(image_data,(A_value,B_value))
        display_image(resize_image)
    else:
        print('No image selected.')


window=tk.Tk()

open_button= tk.Button(window,text="Mở ảnh ",command=open_image)
open_button.pack()

tachbien_button=tk.Button(window,text="Tách biên ảnh ",command=tachbien)
tachbien_button.pack()

resize_button = tk.Button(window,text="Đổi kích thước",command=resize)
resize_button.pack()

A=tk.Entry(window,width=10)
B=tk.Entry(window,width=10)
A.pack()
B.pack()

image_label = tk.Label(window)
image_label.pack()
window.mainloop()


