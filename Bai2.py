from sympy import symbols, diff, integrate, sympify
import tkinter as tk
def compute_derivative():
    expression = entry_expression.get()
    try:
        x = symbols('x')
        f = sympify(expression)
        derivative = diff(f, x)
        result = str(derivative)
        text_result.delete(1.0, tk.END)  # Xóa nội dung cũ trong ô văn bản
        text_result.insert(tk.END, "Đạo hàm của {} là:\n{}".format(expression, result))
    except:
        text_result.delete(1.0, tk.END)  # Xóa nội dung cũ trong ô văn bản
        text_result.insert(tk.END, "Lỗi: Không thể tính đạo hàm. Vui lòng kiểm tra lại biểu thức.")

def compute_integral():
    expression = entry_expression.get()
    try:
        x = symbols('x')
        f = sympify(expression)
        integral = integrate(f, x)
        result = str(integral)
        text_result.delete(1.0, tk.END)  # Xóa nội dung cũ trong ô văn bản
        text_result.insert(tk.END, "Nguyên hàm của {} là:\n{}".format(expression, result))
    except:
        text_result.delete(1.0, tk.END)  # Xóa nội dung cũ trong ô văn bản
        text_result.insert(tk.END, "Lỗi: Không thể tính nguyên hàm. Vui lòng kiểm tra lại biểu thức.")

# Tạo cửa sổ giao diện
window = tk.Tk()
window.title("Tính đạo hàm và nguyên hàm")
window.geometry("400x300")

# Tạo các thành phần giao diện
label_expression = tk.Label(window, text="Nhập biểu thức:")
label_expression.pack()

entry_expression = tk.Entry(window, width=30)
entry_expression.pack()

button_derivative = tk.Button(window, text="Tính đạo hàm", command=compute_derivative)
button_derivative.pack()

button_integral = tk.Button(window, text="Tính nguyên hàm", command=compute_integral)
button_integral.pack()

label_result = tk.Label(window, text="Kết quả:")
label_result.pack()

text_result = tk.Text(window, height=5, width=30)
text_result.pack()

# Chạy vòng lặp chính của giao diện người dùng
window.mainloop()