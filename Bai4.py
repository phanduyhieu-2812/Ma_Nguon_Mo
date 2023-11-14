import tkinter as tk
import sympy as sp

def calculate_fourier_transform():
    # Lấy giá trị từ ô nhập liệu
    expression = entry.get()

    # Tạo một biến ký hiệu
    t = sp.symbols('t')

    try:
        # Biểu diễn tín hiệu số từ biểu thức nhập vào
        signal = sp.sympify(expression)

        # Tính biến đổi Fourier cho tín hiệu số
        fourier_transform = sp.fourier_transform(signal, t, sp.symbols('f'))

        # Hiển thị kết quả lên giao diện
        result_label.configure(text=str(fourier_transform))

    except sp.SympifyError:
        result_label.configure(text="Error: Invalid expression")

# Tạo một cửa sổ giao diện
window = tk.Tk()
window.title("Xử lý tín hiệu số")

# Tạo một nhãn và ô nhập liệu
expression_label = tk.Label(window, text="Nhập biểu thức tín hiệu số:")
expression_label.pack()
entry = tk.Entry(window)
entry.pack()

# Tạo nút tính toán và đặt một hành động cho nó
calculate_button = tk.Button(window, text="Tính biến đổi Fourier", command=calculate_fourier_transform)
calculate_button.pack()

# Tạo một nhãn hiển thị kết quả
result_label = tk.Label(window, text="")
result_label.pack()

# Khởi chạy vòng lặp sự kiện chính
window.mainloop()
