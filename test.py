from tkinter import *
window = Tk()
window.title("Calculator")
window.option_add("*font", "Algerian 30")
window.option_add("*background", "#FFF7EE")
window.option_add("*foreground", "#283747")
window.option_add("*relief", GROOVE)

label_show = StringVar()
label_show.set("")
expression = ""
in_show = ""

def Clear():
    global expression
    global label_show
    mid_label.config(text="")   
    result = ""
    expression = ""
    b_del.config(state=NORMAL)
    label_show.set(result)
    if expression == "":
        b_del.config(state=DISABLED)

def Show(n):
    global expression
    global label_show
    global in_show
    b_del.config(state=NORMAL)
    in_show += n
    expression += n
    mid_label.config(text="")
    if len(expression) > 18:
        label_show.set(expression[len(expression)-18:])
        in_show = expression[len(expression)-18:]
    else:
        label_show.set(expression)
def Calculate():
    global expression
    global label_show
    try:
        b_del.config(state=DISABLED)
        real = ["*", "/"]
        edit = ["x", "÷"]
        result = ""
        for i in expression:
            if i in edit:
                idx = edit.index(i)
                result += real[idx]
            else:
                result += i
        final_result = eval(result)
        if len(str(final_result)) <= 18:
            if type(final_result) == int:
                label_show.set(final_result)
                expression = str(final_result)
            else:
                if final_result - int(final_result) == 0:
                    label_show.set(int(final_result))
                    expression = str(final_result)
                else:
                    x = round(final_result, 3)
                    label_show.set(x)
                    expression = str(x)
        else:
            label_show.set("")
            mid_label.config(text="This number is too high.")
            b_del.config(state=DISABLED)
            expression = ""
    except:
        label_show.set("")
        mid_label.config(text="Error")
        b_del.config(state=DISABLED)
        expression = ""
def Delete():
    global expression
    global label_show
    global i
    if len(expression)==1:
        b_del.config(state=DISABLED)
    if len(expression) > 18:
        delete = expression[len(expression)-18-1:len(expression)-1]
        label_show.set(delete)
        expression = expression[:len(expression)-1]
    else:
        delete = expression[:len(expression)-1]
        label_show.set(delete)
        expression = delete

Label(textvariable=label_show, bg="#FFF7F7", font="Algerian 18", bd=5).grid(row=0, column=0, columnspan=4, sticky="NEWS")
mid_label = Label(bd=5, font="Algerian 16")
mid_label.grid(row=1, column=0, columnspan=4, sticky="NEWS")
Button(text="C", command=Clear, bd=5, fg="#FF604F").grid(row=2, column=0, sticky="NEWS")
Button(text="(", command=lambda: Show("("), bd=5).grid(row=2, column=1, sticky="NEWS")
Button(text=")", command=lambda: Show(")"), bd=5).grid(row=2, column=2, sticky="NEWS")
b_del = Button(text="␡", command=Delete, bd=5, bg="#F1948A")
b_del.grid(row=2, column=3, sticky="NEWS")
b_del.config(state=DISABLED)
Button(text="7", command=lambda: Show("7"), bd=5).grid(row=3, column=0, sticky="NEWS")
Button(text="8", command=lambda: Show("8"), bd=5).grid(row=3, column=1, sticky="NEWS")
Button(text="9", command=lambda: Show("9"), bd=5).grid(row=3, column=2, sticky="NEWS")
Button(text="÷", command=lambda: Show("÷"), bd=5).grid(row=3, column=3, sticky="NEWS")
Button(text="4", command=lambda: Show("4"), bd=5).grid(row=4, column=0, sticky="NEWS")
Button(text="5", command=lambda: Show("5"), bd=5).grid(row=4, column=1, sticky="NEWS")
Button(text="6", command=lambda: Show("6"), bd=5).grid(row=4, column=2, sticky="NEWS")
Button(text="x", command=lambda: Show("x"), bd=5).grid(row=4, column=3, sticky="NEWS")
Button(text="1", command=lambda: Show("1"), bd=5).grid(row=5, column=0, sticky="NEWS")
Button(text="2", command=lambda: Show("2"), bd=5).grid(row=5, column=1, sticky="NEWS")
Button(text="3", command=lambda: Show("3"), bd=5).grid(row=5, column=2, sticky="NEWS")
Button(text="-", command=lambda: Show("-"), bd=5).grid(row=5, column=3, sticky="NEWS")
Button(text="0", command=lambda: Show("0"), bd=5).grid(row=6, column=0, sticky="NEWS")
Button(text=".", command=lambda: Show("."), bd=5).grid(row=6, column=1, sticky="NEWS")
Button(text="+", command=lambda: Show("+"), bd=5).grid(row=6, column=3, sticky="NEWS")
Button(text="=", command=Calculate, bd=5, fg="#28B463").grid(row=6, column=2, sticky="NEWS")

window.mainloop()