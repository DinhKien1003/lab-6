import tkinter as tk

def start_recording():
    status_label.config(text="Recording started")

def pause_recording():
    status_label.config(text="Recording paused")

def stop_recording():
    status_label.config(text="Recording stopped")

# Tạo cửa sổ
window = tk.Tk()
window.title("Frame Recorder")
window.geometry("600x300")
window.configure(background="#f0f0f0")

# Tiêu đề
title_label = tk.Label(window, text="Frame Recorder", font=("Arial", 24))
title_label.pack(pady=20)

# Đầu vào FPS
fps_label = tk.Label(window, text="FPS (Frames per Second):")
fps_label.pack()

fps_entry = tk.Entry(window)
fps_entry.pack(pady=10)

# Nút
button_frame = tk.Frame(window)
button_frame.pack()

start_button = tk.Button(button_frame, text="Start", command=start_recording)
start_button.pack(side="left")

pause_button = tk.Button(button_frame, text="Pause", command=pause_recording)
pause_button.pack(side="left")

stop_button = tk.Button(button_frame, text="Stop", command=stop_recording)
stop_button.pack(side="left")

# Nhãn trạng thái
status_label = tk.Label(window, text="Status: Ready")
status_label.pack(pady=20)

# Chạy ứng dụng
window.mainloop()