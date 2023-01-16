import tkinter as tk

border_effects = {
    "flat": tk.FLAT,
    "sunken": tk.SUNKEN,
    "raised": tk.RAISED,
    "groove": tk.GROOVE,
    "ridge": tk.RIDGE,
}

def handle_button_press():
    print("debug", lbl_out["text"])
    lbl_out["text"]="ABCD-OUTPUT"

window = tk.Tk()
window.rowconfigure([0,1,2], minsize=50, weight=1)
window.columnconfigure([0, 1, 2,3, 4, 5], minsize=50, weight=1)

lbl_name = tk.Label(
    master=window,
    text="Easy Password Generator",
    width=100,
    height=5,
).grid(row=1, column=4, sticky="nsew")

btn_generate = tk.Button(
    master=window,
    text="Generate Password",
    width=25,
    height=5,
    relief=border_effects["raised"],
    borderwidth=5,
    command=handle_button_press
).grid(row=2, column=1, sticky="nsew")

entry = tk.Entry(
    master=window,
    width=5,
    relief=border_effects["raised"],
    borderwidth=1
).grid(row=2, column=2, sticky="nsew")

lbl_out = tk.Label(
    master=window,
    text="Your Password",
    width=25,
    height=5,
).grid(row=2, column=3, sticky="nsew")




window.mainloop()