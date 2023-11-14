from sympy import Point, Polygon,N
import tkinter as tk
import matplotlib.pyplot as plt
def vetamgiac():
    Ax_value = float(Ax_entry.get())
    Ay_value = float(Ay_entry.get())
    Bx_value = float(Bx_entry.get())
    By_value = float(By_entry.get())
    Cx_value = float(Cx_entry.get())
    Cy_value = float(Cy_entry.get())

    A = Point(Ax_value, Ay_value)
    B = Point(Bx_value, By_value)
    C = Point(Cx_value, Cy_value)

    tamgiac = Polygon(A, B, C)

    x_coords = [A.x, B.x, C.x, A.x]
    y_coords = [A.y, B.y, C.y, A.y]

    # Vẽ tam giác
    plt.plot(x_coords, y_coords)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Tam giác')
    plt.grid(True)
    plt.show()
def chuvi():
    Ax_value = float(Ax_entry.get())
    Ay_value = float(Ay_entry.get())
    Bx_value = float(Bx_entry.get())
    By_value = float(By_entry.get())
    Cx_value = float(Cx_entry.get())
    Cy_value = float(Cy_entry.get())

    A = Point(Ax_value, Ay_value)
    B = Point(Bx_value, By_value)
    C = Point(Cx_value, Cy_value)
    AB=A.distance(B)
    AC=A.distance(C)
    BC=B.distance(C)
    chu_vi =AB+AC+BC
    chu_vi=N(chu_vi)
    text_result.delete(1.0, tk.END)  # Xóa nội dung cũ trong ô văn bản
    text_result.insert(tk.END, "Chu vi của tam giác  là:\n{}".format(chu_vi))
def dientich():
    Ax_value = float(Ax_entry.get())
    Ay_value = float(Ay_entry.get())
    Bx_value = float(Bx_entry.get())
    By_value = float(By_entry.get())
    Cx_value = float(Cx_entry.get())
    Cy_value = float(Cy_entry.get())

    A = Point(Ax_value, Ay_value)
    B = Point(Bx_value, By_value)
    C = Point(Cx_value, Cy_value)
    tamgiac = Polygon(A, B, C)
    dien_tich = tamgiac.area
    dien_tich=N(dien_tich)
    text_result.delete(1.0, tk.END)  # Xóa nội dung cũ trong ô văn bản
    text_result.insert(tk.END, "Diện của tam giác  là:\n{}".format(dien_tich))

window = tk.Tk()
window.title("Tính toán tam giác từ các điểm trong không gian ")
window.geometry("500x500")

label_a = tk.Label(window, text="Cạnh a:")
label_b = tk.Label(window, text="Cạnh b:")
label_c = tk.Label(window, text="Cạnh c:")
label_result = tk.Label(window, text="Kết quả:")
text_result = tk.Text(window, height=5, width=30)

Ax_entry = tk.Entry(window, width=10)
Ay_entry = tk.Entry(window, width=10)
Bx_entry = tk.Entry(window, width=10)
By_entry = tk.Entry(window, width=10)
Cx_entry = tk.Entry(window, width=10)
Cy_entry = tk.Entry(window, width=10)

button_ve = tk.Button(window, text="Vẽ tam giác", command=vetamgiac)
button_chui=tk.Button(window,text="tính chu vi tam giác",command=chuvi)
button_dientich=tk.Button(window,text="tính diện tích tam giác ",command=dientich)
label_a.grid(row=0, column=0)
Ax_entry.grid(row=0, column=1)
Ay_entry.grid(row=0, column=2)

label_b.grid(row=1, column=0)
Bx_entry.grid(row=1, column=1)
By_entry.grid(row=1, column=2)

label_c.grid(row=2, column=0)
Cx_entry.grid(row=2, column=1)
Cy_entry.grid(row=2, column=2)

button_ve.grid(row=3, column=0)
button_chui.grid(row=4,column=0)
button_dientich.grid(row=4,column=1)
label_result.grid(row=5)
text_result.grid(row=6)
window.mainloop()