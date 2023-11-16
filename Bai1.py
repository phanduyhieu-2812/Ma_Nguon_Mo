import numpy as np
import tkinter as tk

def giai_he_phuong_trinh(A, B):
    # Tìm số ẩn trong hệ phương trình
    n = len(A)

    # Tạo ma trận mở rộng bằng cách nối ma trận A và ma trận B
    AB = np.column_stack((A, B))

    # Sử dụng hàm solve của NumPy để giải hệ phương trình
    giai = np.linalg.solve(AB[:, :-1], AB[:, -1])

    return giai

def giai_phuong_trinh():
    # Lấy giá trị n từ ô nhập
    global n
    n = int(n_input.get())

    # Lấy các hệ số của phương trình từ ô nhập
    A = []
    B = []
    for i in range(n):
        row = []
        for j in range(n):
            coefficient = float(A_entries[i][j].get())
            row.append(coefficient)
        A.append(row)
        b = float(B_entries[i].get())
        B.append(b)

    # Chuyển đổi A và B thành mảng NumPy
    A = np.array(A)
    B = np.array(B)

    # Gọi hàm giải hệ phương trình
    ket_qua = giai_he_phuong_trinh(A, B)

    # Hiển thị kết quả lên ô hiển thị
    
    ket_qua_text.configure(state='normal')
    ket_qua_text.delete('1.0', tk.END)
    ket_qua_text.insert(tk.END, "Kết quả 1: " + str(ket_qua[0]) + "\n")
    ket_qua_text.insert(tk.END, "Kết quả 2: " + str(ket_qua[1]))
    ket_qua_text.configure(state='disabled')

# Tạo cửa sổ giao diện
window = tk.Tk()
window.title("Ứng dụng giải hệ phương trình")
window.geometry("500x500")

# Tạo các thành phần giao diện
n_label = tk.Label(window, text="Nhập số ẩn n:")
n_label.pack()

n_input = tk.Entry(window)
n_input.pack()

A_label = tk.Label(window, text="Nhập ma trận hệ số A:")
A_label.pack()

A_entries = []
B_entries = []

def create_entries():
    global A_entries
    A_entries = []
    for i in range(n):
        row_entries = []
        for j in range(n):
            entry = tk.Entry(window)
            entry.pack()
            row_entries.append(entry)
        A_entries.append(row_entries)

def create_b_entries():
    global B_entries
    B_entries = []
    for i in range(n):
        entry = tk.Entry(window)
        entry.pack()
        B_entries.append(entry)

def reset_entries():
    for entry_row in A_entries:
        for entry in entry_row:
            entry.destroy()
    A_entries.clear()

    for entry in B_entries:
        entry.destroy()
    B_entries.clear()

def create_and_reset_entries():
    reset_entries()
    create_entries()
    create_b_entries()

def giai_phuong_trinh_wrapper():
    giai_phuong_trinh()

create_and_reset_button = tk.Button(window, text="Tạo lại", command=create_and_reset_entries)
create_and_reset_button.pack()

tinh_button = tk.Button(window, text="Tính", command=giai_phuong_trinh_wrapper)
tinh_button.pack()

ket_qua_label = tk.Label(window, text="Kết quả:")
ket_qua_label.pack()

ket_qua_text = tk.Text(window, height=5, width=30, state='disabled')
ket_qua_text.pack()

# Chạy ứng dụng
window.mainloop()