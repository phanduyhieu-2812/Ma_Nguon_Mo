# ý tưởng thiết kế : tạo 1 giao diện có 1 ô  cho phép nhập 1 dãy số và thực hiện các chức năng :
#tìm số lớn nhất , tìm số nhỏ nhất , sắp xếp từ lớn đến bé , sắp xếp từ bé đến lớn , tìm số tring bình , tìm số trung vị , kiểm tra âm dương 
#1 ô nhập ngôn ngữ và hiển thị thông tin ngôn ngữ đó 
#đọc 1 file csv từ bộ nhớ máy tính cá nhân và hiển thị 
print('Maximum of 4,12,43.3,1 and 100 is : ',end="")
print(max(4,12,53,3,19,100))
print(min(4,12,43.3,19.100))
list1=['java','python','c++','php','sql']
list2=[4,2,8,10,6]
list1.sort()
list2.sort()
print("list 1 được sắp xếp : ",list1)
print("list 2 được sắp xếp : ",list2)
import numpy as np 
import tkinter as tk
from tkinter import filedialog
import csv
from tkinter import ttk
from tkinter import messagebox

class NumberOperations:
    def __init__(self, root):
        self.root = root
        self.root.title("Number Operations")

        self.create_widgets()

    def create_widgets(self):
        # Nhập dãy số
        self.label = tk.Label(self.root, text="Nhập dãy số (cách nhau bằng dấu phẩy):")
        self.label.pack(pady=10)

        

        self.number_entry = tk.Entry(self.root)
        self.number_entry.pack(pady=10)

         # Nhập dãy số
        self.label = tk.Label(self.root, text="Nhập ngôn ngữ lập trình ")
        self.label.pack(pady=10)

        # Ô nhập ngôn ngữ lập trình
        self.language_entry = tk.Entry(self.root)
        self.language_entry.pack(pady=10)

        # Widget Text để hiển thị kết quả
        self.result_text = tk.Text(self.root, height=10, width=50)
        self.result_text.pack(pady=10)

        # Nút tìm số lớn nhất
        self.max_button = tk.Button(self.root, text="Tìm số lớn nhất", command=self.find_max)
        self.max_button.pack()

        # Nút tìm số nhỏ nhất
        self.min_button = tk.Button(self.root, text="Tìm số nhỏ nhất", command=self.find_min)
        self.min_button.pack()

        # Nút tính trung bình
        self.avg_button = tk.Button(self.root, text="Tính trung bình", command=self.calculate_average)
        self.avg_button.pack()

        # Nút tìm số trung vị
        self.median_button = tk.Button(self.root, text="Tìm số trung vị", command=self.find_median)
        self.median_button.pack()

        # Nút sắp xếp từ nhỏ đến lớn
        self.sort_asc_button = tk.Button(self.root, text="Sắp xếp từ nhỏ đến lớn", command=self.sort_ascending)
        self.sort_asc_button.pack()

        # Nút sắp xếp từ lớn đến nhỏ
        self.sort_desc_button = tk.Button(self.root, text="Sắp xếp từ lớn đến nhỏ", command=self.sort_descending)
        self.sort_desc_button.pack()

        # Nút kiểm tra số âm hay số dương
        self.check_negative_button = tk.Button(self.root, text="Kiểm tra số âm/số dương", command=self.check_negative_positive)
        self.check_negative_button.pack()

           # Nút hiển thị thông tin ngôn ngữ lập trình
        self.show_info_button = tk.Button(self.root, text="Hiển thị thông tin của ngôn ngữ đã chọn", command=self.show_language_info)
        self.show_info_button.pack()

        # Nút mở file CSV và hiển thị trên treeview
        self.load_csv_button = tk.Button(self.root, text="Mở file CSV", command=self.load_csv_to_treeview)
        self.load_csv_button.pack()

        # Treeview để hiển thị dữ liệu từ file CSV
        self.csv_treeview = ttk.Treeview(self.root)
        self.csv_treeview.pack(pady=10)



     

    def find_max(self):
        numbers = self.get_numbers()
        if numbers:
            max_number = max(numbers)
            self.display_result(f"Số lớn nhất là: {max_number}")

    def find_min(self):
        numbers = self.get_numbers()
        if numbers:
            min_number = min(numbers)
            self.display_result(f"Số nhỏ nhất là: {min_number}")

    def calculate_average(self):
        numbers = self.get_numbers()
        if numbers:
            avg = sum(numbers) / len(numbers)
            self.display_result(f"Trung bình của dãy số là: {avg:.2f}")

    def find_median(self):
        numbers = self.get_numbers()
        if numbers:
            sorted_numbers = sorted(numbers)
            n = len(sorted_numbers)
            if n % 2 == 0:
                median = (sorted_numbers[n//2 - 1] + sorted_numbers[n//2]) / 2
            else:
                median = sorted_numbers[n//2]
            self.display_result(f"Số trung vị của dãy số là: {median}")

    def sort_ascending(self):
        numbers = self.get_numbers()
        if numbers:
            sorted_numbers = sorted(numbers)
            self.display_result(f"Sắp xếp từ nhỏ đến lớn: {sorted_numbers}")

    def sort_descending(self):
        numbers = self.get_numbers()
        if numbers:
            sorted_numbers = sorted(numbers, reverse=True)
            self.display_result(f"Sắp xếp từ lớn đến nhỏ: {sorted_numbers}")

    def check_negative_positive(self):
        numbers = self.get_numbers()
        result = []
        for num in numbers:
            if num > 0:
                result.append(f"{num} là số dương")
            elif num < 0:
                result.append(f"{num} là số âm")
            else:
                result.append(f"{num} là số không âm cũng không dương")
        self.display_result("\n".join(result))

    def load_csv_to_treeview(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if file_path:
            self.load_csv_to_treeview_helper(file_path)

    def load_csv_to_treeview_helper(self, file_path):
        # Xóa dữ liệu hiện tại trên treeview
        for item in self.csv_treeview.get_children():
            self.csv_treeview.delete(item)

        # Đọc dữ liệu từ file CSV và thêm vào treeview
        with open(file_path, "r", newline="", encoding="utf-8") as csvfile:
            csv_reader = csv.reader(csvfile)
            header = next(csv_reader)

            self.csv_treeview["columns"] = header
            for col in header:
                self.csv_treeview.column(col, width=100)
                self.csv_treeview.heading(col, text=col)  # Thêm heading vào treeview

            for idx, row in enumerate(csv_reader):
                self.csv_treeview.insert("", idx, values=row)

    def get_numbers(self):
        try:
            numbers = [float(x.strip()) for x in self.number_entry.get().split(",")]
            return numbers
        except ValueError:
            messagebox.showerror("Lỗi", "Vui lòng nhập dãy số hợp lệ.")
            return []

    def display_result(self, result):
        self.result_text.delete(1.0, tk.END)  # Xóa nội dung cũ
        self.result_text.insert(tk.END, result)

    def show_language_info(self):
        language = self.language_entry.get().lower()
        info = self.get_language_info(language)
        self.display_result(info)

    def get_language_info(self, language):
        languages_info = {
            'java': 'Java (phiên âm Tiếng Việt: "Gia-va") là một ngôn ngữ lập trình hướng đối tượng, dựa trên lớp được thiết kế để có càng ít phụ thuộc thực thi càng tốt. Nó là ngôn ngữ lập trình có mục đích chung cho phép các nhà phát triển ứng dụng viết một lần, chạy ở mọi nơi (WORA),[9] nghĩa là mã Java đã biên dịch có thể chạy trên tất cả các nền tảng hỗ trợ Java mà không cần biên dịch lại.[10] Các ứng dụng Java thường được biên dịch thành bytecode có thể chạy trên bất kỳ máy ảo Java (JVM) nào bất kể kiến trúc máy tính bên dưới.',
            'python': 'Python (phát âm tiếng Anh: /ˈpaɪθɑːn/) là một ngôn ngữ lập trình bậc cao cho các mục đích lập trình đa năng, do Guido van Rossum tạo ra và lần đầu ra mắt vào năm 1991. Python được thiết kế với ưu điểm mạnh là dễ đọc, dễ học và dễ nhớ. Python là ngôn ngữ có hình thức rất sáng sủa, cấu trúc rõ ràng, thuận tiện cho người mới học lập trình và là ngôn ngữ lập trình dễ học; được dùng rộng rãi trong phát triển trí tuệ nhân tạo.',
            'c++': 'C++ (C Plus Plus, CPP, IPA: /siː pləs pləs/) là một ngôn ngữ lập trình bậc cao (high-level). Đây là ngôn ngữ lập trình đa năng được tạo ra bởi Bjarne Stroustrup như một phần mở rộng của ngôn ngữ lập trình C, hoặc "C với các Class", Ngôn ngữ đã được mở rộng đáng kể theo thời gian và C ++ hiện đại có các tính năng: lập trình tổng quát, lập trình hướng đối tượng, lập trình thủ tục, ngôn ngữ đa mẫu hình tự do có kiểu tĩnh, dữ liệu trừu tượng, và lập trình đa hình, ngoài ra còn có thêm các tính năng, công cụ để thao tác với bộ nhớ cấp thấp.',
            'php': 'PHP: Hypertext Preprocessor, thường được viết tắt thành PHP là một ngôn ngữ lập trình kịch bản hay một loại mã lệnh chủ yếu được dùng để phát triển các ứng dụng viết cho máy chủ, mã nguồn mở, dùng cho mục đích tổng quát',
            'sql': 'SQL là Ngôn ngữ truy vấn mang tính cấu trúc, là một loại ngôn ngữ máy tính phổ biến để tạo, sửa, và lấy dữ liệu từ một hệ quản trị cơ sở dữ liệu quan hệ. Ngôn ngữ này phát triển vượt xa so với mục đích ban đầu là để phục vụ các hệ quản trị cơ sở dữ liệu đối tượng-quan hệ. Nó là một tiêu chuẩn ANSI/ISO.'
        }

        return languages_info.get(language, f'Không có thông tin cho ngôn ngữ  {language}')

if __name__ == "__main__":
    root = tk.Tk()
    app = NumberOperations(root)
    root.mainloop()
