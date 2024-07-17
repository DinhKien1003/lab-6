import tkinter as tk

def start_scan():
    status_label.config(text="Scanning in progress...")

# Tạo cửa sổ
window = tk.Tk()
window.title("Scan Application")
window.geometry("800x500")
window.configure(background="#758694")

# Khung chính
main_frame = tk.Frame(window)
main_frame.pack(fill="both", expand=True)

# Thanh bên
sidebar_frame = tk.Frame(main_frame, width=200, bg="#ccc")
sidebar_frame.pack(side="left", fill="y")

status_label = tk.Label(sidebar_frame, text="Trạng thái", font=("Arial", 12), bg="#ccc")
status_label.pack(pady=20)

update_label = tk.Label(sidebar_frame, text="Cập nhật", font=("Arial", 12), bg="#ccc")
update_label.pack(pady=20)

setting_label = tk.Label(sidebar_frame, text="Cài đặt", font=("Arial", 12), bg="#ccc")
setting_label.pack(pady=20)

share_label = tk.Label(sidebar_frame, text="Chia sẻ phản hồi", font=("Arial", 12), bg="#ccc")
share_label.pack(pady=20)

help_label = tk.Label(sidebar_frame, text="Hỗ trợ", font=("Arial", 12), bg="#ccc")
help_label.pack(pady=20)

buy_label = tk.Label(sidebar_frame, text="Mua gói cao cấp", font=("Arial", 12), bg="#ccc")
buy_label.pack(pady=20)

scan_button = tk.Button(sidebar_frame, text="Quét ngay", command=start_scan , bg="#06D001")
scan_button.pack(pady=40)

# Khu vực chính
content_frame = tk.Frame(main_frame, bg="#fff")
content_frame.pack(side="right", fill="both", expand=True)

title_label = tk.Label(content_frame, text="Scan", font=("Arial", 24), bg="#fff")
title_label.pack(pady=20)

subtitle_label = tk.Label(content_frame, text="Premium will be free forever. You just need to click button", font=("Arial", 14), bg="#fff")
subtitle_label.pack(pady=10)

quick_scan_button = tk.Button(content_frame, text="Quét nhanh")
quick_scan_button.pack(pady=10)

web_protect_button = tk.Button(content_frame, text="Bảo vệ web")
web_protect_button.pack(pady=10)

# Nhãn trạng thái
status_label = tk.Label(content_frame, text="Trạng thái: Sẵn sàng", font=("Arial", 12), bg="#fff")
status_label.pack(pady=20)

# Chạy ứng dụng
window.mainloop()