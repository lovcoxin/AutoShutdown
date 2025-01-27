import os
import threading
from tkinter import messagebox
import chardet

# 表示是否关机
flag = False
file_path = "message.txt"

def task_to_run(flag=False):
    if not flag:
        timer.cancel()
        exit()
    elif flag:
        os.system("shutdown /s /t 1")
        timer.cancel()
        exit()

if __name__ == '__main__':
    message = "将在10秒后自动关机，是否立即执行？"

    if os.path.exists(file_path):
        with open(file_path, "rb") as f:
            raw_data = f.read()
            result = chardet.detect(raw_data)
            encoding = result['encoding']
        try:
            with open(file_path, "r", encoding=encoding) as f:
                message = f.read()
        except UnicodeDecodeError:
            messagebox.showerror("错误", f"无法使用检测到的编码({encoding})读取文件，请检查文件编码格式")
            exit()

    # 创建一个threading.Timer，设置10秒间隔，所执行的任务会在10秒后执行
    timer = threading.Timer(10.0, task_to_run)
    # 启动timer
    timer.start()

    # 打开一个TK的消息框，用变量res接收返回值（bool类型，因为用是askyesno函数）
    task_to_run(flag=messagebox.askyesno("自动关机", message))