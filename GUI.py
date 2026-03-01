import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from Business_Logic import Business_logic


def select_file(var, label):
    """Opens a file dialog and updates the provided StringVar and Label."""
    path = filedialog.askopenfilename()
    if path:
        var.set(path)
        # Show only the last 30 characters for UI cleanliness
        display_name = (path[:27] + '...') if len(path) > 30 else path
        label.config(text=f"Selected: {display_name}", fg="green")

def run_main_logic(p1, p2, month):
    """Validates inputs and executes the core script logic."""
    if not p1 or not p2:
        messagebox.showerror("Error", "Please select BOTH files before running.")
        return

    if not month or "Select" in month:
        messagebox.showwarning("Warning", "Please select a month from the dropdown.")
        return

    print(f"Making {month} reports...")
    Business_logic(month, p1, p2)
    messagebox.showinfo("Success", f"Finished making reports!")

    root.destroy()

# --- Root Window Setup ---
root = tk.Tk()
root.title("Report script")
root.geometry("450x450") # Slightly taller to accommodate the new button

# --- Variables ---
file_path1 = tk.StringVar()
file_path2 = tk.StringVar()
month_var = tk.StringVar()
months_list = [f"{i}" for i in range(1, 13)]

# --- UI Layout ---

# Month Selection
tk.Label(root, text="Step 1: Select Reporting Month", font=("Arial", 10, "bold")).pack(pady=(20, 5))
month_dropdown = ttk.Combobox(root, textvariable=month_var, values=months_list, state="readonly")
month_dropdown.set("Select Month")
month_dropdown.pack()

# File Selection Section
tk.Label(root, text="Step 2: Select Revenue Report for Selected Month.", font=("Arial", 10, "bold")).pack(pady=(20, 5))

btn1 = tk.Button(root, text="Browse File 1", command=lambda: select_file(file_path1, lbl1))
btn1.pack()

lbl1 = tk.Label(root, text="No file selected", fg="grey", font=("Arial", 8))
lbl1.pack()

tk.Label(root, text="Step 3: Select Customer Database.", font=("Arial", 10, "bold")).pack(pady=(20, 5))

btn2 = tk.Button(root, text="Browse File 2", command=lambda: select_file(file_path2, lbl2))
btn2.pack(pady=(10, 0))
lbl2 = tk.Label(root, text="No file selected", fg="grey", font=("Arial", 8))
lbl2.pack()

# Buttons that will run script
run_btn = tk.Button(root, text="Create Revenue Report", bg="#2ecc71", fg="white", font=("Arial", 12, "bold"),
                    command=lambda: run_main_logic(file_path1.get(), file_path2.get(), month_var.get()))
run_btn.pack(pady=(30, 10))

#Exit Button
exit_btn = tk.Button(root, text="Exit Application", fg="red", command=root.destroy)
exit_btn.pack(pady=10)

root.mainloop()