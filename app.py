import tkinter as tk
from password_checker import check_strength
from generator import generate_password

def analyze():
    pwd = entry.get()
    strength, entropy, _ = check_strength(pwd)
    result.config(text=f"Strength: {strength} | Entropy: {entropy}")

def generate():
    pwd = generate_password()
    entry.delete(0, tk.END)
    entry.insert(0, pwd)

root = tk.Tk()
root.title("Cyber Password Toolkit")

entry = tk.Entry(root, width=30)
entry.pack(pady=10)

btn_analyze = tk.Button(root, text="Analyze", command=analyze)
btn_analyze.pack()

btn_generate = tk.Button(root, text="Generate Password", command=generate)
btn_generate.pack()

result = tk.Label(root, text="")
result.pack(pady=10)

root.mainloop()
