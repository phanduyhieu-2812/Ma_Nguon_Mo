import sympy as sp
from tkinter import Tk, Label, Entry, Button

# Tạo ứng dụng


# Hàm vẽ hình
def draw_triangle(a, b, c):
  a = float(entry_a.get())
  b = float(entry_b.get())
  c = float(entry_c.get())
  """
  Vẽ hình tam giác với các cạnh a, b, c.

  Args:
    a: Chiều dài cạnh a.
    b: Chiều dài cạnh b.
    c: Chiều dài cạnh c.
  """

  # Tạo các điểm A, B, C
  A = sp.Point((0, 0))
  B = sp.Point((a, 0))
  C = sp.Point(sp.sqrt(a ** 2 - b ** 2), b)

  # Vẽ hình tam giác
  sp.plot((A, B, C, A), linestyle="--")

# Hàm tính chu vi
def perimeter_triangle(a, b, c):
  a = float(entry_a.get())
  b = float(entry_b.get())
  c = float(entry_c.get())
  """
  Tính chu vi tam giác với các cạnh a, b, c.

  Args:
    a: Chiều dài cạnh a.
    b: Chiều dài cạnh b.
    c: Chiều dài cạnh c.

  Returns:
    Chu vi tam giác.
  """

  return a + b + c

# Hàm giải bài tập
def solve_triangle(a, b, c):
  a = float(entry_a.get())
  b = float(entry_b.get())
  c = float(entry_c.get())
  """
  Giải bài tập hình học cho tam giác với các cạnh a, b, c.

  Args:
    a: Chiều dài cạnh a.
    b: Chiều dài cạnh b.
    c: Chiều dài cạnh c.

  Returns:
    Các giá trị của các góc trong tam giác.
  """

  # Tính các giá trị của các cạnh
  s = (a + b + c) / 2
  A = sp.arccos((b ** 2 + c ** 2 - a ** 2) / (2 * b * c))
  B = sp.arccos((a ** 2 + c ** 2 - b ** 2) / (2 * a * c))
  C = sp.arccos((a ** 2 + b ** 2 - c ** 2) / (2 * a * b))

  # Trả về các giá trị của các góc
  return A, B, C
app = Tk()

# Tạo nhãn
label_a = Label(app, text="Cạnh a:")
label_b = Label(app, text="Cạnh b:")
label_c = Label(app, text="Cạnh c:")

# Tạo ô nhập
entry_a = Entry(app)
entry_b = Entry(app)
entry_c = Entry(app)

# Tạo nút
button_draw = Button(app, text="Vẽ hình", command=draw_triangle)
button_perimeter = Button(app, text="Tính chu vi", command=perimeter_triangle)
button_solve = Button(app, text="Giải bài tập", command=solve_triangle)

# Sắp xếp các thành phần
label_a.grid(row=0, column=0)
entry_a.grid(row=0, column=1)
label_b.grid(row=1, column=0)
entry_b.grid(row=1, column=1)
label_c.grid(row=2, column=0)
entry_c.grid(row=2, column=1)
button_draw.grid(row=3, column=0)
button_perimeter.grid(row=3, column=1)
button_solve.grid(row=3, column=2)

# Chạy ứng dụng
app.mainloop()
