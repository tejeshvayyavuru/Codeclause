import tkinter as tk
from tkinter import filedialog, messagebox, font

def open_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        with open(file_path, 'r') as file:
            text.delete('1.0', tk.END)
            text.insert(tk.END, file.read())

def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt")
    if file_path:
        with open(file_path, 'w') as file:
            file.write(text.get('1.0', tk.END))

def about():
    messagebox.showinfo("About", "Simple Text Editor\nCreated with Python and Tkinter\nV.Tejesh")

def change_font():
    selected_font = font.Font(family=font_family.get(), size=font_size.get())
    text.configure(font=selected_font)

def count_words():
    content = text.get('1.0', tk.END)
    words = content.split()
    messagebox.showinfo("Word Count", f"Total words: {len(words)}")

def clear_text():
    text.delete('1.0', tk.END)

def highlight_text():
    keyword = highlight_entry.get()
    if keyword:
        text.tag_remove("highlight", "1.0", tk.END)
        start = "1.0"
        while True:
            start = text.search(keyword, start, stopindex=tk.END)
            if not start:
                break
            end = f"{start}+{len(keyword)}c"
            text.tag_add("highlight", start, end)
            start = end

root = tk.Tk()
root.title("Text Editor")
 
window_width = 800
window_height = 500
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)
root.geometry(f"{window_width}x{window_height}+{x}+{y}")


text = tk.Text(root, font=("Arial", 12))
text.pack(expand=True, fill=tk.BOTH)


menu_bar = tk.Menu(root)
root.config(menu=menu_bar)


file_menu = tk.Menu(menu_bar, tearoff=False)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)


edit_menu = tk.Menu(menu_bar, tearoff=False)
menu_bar.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Undo", command=text.edit_undo)
edit_menu.add_command(label="Redo", command=text.edit_redo)


format_menu = tk.Menu(menu_bar, tearoff=False)
menu_bar.add_cascade(label="Format", menu=format_menu)
font_menu = tk.Menu(format_menu, tearoff=False)
format_menu.add_cascade(label="Font", menu=font_menu)


font_family = tk.StringVar(value="Arial")
font_family_menu = tk.Menu(font_menu, tearoff=False)
font_menu.add_cascade(label="Font Family", menu=font_family_menu)
font_family_menu.add_radiobutton(label="Arial", variable=font_family, value="Arial", command=change_font)
font_family_menu.add_radiobutton(label="Times New Roman", variable=font_family, value="Times New Roman", command=change_font)
font_family_menu.add_radiobutton(label="Courier New", variable=font_family, value="Courier New", command=change_font)


font_size = tk.IntVar(value=12)
font_size_menu = tk.Menu(font_menu, tearoff=False)
font_menu.add_cascade(label="Font Size", menu=font_size_menu)
font_size_menu.add_radiobutton(label="12", variable=font_size, value=12, command=change_font)
font_size_menu.add_radiobutton(label="14", variable=font_size, value=14, command=change_font)
font_size_menu.add_radiobutton(label="16", variable=font_size, value=16, command=change_font)


tools_menu = tk.Menu(menu_bar, tearoff=False)
menu_bar.add_cascade(label="Tools", menu=tools_menu)
tools_menu.add_command(label="Count Words", command=count_words)
tools_menu.add_command(label="Clear Text", command=clear_text)


search_menu = tk.Menu(menu_bar, tearoff=False)
menu_bar.add_cascade(label="Search", menu=search_menu)
highlight_menu = tk.Menu(search_menu, tearoff=False)
search_menu.add_cascade(label="Highlight", menu=highlight_menu)


highlight_entry = tk.StringVar()
highlight_menu.add_command(label="Highlight Text", command=highlight_text)
highlight_menu.add_separator()
highlight_menu.add_command(label="Clear Highlight", command=lambda: text.tag_remove("highlight", "1.0", tk.END))


about_menu = tk.Menu(menu_bar, tearoff=False)
menu_bar.add_cascade(label="About", menu=about_menu)
about_menu.add_command(label="About", command=about)

root.mainloop()
