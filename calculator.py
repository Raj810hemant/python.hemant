import tkinter as tk

# Function to handle button clicks
def button_click(event):
    current_text = entry.get()
    button_text = event.widget.cget("text")

    if button_text == "=":
        try:
            result = eval(current_text)
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif button_text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, button_text)

# Create the main window
window = tk.Tk()
window.title("Calculator")

# Create an entry widget for displaying the input and result
entry = tk.Entry(window, font=("Arial", 20))
entry.grid(row=0, column=0, columnspan=4)

# Define the button labels
buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "=", "+",
    "C"
]

# Create and place the calculator buttons
row, col = 1, 0
for button_text in buttons:
    button = tk.Button(window, text=button_text, font=("Arial", 20), padx=20, pady=20)
    button.grid(row=row, column=col)
    button.bind("<Button-1>", button_click)
    col += 1
    if col > 3:
        col = 0
        row += 1

# Start the main loop
window.mainloop()
