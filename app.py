import tkinter as t
from tkinter.constants import END

commonFont = "Arial 14"

val1 = 0
sign = ""

win = t.Tk()
win.title("Калькулятор")
win.geometry("395x245")

lb_text = t.StringVar()
lb_text.set("")

lb = t.Label(textvariable=lb_text, font=commonFont)
lb.grid(row=0, column=0, columnspan=3, pady=5)

def btn_click(i):
    if (len(lb_text.get()) >= 10):
        return
    txt = lb_text.get()
    lb_text.set(txt + str(i))

index = 1
for r in range(1,4):
    for c in range(1, 4):
        txt_index = str(index)
        func = lambda index=index:btn_click(index)
        btn = t.Button(text=txt_index, font=commonFont, width=7, command=func)
        btn.grid(row=r, column=c-1, padx=5, pady=5)
        index += 1

def btn_clear():
    lb_text.set("")

def get_value():
    result = 0
    if (len(lb_text.get()) > 0):
        result = float(lb_text.get())
    return result

def btn_change(s):
    global sign
    sign = s
    global val1
    val1 = get_value()
    lb_text.set("")

def btn_equal():
    val2 = get_value()
    result = 0
    if (sign == "+"):
        result = val1 + val2
    elif (sign == "-"):
        result = val1 - val2
    elif (sign == "*"):
        result = val1 * val2
    elif (sign == "/"):
        result = val1 / val2
    else:
        lb_text.set("error")
    lb_text.set(round(result,3))

btnPlus = t.Button(text="+", font=commonFont, width=7, command=lambda:btn_change("+"))
btnPlus.grid(row=1, column=3, padx=5, pady=5)

btnMinus = t.Button(text="-", font=commonFont, width=7, command=lambda:btn_change("-"))
btnMinus.grid(row=2, column=3, padx=5, pady=5)

btnMultiply = t.Button(text="*", font=commonFont, width=7, command=lambda:btn_change("*"))
btnMultiply.grid(row=3, column=3, padx=5, pady=5)

btnCancel = t.Button(text="C", font=commonFont, width=7, command=btn_clear)
btnCancel.grid(row=4, column=0, padx=5, pady=5)

btnZero = t.Button(text="0", font=commonFont, width=7, command=lambda:btn_click(0))
btnZero.grid(row=4, column=1, padx=5, pady=5)

btnEqual = t.Button(text="=", font=commonFont, width=7, command=btn_equal)
btnEqual.grid(row=4, column=2, padx=5, pady=5)

btnDivide = t.Button(text="/", font=commonFont, width=7, command=lambda:btn_change("/"))
btnDivide.grid(row=4, column=3, padx=5, pady=5)

win.mainloop()