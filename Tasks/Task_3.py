import tkinter as tk

def resize_text_widget(event=None):
    """Изменяет размер многострочного текстового поля в соответствии со значениями полей ввода."""
    try:
        width = int(entry_width.get())
        height = int(entry_height.get())
        text_widget.config(width=width, height=height)
    except ValueError:
        tk.messagebox.showerror("Ошибка", "Введите корректные числовые значения!")

def set_focus_color(event):
    text_widget.config(bg="white")

def unset_focus_color(event):
    text_widget.config(bg="lightgrey")

root = tk.Tk()
root.title("Изменение размеров Text")

# Поля для ввода ширины и высоты
entry_width = tk.Entry(root, width=5)
entry_width.insert(0, "25")
entry_width.grid(row=0, column=0, padx=5, pady=5)

entry_height = tk.Entry(root, width=5)
entry_height.insert(0, "12")
entry_height.grid(row=1, column=0, padx=5, pady=5)

# Кнопка для изменения размеров
btn_resize = tk.Button(root, text="Изменить", command=resize_text_widget)
btn_resize.grid(row=0, column=1, rowspan=2, padx=5, pady=5)

# Многострочное текстовое поле
text_widget = tk.Text(root, width=25, height=12, bg="lightgrey")
text_widget.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

entry_width.bind("<Return>", resize_text_widget)
entry_height.bind("<Return>", resize_text_widget)
text_widget.bind("<FocusIn>", set_focus_color)
text_widget.bind("<FocusOut>", unset_focus_color)

root.mainloop()
