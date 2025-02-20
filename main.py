import sys
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title(u"memo")
root.geometry("400x300")

frame = tk.Frame(root)
frame.grid(row=2, column=0, columnspan=2, sticky="w")

txtBox = tk.Entry()
txtBox.grid(row=0, column=0, padx=5, pady=5)
value = txtBox.get()

checkBoxes = []

# ボタンを押したときに呼び出される関数
def SaveEntryValue(event):
    value = txtBox.get()
    if not value:
        messagebox.showinfo('error', 'Please enter a value')
        return 

    boolean_v = tk.BooleanVar()
    checkBox = tk.Checkbutton(frame, text = value, variable=boolean_v)
    checkBox.var = boolean_v
    # checkBox.grid(row=len(checkBoxes)+2, column=0, padx=5, pady=5, sticky="w")
    checkBox.pack(anchor="w")
    checkBoxes.append(checkBox)
    txtBox.delete(0, tk.END)

# 項目削除
def DeleteItem(event):
    global checkBoxes
    n_checkBoxes = []
    for checkBox in checkBoxes:
        if checkBox.var.get():
            checkBox.destroy()
        else:
            n_checkBoxes.append(checkBox)
    checkBoxes = n_checkBoxes



btn = tk.Button(text = u'保存')
btn.bind("<Button-1>", SaveEntryValue)
btn.grid(row=0, column=1, padx=5, pady=5)

Dbtn = tk.Button(text = u'選択した要素を削除')
Dbtn.bind("<Button-1>", DeleteItem)
Dbtn.grid(row=1, column=0, padx=5, pady=5)


bar_y = tk.Scrollbar(frame, orient=tk.VERTICAL)
bar_y.pack(side=tk.RIGHT, fill=tk.Y)

root.mainloop()