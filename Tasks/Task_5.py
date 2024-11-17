from tkinter import *

def motion():
    """Функция анимации движения круга."""
    # координаты центра круга
    x0, y0, x1, y1 = c.coords(ball)
    ball_center_x = (x0 + x1) / 2
    ball_center_y = (y0 + y1) / 2

    # разница между текущими и целевыми координатами
    dx = target_x - ball_center_x
    dy = target_y - ball_center_y

    # Скорость
    step_x = 1 if dx > 0 else -1 if dx < 0 else 0
    step_y = 1 if dy > 0 else -1 if dy < 0 else 0

    c.move(ball, step_x, step_y)

    if abs(dx) > 1 or abs(dy) > 1:
        root.after(10, motion)

def on_click(event):
    global target_x, target_y
    target_x = event.x
    target_y = event.y
    motion()

root = Tk()

# холст
c = Canvas(root, width=300, height=200, bg="white")
c.pack()

# круг
ball = c.create_oval(0, 100, 40, 140, fill='green')

# Начальные координаты 
target_x = 20 
target_y = 120

# Привязка клика мыши
c.bind("<Button-1>", on_click)

root.mainloop()
