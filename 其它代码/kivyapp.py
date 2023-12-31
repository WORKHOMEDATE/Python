import tkinter as tk

def greet():
    name = entry.get()
    greeting = "Hello, " + name + "!"
    label.config(text=greeting)

# 创建主窗口
window = tk.Tk()
window.title("个性化应用")
window.geometry("300x200")

# 创建标签和输入框
label = tk.Label(window, text="请输入您的名字：")
label.pack()

entry = tk.Entry(window)
entry.pack()

# 创建按钮
button = tk.Button(window, text="打招呼", command=greet)
button.pack()

# 运行主循环
window.mainloop()
