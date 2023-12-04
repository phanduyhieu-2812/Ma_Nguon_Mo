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
def enhance_image():
    # Đọc ảnh từ đường dẫn
    img = image_data

    # Chuyển ảnh sang không gian màu LAB (L: độ sáng, A và B: các thành phần màu)
    lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)

    # Tách các thành phần màu
    l, a, b = cv2.split(lab)

    # Áp dụng cân bằng histogram cho kênh L (độ sáng)
    clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8, 8))
    cl = clahe.apply(l)

    # Gộp các kênh sau khi xử lý
    enhanced_lab = cv2.merge([cl, a, b])

    # Chuyển lại sang không gian màu BGR
    enhanced_img = cv2.cvtColor(enhanced_lab, cv2.COLOR_LAB2BGR)
    display_image(enhanced_img)
window=tk.Tk()
open_button= tk.Button(window,text="Mở ảnh ",command=open_image)
open_button.pack()

tachbien_button=tk.Button(window,text="Tăng cường sáng  ",command=enhance_image)
tachbien_button.pack()
image_label = tk.Label(window)
image_label.pack()
window.mainloop()
