import tkinter as tk

def add_to_listbox(event):
    """Добавляет текст из текстового поля в список при нажатии Enter."""
    text = entry.get().strip()
    if text: 
        listbox.insert(tk.END, text)
        entry.delete(0, tk.END)  

def copy_to_entry(event):
    """Копирует выбранный элемент из списка в текстовое поле при двойном клике."""
    selection = listbox.curselection()
    if selection: 
        entry.delete(0, tk.END)  
        entry.insert(0, listbox.get(selection[0]))  # Копирование текста

def main():
    root = tk.Tk()
    root.title("Текстовое поле и список")

    # Однострочное текстовое поле
    global entry  
    entry = tk.Entry(root, width=40)
    entry.pack(pady=10)
    entry.bind("<Return>", add_to_listbox) 

    # Список (Listbox)
    global listbox  
    listbox = tk.Listbox(root, width=40, height=10)
    listbox.pack(pady=10)
    listbox.bind("<Double-Button-1>", copy_to_entry)

    root.mainloop()

if __name__ == "__main__":
    main()
