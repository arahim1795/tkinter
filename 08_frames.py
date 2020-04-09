import tkinter as tk


def main():
    root = tk.Tk()
    root.title("Frames")

    frame = tk.LabelFrame(root, text="This is a Frame", padx=50, pady=50)
    frame.pack(padx=10, pady=10)

    b = tk.Button(frame, text="This is a Button")
    b2 = tk.Button(frame, text="A Second Button")
    b.grid(row=0, column=0)
    b2.grid(row=1, column=0)

    root.mainloop()


if __name__ == "__main__":
    main()
