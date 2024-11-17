import tkinter as tk

def main():
    root = tk.Tk()
    root.title("Рисунок на холсте")

    # холст
    canvas = tk.Canvas(root, width=300, height=300, bg="white")
    canvas.pack()

    # прямоугольник
    canvas.create_rectangle(100, 150, 200, 250, fill="lightblue", outline="")

    # крыша
    canvas.create_polygon(80, 150, 220, 150, 150, 90, fill="lightblue", outline="")

    # солнце
    canvas.create_oval(220, 40, 260, 80, fill="orange", outline="")

    # трава
    for i in range(0, 300, 10):  
        canvas.create_line(i, 250, i + 15, 230, fill="green", width=2) 

    root.mainloop()

if __name__ == "__main__":
    main()
