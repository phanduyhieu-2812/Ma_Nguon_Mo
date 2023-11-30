import tkinter as tk
from tkinter import filedialog
import cv2
from PIL import Image, ImageTk
def open_image():
    # Mở hộp thoại lựa chọn tệp tin
    file_path = filedialog.askopenfilename()
    
    # Đọc ảnh bằng OpenCV
    image = cv2.imread(file_path)
    
    if image is not None:
        # Lưu trữ dữ liệu ảnh
        global image_data
        image_data = image
        
        # Hiển thị ảnh gốc
        display_image(image_data)
    else:
        print("Failed to open image.")  

def apply_gaussian():
    if image_data is not None:
        # Áp dụng Gaussian Blur với kernel size là (5, 5)
        blurred_image = cv2.GaussianBlur(image_data, (5, 5), 0)
        
        # Hiển thị ảnh đã được làm mịn
        display_image(blurred_image)
    else:
        print("No image selected.")

def resize_image():
    if image_data is not None:
        # Thay đổi kích thước ảnh thành (300, 300)
        resized_image = cv2.resize(image_data, (500, 500))
        
        # Hiển thị ảnh đã được thay đổi kích thước
        display_image(resized_image)
    else:
        print("No image selected.")
def median_blur():
    if image_data is not None:
        median_image = cv2.medianBlur(image_data, 5)
        display_image(median_image)
    else:
        print("No image selected")
def bilateral():
    if image_data is not None:
        bilateral_image = cv2.bilateralFilter(image_data, 9, 75, 75)
        display_image(bilateral_image)
    else:
        print("No image selected")
def soble():
    if image_data is not None:
        edges = cv2.Sobel(image_data, cv2.CV_64F, 1, 0)
        display_image(edges)

def display_image(image):
    # Chuyển đổi ảnh từ OpenCV sang định dạng PIL
    image_pil = Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2RGB)) 
    
    # Hiển thị ảnh trong cửa sổ
    image_tk = ImageTk.PhotoImage(image_pil)
    image_label.configure(image=image_tk)
    image_label.image = image_tk

# Tạo cửa sổ giao diện
window = tk.Tk()

# Tạo nút mở ảnh
open_button = tk.Button(window, text="Mở ảnh", command=open_image)
open_button.pack()

# Tạo nút áp dụng Gaussian Blur
gaussian_button = tk.Button(window, text="Áp dụng Gaussian Blur", command=apply_gaussian)
gaussian_button.pack()

# Tạo nút thay đổi kích thước ảnh
resize_button = tk.Button(window, text="Thay đổi kích thước ảnh", command=resize_image)
resize_button.pack()

median_button=tk.Button(window,text='Bộ lọc median',command=median_blur)
median_button.pack()

bilateral_button=tk.Button(window,text="LÀm mờ song song ",command=bilateral)
bilateral_button.pack()

soble_button=tk.Button(window,text="Phát hiện biên bằng phép tích chập",command=soble)
soble_button.pack()
# Tạo nhãn để hiển thị ảnh
image_label = tk.Label(window)
image_label.pack()

# Biến lưu trữ dữ liệu ảnh
image_data = None

# Khởi chạy vòng lặp chính của giao diện
window.mainloop()