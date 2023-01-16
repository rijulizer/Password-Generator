from password_generator import PasswordGenerator
import tkinter as tk
import tkinter.messagebox

border_effects = {
    "flat": tk.FLAT,
    "sunken": tk.SUNKEN,
    "raised": tk.RAISED,
    "groove": tk.GROOVE,
    "ridge": tk.RIDGE,
}

def handle_button_press():
    print("input - ", entry_params.get())
    if entry_params.get() in ['', ' ', None, "Null"]: #  not none
        print("case -1")
        pg = PasswordGenerator(16)
    else:
        print("case -2")
        pg = PasswordGenerator(int(entry_params.get()))#  none case
    try:
        pg.read_titles()
    except:
        tk.messagebox.showerror(title='Error', message='Could not load data')
    password = pg.generate()
    tk.messagebox.showinfo(title="password", message=f"New Password - {password}")
    print("password is - ", password)
    lbl_out["text"] = password

window = tk.Tk()
window.rowconfigure([0,1,2], minsize=50, weight=1)
window.columnconfigure([0, 1, 2,3, 4, 5], minsize=10, weight=1)

lbl_name = tk.Label(
    master=window,
    text="Easy Password Generator",
    width=100,
    height=5,
).grid(row=1, column=4)

btn_generate = tk.Button(
    master=window,
    text="Generate Password",
    width=25,
    height=5,
    relief=border_effects["raised"],
    borderwidth=5,
    command=handle_button_press
).grid(row=2, column=1, sticky="nsew")

lbl_argument = tk.Label(
    master=window,
    text="Min Password length",
    width=25,
    height=5,
).grid(row=2, column=2)
entry_params = tk.Entry(
    master=window,
    width=10,
    relief=border_effects["raised"],
    borderwidth=1
)
param_input = entry_params.get()
entry_params.grid(row=2, column=3)

lbl_out = tk.Label(
    master=window,
    text="Your Password",
    width=25,
    height=5,
)
lbl_out.grid(row=2, column=4)

window.mainloop()
