import tkinter as tk


def number(root, e, number):
    current = e.get()
    e.delete(0, tk.END)
    e.insert(0, str(current) + str(number))


def dot(root, e):
    current = e.get()
    e.delete(0, tk.END)
    e.insert(0, str(current) + ".")


def clear(root, e):
    e.delete(0, tk.END)


def add(root, e):
    first = e.get()
    global f_num, math
    math = 1
    f_num = float(first)
    e.delete(0, tk.END)


def subtract(root, e):
    first = e.get()
    global f_num, math
    math = 2
    f_num = float(first)
    e.delete(0, tk.END)


def multiply(root, e):
    first = e.get()
    global f_num, math
    math = 3
    f_num = float(first)
    e.delete(0, tk.END)


def divide(root, e):
    first = e.get()
    global f_num, math
    math = 4
    f_num = float(first)
    e.delete(0, tk.END)


def equals(root, e):
    second_number = float(e.get())
    e.delete(0, tk.END)
    if math == 1:
        e.insert(0, f_num + second_number)
    elif math == 2:
        e.insert(0, f_num - second_number)
    elif math == 3:
        e.insert(0, f_num * second_number)
    else:
        if second_number == 0:
            e.insert(0, "Cannot Divide by Zero")
        else:
            e.insert(0, f_num / second_number)


def negate(root, e):
    value = float(e.get())
    e.delete(0, tk.END)
    e.insert(0, -1 * value)


def button_operator(root, e):
    pass


def main():
    root = tk.Tk()
    root.title("Simple Calculator")

    e = tk.Entry(root, width=35, borderwidth=5, bg="#ffffff")
    e.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

    # define buttons
    # 1
    button_clear = tk.Button(
        root, text="C", padx=40, pady=20, command=lambda: clear(root, e)
    )
    button_divide = tk.Button(
        root, text="÷", padx=40, pady=20, width=1, command=lambda: divide(root, e),
    )

    # 2
    button_7 = tk.Button(
        root, text="7", padx=40, pady=20, width=1, command=lambda: number(root, e, 7),
    )
    button_8 = tk.Button(
        root, text="8", padx=40, pady=20, width=1, command=lambda: number(root, e, 8),
    )
    button_9 = tk.Button(
        root, text="9", padx=40, pady=20, width=1, command=lambda: number(root, e, 9),
    )
    button_multiply = tk.Button(
        root, text="×", padx=40, pady=20, width=1, command=lambda: multiply(root, e),
    )

    # 3
    button_4 = tk.Button(
        root, text="4", padx=40, pady=20, width=1, command=lambda: number(root, e, 4),
    )
    button_5 = tk.Button(
        root, text="5", padx=40, pady=20, width=1, command=lambda: number(root, e, 5),
    )
    button_6 = tk.Button(
        root, text="6", padx=40, pady=20, width=1, command=lambda: number(root, e, 6),
    )
    buttom_subtract = tk.Button(
        root, text="-", padx=40, pady=20, width=1, command=lambda: subtract(root, e),
    )

    # 4
    button_1 = tk.Button(
        root, text="1", padx=40, pady=20, width=1, command=lambda: number(root, e, 1),
    )
    button_2 = tk.Button(
        root, text="2", padx=40, pady=20, width=1, command=lambda: number(root, e, 2),
    )
    button_3 = tk.Button(
        root, text="3", padx=40, pady=20, width=1, command=lambda: number(root, e, 3),
    )
    button_add = tk.Button(
        root, text="+", padx=40, pady=20, width=1, command=lambda: add(root, e),
    )

    # 5
    button_negation = tk.Button(
        root, text="+/-", padx=40, pady=20, width=1, command=lambda: negate(root, e),
    )
    button_0 = tk.Button(
        root, text="0", padx=40, pady=20, width=1, command=lambda: number(root, e, 0),
    )
    button_dot = tk.Button(
        root,
        text=".",
        padx=40,
        pady=20,
        width=1,
        command=lambda: dot(root, e),
    )
    button_equal = tk.Button(
        root, text="=", padx=40, pady=20, width=1, command=lambda: equals(root, e),
    )

    # arrange button on screen
    button_clear.grid(row=1, column=0, columnspan=3, sticky=tk.W + tk.E)
    button_divide.grid(row=1, column=3)

    button_7.grid(row=2, column=0)
    button_8.grid(row=2, column=1)
    button_9.grid(row=2, column=2)
    button_multiply.grid(row=2, column=3)

    button_4.grid(row=3, column=0)
    button_5.grid(row=3, column=1)
    button_6.grid(row=3, column=2)
    buttom_subtract.grid(row=3, column=3)

    button_1.grid(row=4, column=0)
    button_2.grid(row=4, column=1)
    button_3.grid(row=4, column=2)
    button_add.grid(row=4, column=3)

    button_negation.grid(row=5, column=0)
    button_0.grid(row=5, column=1)
    button_dot.grid(row=5, column=2)
    button_equal.grid(row=5, column=3)

    root.mainloop()


if __name__ == "__main__":
    main()
