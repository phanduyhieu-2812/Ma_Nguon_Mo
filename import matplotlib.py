from tkinter import Tk, Label, Entry, Button
from sympy import symbols, fourier_transform, correlate, z_transform, hankel_transform

def compute_fourier():
    x = input_entry.get()
    t, w = symbols('t w')
    X = fourier_transform(x, t, w)
    result_label.config(text="Result: " + str(X))

def compute_correlation():
    x = input1_entry.get()
    y = input2_entry.get()
    n = symbols('n')
    correlation = correlate(x, y, n)
    result_label.config(text="Result: " + str(correlation))

def compute_ztransform():
    x = input_entry.get()
    n, z = symbols('n z')
    X = z_transform(x, n, z)
    result_label.config(text="Result: " + str(X))

def compute_hankeltransform():
    f = input_entry.get()
    r, k = symbols('r k')
    F = hankel_transform(f, r, k)
    result_label.config(text="Result: " + str(F))

# Tạo cửa sổ giao diện
window = Tk()
window.title("SymPy Signal Processing")

# Tạo nhãn và ô nhập liệu cho Fourier Transform
fourier_label = Label(window, text="Fourier Transform")
fourier_label.pack()
input_label = Label(window, text="Input:")
input_label.pack()
input_entry = Entry(window)
input_entry.pack()
fourier_button = Button(window, text="Compute", command=compute_fourier)
fourier_button.pack()

# Tạo nhãn và ô nhập liệu cho Correlation
correlation_label = Label(window, text="Correlation")
correlation_label.pack()
input1_label = Label(window, text="Input 1:")
input1_label.pack()
input1_entry = Entry(window)
input1_entry.pack()
input2_label = Label(window, text="Input 2:")
input2_label.pack()
input2_entry = Entry(window)
input2_entry.pack()
correlation_button = Button(window, text="Compute", command=compute_correlation)
correlation_button.pack()

# Tạo nhãn và ô nhập liệu cho Z Transform
ztransform_label = Label(window, text="Z Transform")
ztransform_label.pack()
input_label = Label(window, text="Input:")
input_label.pack()
input_entry = Entry(window)
input_entry.pack()
ztransform_button = Button(window, text="Compute", command=compute_ztransform)
ztransform_button.pack()

# Tạo nhãn và ô nhập liệu cho Hankel Transform
hankeltransform_label = Label(window, text="Hankel Transform")
hankeltransform_label.pack()
input_label = Label(window, text="Input:")
input_label.pack()
input_entry = Entry(window)
input_entry.pack()
hankeltransform_button = Button(window, text="Compute", command=compute_hankeltransform)
hankeltransform_button.pack()

# Hiển thị kết quả
result_label = Label(window, text="")
result_label.pack()

# Chạy giao diện
window.mainloop()