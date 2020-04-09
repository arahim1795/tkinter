import tkinter as tk


def clicked(root, value):
    global my_label
    my_label = tk.Label(root, text=value)
    my_label.pack()


def main():
    root = tk.Tk()
    root.title("Radio Buttons")

    # # can be IntVar(), StringVar()
    # r = tk.IntVar()
    # r.set(0)
    # tk.Radiobutton(root, text="Option 1", variable=r, value=0, command=lambda: clicked(root, r.get())).pack()
    # tk.Radiobutton(root, text="Option 2", variable=r, value=1, command=lambda: clicked(root, r.get())).pack()
    # b_1 = tk.Button(root, text="Click Me!", command=lambda: clicked(root, r.get()))
    # b_1.pack()
    # global my_label
    # my_label = tk.Label(root, text=r.get())
    # my_label.pack()

    toppings = [
        ("Pepperoni", "Pepperoni"),
        ("Cheese", "Cheese"),
        ("Mushroom", "Mushroom"),
        ("Onion", "Onion"),
    ]
    pizza = tk.StringVar()
    pizza.set("Cheese")

    for text, topping in toppings:
        tk.Radiobutton(root, text=text, variable=pizza, value=topping).pack(anchor=tk.W)

    b_1 = tk.Button(root, text="Click Me!", command=lambda: clicked(root, pizza.get()))
    b_1.pack()

    root.mainloop()


if __name__ == "__main__":
    main()
