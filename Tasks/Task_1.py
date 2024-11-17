import tkinter as tk
from tkinter import messagebox

def move_items(source_listbox, target_listbox):
    selected_items = source_listbox.curselection()
    if not selected_items:
        messagebox.showinfo("Информация", "Dыберите элементы для перемещения.")
        return

    for index in selected_items[::-1]:  
        item = source_listbox.get(index)
        target_listbox.insert(tk.END, item)
        source_listbox.delete(index)

def main():
    root = tk.Tk()
    root.title("Список покупок")

    # Фреймы
    frame_lists = tk.Frame(root)
    frame_lists.pack(pady=10)

    frame_buttons = tk.Frame(root)
    frame_buttons.pack()

    # перечень товаров
    listbox_items = tk.Listbox(frame_lists, selectmode=tk.MULTIPLE, width=30, height=15)
    listbox_items.pack(side=tk.LEFT, padx=5)

    items = ["Печенье", "Сок", "Бананы", "Творог", "Овсянка", "Морковь", "Картофель", "Курица", "Салат", "Гречка"]
    for item in items:
        listbox_items.insert(tk.END, item)

    # перечень покупок
    listbox_shopping = tk.Listbox(frame_lists, selectmode=tk.MULTIPLE, width=30, height=15)
    listbox_shopping.pack(side=tk.RIGHT, padx=5)

    # Кнопки управления
    button_add = tk.Button(frame_buttons, text="Добавить в покупки", 
                           command=lambda: move_items(listbox_items, listbox_shopping))
    button_add.pack(side=tk.LEFT, padx=5, pady=5)

    button_remove = tk.Button(frame_buttons, text="Удалить из покупок", 
                              command=lambda: move_items(listbox_shopping, listbox_items))
    button_remove.pack(side=tk.RIGHT, padx=5, pady=5)

    root.mainloop()

if __name__ == "__main__":
    main()
