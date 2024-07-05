from random import randint
import random
from tkinter import *
import turtle
from PIL import ImageGrab
import os
from functools import partial
from tkinter import ttk, PhotoImage, font, filedialog

root = Tk()
root.geometry('1350x850')
root.resizable(False, False)
root.config(bg='#dadada')
style = ttk.Style(root)
style.theme_use('alt')
font_label = font.Font(family="Courier New", size=11, weight="normal", slant="roman")
root.title("L-SYSTEM GENERATION")


main_menu = Menu(root)
root.config(menu=main_menu)


def browseFiles(filename):
    with open(filename, 'r') as f:
        data = f.readline()
    data = eval(data)
    dop_pr.append(data["Доп. правила"])
    ahead.append(data["Вперед"])
    draw_line.append(data["Рисовать"])
    input_ax.delete(0, END)
    input_ax.insert(0, data["Аксиома"])
    input_pr_1.delete(0, END)
    input_pr_1.insert(0, data["Правила"])
    input_angle.delete(0, END)
    input_angle.insert(0, data["Угол"])
    input_itr.delete(0, END)
    input_itr.insert(0, data["Кол-во итераций"])
    input_len.delete(0, END)
    input_len.insert(0, data["Длина линии"])
    input_name.delete(0, END)
    input_name.insert(0, data["Название"])


def save_setting():
    save_param = {}
    save_param["Аксиома"] = input_ax.get()
    save_param["Правила"] = input_pr_1.get()
    save_param["Доп. правила"] = dop_pr[-1]
    save_param["Угол"] = input_angle.get()
    save_param["Кол-во итераций"] = input_itr.get()
    save_param["Длина линии"] = input_len.get()
    save_param["Рисовать"] = draw_line[-1]
    save_param["Вперед"] = ahead[-1]
    save_param["Название"] = input_name.get()
    with open(f"{input_name.get()}.txt", 'w') as f:
        f.write(f'{save_param}')
    file_menu_info.delete(0, END)
    file_menu_info_2.delete(0, END)
    all_files = os.listdir("C:/Users/griba/MainProject")
    for i in all_files:
        if i[-4:] == '.txt':
            if "SOL" in i:
                file_menu_info_2.add_command(label=i[:-4], command=partial(browseFiles, i))
            else:
                file_menu_info.add_command(label=i[:-4], command=partial(browseFiles, i))


def new_window_color_bg():
    window_color_bg = Toplevel(root)
    window_color_bg.geometry('308x313')
    window_color_bg.config(bg='#dadada')
    window_color_bg.resizable(False, False)
    window_color_bg.title("Цвет")
    frame_color_bg = LabelFrame(window_color_bg, text="Цвет: ", font=("Courier New", 10, 'bold'), bg="#dadada")
    frame_color_bg.place(x=10, y=5, width=289, height=298)
    white_label = Text(window_color_bg, bg='#ffffff', state=DISABLED)
    white = ttk.Entry(window_color_bg, font=("Courier New", 10))
    white.insert(0, '#FFFFFF')
    black_label = Text(window_color_bg, bg='#000000', state=DISABLED)
    black = ttk.Entry(window_color_bg, font=("Courier New", 10))
    black.insert(0, '#000000')
    gray_label = Text(window_color_bg, bg='#808080', state=DISABLED)
    gray = ttk.Entry(window_color_bg, font=("Courier New", 10))
    gray.insert(0, '#808080')
    white_label.place(x=30, y=30, width=15, height=15)
    white.place(x=60, y=30, width=80, height=15)
    black_label.place(x=30, y=60, width=15, height=15)
    black.place(x=60, y=60, width=80, height=15)
    gray_label.place(x=30, y=90, width=15, height=15)
    gray.place(x=60, y=90, width=80, height=15)
    bisque_label = Text(window_color_bg, bg='#FFE4C4', state=DISABLED)
    bisque = ttk.Entry(window_color_bg, font=("Courier New", 10))
    bisque.insert(0, '#FFE4C4')
    bisque_label.place(x=30, y=120, width=15, height=15)
    bisque.place(x=60, y=120, width=80, height=15)

    tan_label = Text(window_color_bg, bg='#D2B48C', state=DISABLED)
    tan = ttk.Entry(window_color_bg, font=("Courier New", 10))
    tan.insert(0, '#D2B48C')
    tan_label.place(x=30, y=150, width=15, height=15)
    tan.place(x=60, y=150, width=80, height=15)

    sandybrown_label = Text(window_color_bg, bg='#F4A460', state=DISABLED)
    sandybrown = ttk.Entry(window_color_bg, font=("Courier New", 10))
    sandybrown.insert(0, '#F4A460')
    sandybrown_label.place(x=30, y=180, width=15, height=15)
    sandybrown.place(x=60, y=180, width=80, height=15)

    peru_label = Text(window_color_bg, bg='#CD853F', state=DISABLED)
    peru = ttk.Entry(window_color_bg, font=("Courier New", 10))
    peru.insert(0, '#CD853F')
    peru_label.place(x=30, y=210, width=15, height=15)
    peru.place(x=60, y=210, width=80, height=15)

    saddlebrown_label = Text(window_color_bg, bg='#8B4513', state=DISABLED)
    saddlebrown = ttk.Entry(window_color_bg, font=("Courier New", 10))
    saddlebrown.insert(0, '#8B4513')
    saddlebrown_label.place(x=30, y=240, width=15, height=15)
    saddlebrown.place(x=60, y=240, width=80, height=15)

    brown_label = Text(window_color_bg, bg='#A52A2A', state=DISABLED)
    brown = ttk.Entry(window_color_bg, font=("Courier New", 10))
    brown.insert(0, '#A52A2A')
    brown_label.place(x=30, y=270, width=15, height=15)
    brown.place(x=60, y=270, width=80, height=15)

    lightcoral_label = Text(window_color_bg, bg='#CD5C5C', state=DISABLED)
    lightcoral = ttk.Entry(window_color_bg, font=("Courier New", 10))
    lightcoral.insert(0, '#CD5C5C')
    lightcoral_label.place(x=170, y=30, width=15, height=15)
    lightcoral.place(x=200, y=30, width=80, height=15)

    hotpink_label = Text(window_color_bg, bg='#FA8072', state=DISABLED)
    hotpink = ttk.Entry(window_color_bg, font=("Courier New", 10))
    hotpink.insert(0, '#FA8072')
    hotpink_label.place(x=170, y=60, width=15, height=15)
    hotpink.place(x=200, y=60, width=80, height=15)

    crimson_label = Text(window_color_bg, bg='#DC143C', state=DISABLED)
    crimson = ttk.Entry(window_color_bg, font=("Courier New", 10))
    crimson.insert(0, '#DC143C')
    crimson_label.place(x=170, y=90, width=15, height=15)
    crimson.place(x=200, y=90, width=80, height=15)

    forestgreen_label = Text(window_color_bg, bg='#228B22', state=DISABLED)
    forestgreen = ttk.Entry(window_color_bg, font=("Courier New", 10))
    forestgreen.insert(0, '#228B22')
    forestgreen_label.place(x=170, y=120, width=15, height=15)
    forestgreen.place(x=200, y=120, width=80, height=15)

    darkgreen_label = Text(window_color_bg, bg='#006400', state=DISABLED)
    darkgreen = ttk.Entry(window_color_bg, font=("Courier New", 10))
    darkgreen.insert(0, '#006400')
    darkgreen_label.place(x=170, y=150, width=15, height=15)
    darkgreen.place(x=200, y=150, width=80, height=15)

    olivedrab_label = Text(window_color_bg, bg='#6B8E23', state=DISABLED)
    olivedrab = ttk.Entry(window_color_bg, font=("Courier New", 10))
    olivedrab.insert(0, '#6B8E23')
    olivedrab_label.place(x=170, y=180, width=15, height=15)
    olivedrab.place(x=200, y=180, width=80, height=15)

    paleturquoise_label = Text(window_color_bg, bg='#AFEEEE', state=DISABLED)
    paleturquoise = ttk.Entry(window_color_bg, font=("Courier New", 10))
    paleturquoise.insert(0, '#AFEEEE')
    paleturquoise_label.place(x=170, y=210, width=15, height=15)
    paleturquoise.place(x=200, y=210, width=80, height=15)

    turquoise_label = Text(window_color_bg, bg='#40E0D0', state=DISABLED)
    turquoise = ttk.Entry(window_color_bg, font=("Courier New", 10))
    turquoise.insert(0, '#40E0D0')
    turquoise_label.place(x=170, y=240, width=15, height=15)
    turquoise.place(x=200, y=240, width=80, height=15)

    dodgerblue_label = Text(window_color_bg, bg='#1E90FF', state=DISABLED)
    dodgerblue = ttk.Entry(window_color_bg, font=("Courier New", 10))
    dodgerblue.insert(0, '#1E90FF')
    dodgerblue_label.place(x=170, y=270, width=15, height=15)
    dodgerblue.place(x=200, y=270, width=80, height=15)


def save_dop_pr():
    dop_pr.append(input_dop_pr.get("1.0", END))
    draw_line.append(input_setting_draw_line.get())
    ahead.append(input_setting_ahead.get())


cb_2 = IntVar()
cb_1 = IntVar()
cb = IntVar()
dop_pr = [""]
draw_line = [""]
ahead = [""]


def create_window():
    global cb, input_setting_ahead, input_setting_draw_line, input_dop_pr, dop_pr, draw_line, ahead
    window = Toplevel(root)
    window.geometry('395x310')
    window.config(bg='#dadada')
    window.resizable(False, False)
    frame_setting = LabelFrame(window, text="Доп. правила: ", font=("Courier New", 10, 'bold'), bg="#dadada")
    frame_setting.place(x=20, y=50, width=355, height=120)
    frame_setting = LabelFrame(window, text="Настройка команд: ", font=("Courier New", 10, 'bold'), bg="#dadada")
    frame_setting.place(x=20, y=175, width=355, height=90)
    input_dop_pr = Text(window, font=("Courier New", 10, 'bold'))
    input_dop_pr.place(x=30, y=70, width=333, height=89)
    input_dop_pr.insert(END, dop_pr[-1])
    lbl100 = ttk.Label(window, text="Рисуем отрезок:", font=font_label)
    lbl100.place(x=30, y=200)
    input_setting_draw_line = ttk.Entry(window, width=25, font=("Courier New", 10))
    input_setting_draw_line.place(x=200, y=200, width=157, height=20)
    input_setting_draw_line.insert(0, draw_line[-1])
    lbl101 = ttk.Label(window, text="Вперед (не рисуя):", font=font_label)
    lbl101.place(x=30, y=230)
    input_setting_ahead = ttk.Entry(window, width=25, font=("Courier New", 10))
    input_setting_ahead.place(x=200, y=230, width=157, height=20)
    input_setting_ahead.insert(0, ahead[-1])
    check_button_setting_dark_screen = ttk.Checkbutton(window, text="Случайный угол", variable=cb_1, onvalue=1, offvalue=0)
    check_button_setting_dark_screen.place(x=235, y=20)
    check_button_setting_line_itr = ttk.Checkbutton(window, text="Случайная длина", variable=cb_2, onvalue=1, offvalue=0)
    check_button_setting_line_itr.place(x=20, y=275)
    btn33 = ttk.Button(window, text="Сохранить изменения", command=save_dop_pr)
    btn33.place(x=200, y=275, width=157, height=25)
    window.title("Настройки")


def draw_beautiful_tree_1():
    t.color(color_bc_input_line)
    t.penup()
    t.setx(int(input_x.get()))
    t.sety(int(input_y.get()))
    t.setheading(int(input_start_angle.get()))
    t.pendown()
    axiom = "22220"
    axmTemp = ""
    itr = 12
    angl = 16
    dl = 10
    stc = []
    thick = 16
    t.pensize(thick)
    translate = {"1": "21",
                 "0": "1[-20]+20"}
    dop_pr.append("1 : 21")
    draw_line.append("0 1 2")
    input_pr_1.delete(0, END)
    input_pr_1.insert(0, "0 : 1[-20][+20]")
    input_ax.delete(0, END)
    input_ax.insert(0, axiom)
    input_angle.delete(0, END)
    input_angle.insert(0, "16")
    input_itr.delete(0, END)
    input_itr.insert(0, "12")
    input_len.delete(0, END)
    input_len.insert(0, "10")
    input_name.delete(0, END)
    input_name.insert(0, "Дерево 1")
    for k in range(itr):
        for ch in axiom:
            if ch in translate:
                axmTemp += translate[ch]
            else:
                axmTemp += ch
        axiom = axmTemp
        axmTemp = ""

    for ch in axiom:
        if ch == "+":
            t.right(angl - randint(-13, 13))
        elif ch == "-":
            t.left(angl - randint(-13, 13))
        elif ch == "2":
            if randint(0, 10) > 4:
                t.forward(dl)
        elif ch == "1":
            if randint(0, 10) > 4:
                t.forward(dl)
        elif ch == "0":
            stc.append(t.pensize())
            t.pensize(4)
            r = randint(0, 10)
            if r < 3:
                t.pencolor('#009900')
            elif r > 6:
                t.pencolor('#667900')
            else:
                t.pencolor('#20BB00')
            t.forward(dl - 2)
            t.pensize(stc.pop())
            t.pencolor(color_bc_input_line)
        elif ch == "[":
            thick = thick * 0.75
            t.pensize(thick)
            stc.append(thick)
            stc.append(t.xcor())
            stc.append(t.ycor())
            stc.append(t.heading())
        elif ch == "]":
            t.penup()
            t.setheading(stc.pop())
            t.sety(stc.pop())
            t.setx(stc.pop())
            thick = stc.pop()
            t.pensize(thick)
            t.pendown()

def draw_beautiful_tree_2():
    t.color(color_bc_input_line)
    t.penup()
    t.setx(int(input_x.get()))
    t.sety(int(input_y.get()))
    t.setheading(int(input_start_angle.get()))
    t.pendown()
    axiom = "22220"
    axmTemp = ""
    itr = 12
    angl = 14
    dl = 10
    level = 0
    stc = []
    thick = 16
    t.pensize(thick)
    dop_pr.append("1 : 21")
    draw_line.append("0 1 2")
    input_ax.delete(0, END)
    input_ax.insert(0, axiom)
    input_pr_1.delete(0, END)
    input_pr_1.insert(0, "0 : 1[-20][+20]")
    input_angle.delete(0, END)
    input_angle.insert(0, "16")
    input_itr.delete(0, END)
    input_itr.insert(0, "12")
    input_len.delete(0, END)
    input_len.insert(0, "10")
    input_name.delete(0, END)
    input_name.insert(0, "Дерево 2")
    for k in range(itr):
        for ch in axiom:
            if ch == '0':
                axmTemp += '1[-20][+20]'
            elif ch == '1':
                axmTemp += '21'
            elif ch == '[':
                axmTemp += '['
                level += 1
            elif ch == ']':
                axmTemp += ']'
                level -= 1
            elif ch == '2':
                if randint(0, 100) < 7 and level > 2:
                    axmTemp += '3[^30]'
                else:
                    axmTemp += '2'
            else:
                axmTemp += ch
        axiom = axmTemp
        axmTemp = ""
    for ch in axiom:
        if ch == "+":
            t.right(angl - randint(-13, 13))
        elif ch == "-":
            t.left(angl - randint(-13, 13))
        elif ch == "^":
            ug = randint(-30, 30)
            if ug < 0:
                t.left(ug - 25)
            else:
                t.left(ug + 25)
        elif ch == "[":
            level += 1
            stc.append(thick)
            stc.append(t.xcor())
            stc.append(t.ycor())
            stc.append(t.heading())
            thick = thick * 0.75
            t.pensize(thick)
        elif ch == "]":
            level -= 1
            t.penup()
            t.setheading(stc.pop())
            t.sety(stc.pop())
            t.setx(stc.pop())
            thick = stc.pop()
            t.pensize(thick)
            t.pendown()
        elif ch == "0":
            stc.append(t.pensize())
            t.pensize(4)
            r = randint(0, 10)
            if r < 3:
                t.pencolor('#009900')
            elif r > 6:
                t.pencolor('#667900')
            else:
                t.pencolor('#20BB00')
            t.forward(dl - 2)
            t.pensize(stc.pop())
            t.pencolor(color_bc_input_line)
        else:
            if randint(0, 10) > 4:
                t.forward(dl)


file_menu_info = Menu(main_menu, tearoff=0)
file_menu_info_2 = Menu(main_menu, tearoff=0)

all_files = os.listdir("C:/Users/griba/MainProject")
for i in all_files:
    if i[-4:] == '.txt':
        if "SOL" in i:
            file_menu_info_2.add_command(label=i[:-4], command=partial(browseFiles, i))
        else:
            file_menu_info.add_command(label=i[:-4], command=partial(browseFiles, i))


file_menu = Menu(main_menu, tearoff=0)
file_menu.add_command(label="Сохранить параметры", command=save_setting)
file_menu.add_separator()
file_menu.add_command(label="Настройки", command=create_window)

file_menu_trees = Menu(main_menu, tearoff=0)
file_menu_trees.add_command(label="Дерево 1", command=draw_beautiful_tree_1)
file_menu_trees.add_command(label="Дерево 2", command=draw_beautiful_tree_2)

main_menu.add_cascade(label='Файл', menu=file_menu)
main_menu.add_cascade(label='Деревья', menu=file_menu_trees)
main_menu.add_cascade(label='DOL-системы', menu=file_menu_info)
main_menu.add_cascade(label='SOL-системы', menu=file_menu_info_2)


def clear_screen():
    t.clear()


def save_screen():
    x0 = root.winfo_rootx() + 5
    y0 = root.winfo_rooty() + 15
    x1 = x0 + root.winfo_width() - 245
    y1 = y0 + root.winfo_height() - 35
    ImageGrab.grab().crop((x0, y0, x1, y1)).save(f"{input_name.get()}.png")


def print_screen():
    global t
    screen.bgcolor(color_bc_input)
    t.pensize(int(input_width_line.get()))
    t.color(color_bc_input_line)
    t.penup()
    t.setx(int(input_x.get()))
    t.sety(int(input_y.get()))
    t.setheading(int(input_start_angle.get()))
    t.pendown()
    rules = {}
    key_list = ''
    value_list = []
    choice_list = []
    try:
        if len(dop_pr[-1].splitlines()) > 0:
            for rule in dop_pr[-1].splitlines():
                if ":" not in rule:
                    output_err.delete('1.0', END)
                    output_err.insert("1.0", "Ошибка в правиле")
                if len(rule.split(":")) == 2:
                    key, value = rule.split(":")
                    rules[key.strip()] = [[value.strip()], [1]]
                elif len(rule.split(":")) == 3:
                    key, choice, value = rule.split(":")
                    if key_list != key:
                        key_list = key
                        value_list = [value.strip()]
                        choice_list = [float(choice.strip())]
                    else:
                        value_list.append(value.strip())
                        choice_list.append(float(choice.strip()))
                    rules[key_list.strip()] = [value_list, choice_list]
    except:
        output_err.delete("1.0", END)
        output_err.insert("1.0", "Неправильно введено правило")

    axmTemp = ""
    if len(input_pr_1.get()) > 0:
        key, value = input_pr_1.get().split(":")
        rules[key.strip()] = [[value.strip()], [1]]
        if ":" not in input_pr_1.get():
            output_err.delete('1.0', END)
            output_err.insert("1.0", "Ошибка в правиле")

    print(rules)
    axiom = input_ax.get()
    if len(axiom) == 0:
        output_err.delete('1.0', END)
        output_err.insert("1.0", "Введите аксиому")
    itr = input_itr.get()
    if len(itr) == 0:
        output_err.delete('1.0', END)
        output_err.insert("1.0", "Введите \nчисло итерации")
    for i in rules.keys():
        if sum(rules[i][1]) > 1:
            output_err.delete('1.0', END)
            output_err.insert("1.0", f"Правило: {i} \nбольше 1")
            break
    an = input_angle.get()
    if len(an) == 0:
        output_err.delete('1.0', END)
        output_err.insert("1.0", f"Введите угол")
    print(len(an))
    for _ in range(int(input_itr.get())):
        for ch in axiom:
            try:
                axmTemp += random.choices(rules[ch][0], weights=rules[ch][1])[0]
            except:
                rules[ch] = [[ch], [1]]
                axmTemp += random.choices(rules[ch][0], weights=rules[ch][1])[0]
        axiom = axmTemp
        axmTemp = ""
    help_func(axiom)
    print(axiom)


def help_func(axiom):
    global draw_line
    stc = []
    draw_line_1 = draw_line[-1].split()
    if cb_1.get() == 1 and cb_2.get() == 1:
        for ch in axiom:
            if ch == "+":
                t.right(int(input_angle.get()) - randint(-13,13))
            elif ch == "-":
                t.left(int(input_angle.get()) - randint(-13,13))
            elif ch == "[":
                stc.append(t.xcor())
                stc.append(t.ycor())
                stc.append(t.heading())
            elif ch == "]":
                t.penup()
                t.setheading(stc.pop())
                t.sety(stc.pop())
                t.setx(stc.pop())
                t.pendown()
            elif ch in draw_line_1:
                if randint(0, 10) > 4:
                    t.forward(int(input_len.get()))
    elif cb_1.get() == 1 and cb_2.get() == 0:
        for ch in axiom:
            if ch == "+":
                t.right(int(input_angle.get()) - randint(-13,13))
            elif ch == "-":
                t.left(int(input_angle.get()) - randint(-13,13))
            elif ch == "[":
                stc.append(t.xcor())
                stc.append(t.ycor())
                stc.append(t.heading())
            elif ch == "]":
                t.penup()
                t.setheading(stc.pop())
                t.sety(stc.pop())
                t.setx(stc.pop())
                t.pendown()
            elif ch in draw_line_1:
                t.forward(int(input_len.get()))
    else:
        for ch in axiom:
            if ch == "+":
                t.right(int(input_angle.get()))
            elif ch == "-":
                t.left(int(input_angle.get()))
            elif ch == "[":
                stc.append(t.xcor())
                stc.append(t.ycor())
                stc.append(t.heading())
            elif ch == "]":
                t.penup()
                t.setheading(stc.pop())
                t.sety(stc.pop())
                t.setx(stc.pop())
                t.pendown()
            elif ch in draw_line_1:
                t.forward(int(input_len.get()))
    output_err.delete('1.0', END)


def on_color_line(index):
    global color_bc_line, color_bc_input_line
    color_bc_line_1 = input_color_line.get()
    if color_bc_line_1 == "  Белый":
        color_bc_line.config(background="#FFFFFF")
        color_bc_input_line = "#FFFFFF"
    elif color_bc_line_1 == "  Черный":
        color_bc_line.config(background="#000000")
        color_bc_input_line = "#000000"
    elif color_bc_line_1 == "  Серый":
        color_bc_line.config(background="#808080")
        color_bc_input_line = "#808080"
    elif color_bc_line_1 == "  Молочный":
        color_bc_line.config(background="#FFE4C4")
        color_bc_input_line = "#FFE4C4"
    elif color_bc_line_1 == "  Смуглый":
        color_bc_line.config(background="#D2B48C")
        color_bc_input_line = "#D2B48C"
    elif color_bc_line_1 == "  Песочный":
        color_bc_line.config(background="#F4A460")
        color_bc_input_line = "#F4A460"
    elif color_bc_line_1 == "  Коричневый":
        color_bc_line.config(background="#8B4513")
        color_bc_input_line = "#8B4513"
    elif color_bc_line_1 == "  Бурый":
        color_bc_line.config(background="#A52A2A")
        color_bc_input_line = "#A52A2A"
    elif color_bc_line_1 == "  Розовый":
        color_bc_line.config(background="#FA8072")
        color_bc_input_line = "#FA8072"
    elif color_bc_line_1 == "  Красный":
        color_bc_line.config(background="#DC143C")
        color_bc_input_line = "#DC143C"
    elif color_bc_line_1 == "  Зеленый":
        color_bc_line.config(background="#228B22")
        color_bc_input_line = "#228B22"
    elif color_bc_line_1 == "  Болотный":
        color_bc_line.config(background="#6B8E23")
        color_bc_input_line = "#6B8E23"
    elif color_bc_line_1 == "  Голубой":
        color_bc_line.config(background="#AFEEEE")
        color_bc_input_line = "#AFEEEE"
    elif color_bc_line_1 == "  Синий":
        color_bc_line.config(background="#1E90FF")
        color_bc_input_line = "#1E90FF"


def on_field_change(index):
    global color_bc_text, color_bc_input
    color_bc = input_color_bc.get()
    if color_bc == "  Белый":
        color_bc_text.config(background="#FFFFFF")
        color_bc_input = "#FFFFFF"
    elif color_bc == "  Черный":
        color_bc_text.config(background="#000000")
        color_bc_input = "#000000"
    elif color_bc == "  Серый":
        color_bc_text.config(background="#808080")
        color_bc_input = "#808080"
    elif color_bc == "  Молочный":
        color_bc_text.config(background="#FFE4C4")
        color_bc_input = "#FFE4C4"
    elif color_bc == "  Смуглый":
        color_bc_text.config(background="#D2B48C")
        color_bc_input = "#D2B48C"
    elif color_bc == "  Песочный":
        color_bc_text.config(background="#F4A460")
        color_bc_input = "#F4A460"
    elif color_bc == "  Коричневый":
        color_bc_text.config(background="#8B4513")
        color_bc_input = "#8B4513"
    elif color_bc == "  Бурый":
        color_bc_text.config(background="#A52A2A")
        color_bc_input = "#A52A2A"
    elif color_bc == "  Розовый":
        color_bc_text.config(background="#FA8072")
        color_bc_input = "#FA8072"
    elif color_bc == "  Красный":
        color_bc_text.config(background="#DC143C")
        color_bc_input = "#DC143C"
    elif color_bc == "  Зеленый":
        color_bc_text.config(background="#228B22")
        color_bc_input = "#228B22"
    elif color_bc == "  Болотный":
        color_bc_text.config(background="#6B8E23")
        color_bc_input = "#6B8E23"
    elif color_bc == "  Голубой":
        color_bc_text.config(background="#AFEEEE")
        color_bc_input = "#AFEEEE"
    elif color_bc == "  Синий":
        color_bc_text.config(background="#1E90FF")
        color_bc_input = "#1E90FF"


def main_window_1350x850():
    global output_err, input_width_line, input_color_line, input_color_bc, input_x, input_y, input_start_angle, input_ax, input_pr_1, input_len, input_angle, input_name, input_itr, color_bc_text, color_bc_line, input_color_line, color_bc_input, color_bc_input_line
    frame_top = Frame(root, highlightbackground="#838383", highlightthickness=1, bg='#dadada')
    frame_top.place(x=1138, y=5, width=202, height=825)

    frame_param = LabelFrame(root, text="Начальные условия: ", font=("Courier New", 10, 'bold'), bg="#dadada")
    frame_param.place(x=1147, y=10, width=185, height=81)

    frame_param = LabelFrame(root, text="Параметры: ", font=("Courier New", 10, 'bold'), bg="#dadada")
    frame_param.place(x=1147, y=95, width=185, height=270)

    frame_param = LabelFrame(root, text="Внешний вид: ", font=("Courier New", 10, 'bold'), bg="#dadada")
    frame_param.place(x=1147, y=369, width=185, height=140)

    frame_param = LabelFrame(root, text="Вывод: ", font=("Courier New", 10, 'bold'), bg="#dadada")
    frame_param.place(x=1147, y=680, width=185, height=140)

    output_err = Text(root)
    output_err.place(x=1156, y=700, width=165, height=107)

    input_width_line = ttk.Entry(root, width=25, font=("Courier New", 10))
    input_width_line.place(x=1286, y=480, width=35, height=20)
    input_width_line.insert(0, '2')

    lbl16 = ttk.Label(root, text="Толщина линии:", font=font_label)
    lbl16.place(x=1156, y=480)

    lbl15 = ttk.Label(root, text="Цвет линии:", font=font_label)
    lbl15.place(x=1156, y=428)

    input_color_line = ttk.Combobox(root, values=["  Белый", "  Черный", "  Серый", "  Молочный", "  Смуглый", "  Песочный", "  Коричневый", "  Бурый", "  Розовый", "  Красный", "  Зеленый", "  Болотный", "  Голубой", "  Синий"])
    input_color_line.bind('<<ComboboxSelected>>', on_color_line)
    input_color_line.place(x=1156, y=450, width=120, height=20)
    input_color_line.insert(0, "  Черный")

    color_bc_input_line = "#000000"

    color_bc_line = Text(root, bg='#000000', state=DISABLED)
    color_bc_line.place(x=1283, y=450, width=40, height=20)

    # btn11 = ttk.Button(root, text="· · ·", command=new_window_color_bg)
    # btn11.place(x=1283, y=450, width=40, height=20)

    lbl14 = ttk.Label(root, text="Цвет фона:", font=font_label)
    lbl14.place(x=1156, y=384)

    input_color_bc = ttk.Combobox(root, values=["  Белый", "  Черный", "  Серый", "  Молочный", "  Смуглый", "  Песочный", "  Коричневый", "  Бурый", "  Розовый", "  Красный", "  Зеленый", "  Болотный", "  Голубой", "  Синий"])
    input_color_bc.bind('<<ComboboxSelected>>', on_field_change)
    input_color_bc.insert(0, "  Белый")
    input_color_bc.place(x=1156, y=406, width=120, height=20)

    color_bc_input = "#FFFFFF"

    color_bc_text = Text(root, bg='#FFFFFF', state=DISABLED)
    color_bc_text.place(x=1283, y=406, width=40, height=20)
    # input_color_bc = ttk.Entry(root, font=("Courier New", 10))
    # input_color_bc.place(x=1156, y=406, width=120, height=20)
    # input_color_bc.insert(0, '#FFFFFF')

    # btn10 = ttk.Button(root, text="· · ·", command=new_window_color_bg)
    # btn10.place(x=1283, y=406, width=40, height=20)

    lbl10 = ttk.Label(root, text="X:", font=font_label)
    lbl10.place(x=1165, y=30)

    input_x = ttk.Entry(root, width=25, font=("Courier New", 10))
    input_x.place(x=1190, y=30, width=40, height=20)
    input_x.insert(0, "0")

    lbl11 = ttk.Label(root, text="Y:", font=font_label)
    lbl11.place(x=1245, y=30)

    input_y = ttk.Entry(root, width=25, font=("Courier New", 10))
    input_y.place(x=1270, y=30, width=40, height=20)
    input_y.insert(0, '0')

    lbl12 = ttk.Label(root, text="Угол:", font=font_label)
    lbl12.place(x=1165, y=60)

    input_start_angle = ttk.Entry(root, width=25, font=("Courier New", 10))
    input_start_angle.place(x=1217, y=60, width=40, height=20)
    input_start_angle.insert(0, '90')

    lbl13 = ttk.Label(root, text="°", font=font_label)
    lbl13.place(x=1260, y=60)

    lbl1 = ttk.Label(root, text="Аксиома:", font=font_label)
    lbl1.place(x=1156, y=110)

    input_ax = ttk.Entry(root, width=25, font=("Courier New", 10))
    input_ax.place(x=1156, y=132, width=165, height=20)

    lbl2 = ttk.Label(root, text="Правило:", font=font_label)
    lbl2.place(x=1156, y=154)

    input_pr_1 = ttk.Entry(root, width=25, font=("Courier New", 10))
    input_pr_1.place(x=1156, y=176, width=165, height=20)

    lbl5 = ttk.Label(root, text="Длина:", font=font_label)
    lbl5.place(x=1156, y=247)

    input_len = ttk.Entry(root, font=("Courier New", 10))
    input_len.place(x=1215, y=247, width=32, height=20)
    input_len.insert(0, '5')

    lbl6 = ttk.Label(root, text="px.", font=font_label)
    lbl6.place(x=1252, y=247)

    lbl3 = ttk.Label(root, text="Угол:", font=font_label)
    lbl3.place(x=1156, y=274)

    input_angle = ttk.Entry(root, font=("Courier New", 10))
    input_angle.place(x=1215, y=274, width=32, height=20)

    lbl7 = ttk.Label(root, text="°", font=font_label)
    lbl7.place(x=1252, y=274)

    lbl8 = ttk.Label(root, text="——————————————————", font=font_label)
    lbl8.place(x=1156, y=296)

    lbl9 = ttk.Label(root, text="Название:", font=font_label)
    lbl9.place(x=1156, y=312)

    lbl4 = ttk.Label(root, text="Кол-во итераций:", font=font_label)
    lbl4.place(x=1156, y=198)

    input_name = ttk.Entry(root, font=("Courier New", 10))
    input_name.place(x=1156, y=334, width=165, height=20)

    input_itr = ttk.Entry(root, font=("Courier New", 10))
    input_itr.place(x=1156, y=220, width=165, height=20)

    btn1 = ttk.Button(root, text="Построить", command=print_screen)
    btn1.place(x=1143, y=630, width=190, height=40)

    btn2 = ttk.Button(root, text="Очистить холст", command=clear_screen)
    btn2.place(x=1143, y=580, width=190, height=40)

    btn3 = ttk.Button(root, text="Сохранить \nизображения", command=save_screen)
    btn3.place(x=1143, y=530, width=190, height=40)


canvas = turtle.ScrolledCanvas(root, width=1100, height=850)
canvas.pack(side=LEFT)
screen = turtle.TurtleScreen(canvas)
screen.screensize(3000, 3000)
screen.tracer(0)
t = turtle.RawTurtle(screen)
t.hideturtle()
# t.speed(60)


main_window_1350x850()
screen.update()
screen.mainloop()