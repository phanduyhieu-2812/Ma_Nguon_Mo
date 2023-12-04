import pandas as pd
import numpy as np
import tensorflow as tf
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import tkinter as tk
from tkinter import ttk

def predict_grade():
    # Lấy dữ liệu từ các Entry
    hours_studied = float(hours_studied_entry.get())
    hours_slept = float(hours_slept_entry.get())
    hours_tv = float(hours_tv_entry.get())

    # Chuẩn hóa dữ liệu đầu vào
    input_data = scaler.transform([[hours_studied, hours_slept, hours_tv]])

    # Dự đoán hiệu quả học tập
    prediction = model.predict(input_data)

    # Hiển thị kết quả
    result_label.config(text=f'Predicted Grade: {prediction[0][0]:.2f}')

# Đọc dữ liệu từ file CSV
data = pd.read_csv('Student_Performance.csv')

# Xác định biến phụ thuộc (output) và biến độc lập (features)
X = data.drop('Grade', axis=1)
y = data['Grade']

# Chia dữ liệu thành tập huấn luyện và tập kiểm tra
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Chuẩn hóa dữ liệu
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Xây dựng mô hình hồi quy tuyến tính sử dụng TensorFlow
model = tf.keras.Sequential([
    tf.keras.layers.Input(shape=(X_train.shape[1],)),
    tf.keras.layers.Dense(1)
])

# Chọn hàm mất mát và tối ưu hóa
model.compile(optimizer='adam', loss='mean_squared_error')

# Huấn luyện mô hình
model.fit(X_train, y_train, epochs=100, batch_size=32, verbose=2)

# Tạo giao diện Tkinter
window = tk.Tk()
window.title("Student Performance Prediction")

# Tạo và thiết lập các widget trên giao diện
hours_studied_label = ttk.Label(window, text="Hours Studied:")
hours_studied_label.grid(row=0, column=0, padx=10, pady=10)

hours_studied_entry = ttk.Entry(window)
hours_studied_entry.grid(row=0, column=1, padx=10, pady=10)

hours_slept_label = ttk.Label(window, text="Hours Slept:")
hours_slept_label.grid(row=1, column=0, padx=10, pady=10)

hours_slept_entry = ttk.Entry(window)
hours_slept_entry.grid(row=1, column=1, padx=10, pady=10)

hours_tv_label = ttk.Label(window, text="Hours TV:")
hours_tv_label.grid(row=2, column=0, padx=10, pady=10)

hours_tv_entry = ttk.Entry(window)
hours_tv_entry.grid(row=2, column=1, padx=10, pady=10)

predict_button = ttk.Button(window, text="Predict Grade", command=predict_grade)
predict_button.grid(row=3, column=0, columnspan=2, pady=10)

result_label = ttk.Label(window, text="Predicted Grade: ")
result_label.grid(row=4, column=0, columnspan=2, pady=10)

window.mainloop()
