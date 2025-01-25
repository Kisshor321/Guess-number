import tkinter as tk
from tkinter import messagebox

# Create binary bit tables for numbers 1–32
tables = []
for bit in range(5):  # 5 binary bit positions
    table = [n for n in range(1, 33) if (n & (1 << bit)) > 0]  # Numbers where the bit is 1
    tables.append(table)

# Initialize variables
current_table_index = 0
common_numbers = set(range(1, 33))  # Start with all numbers
total = 0  # Total to store the sum of top-left numbers
no_count = 0  # Count the number of times "No" is clicked


def show_table(index):
    """Display the current 4x4 table corresponding to the given index."""
    # Clear the table area
    for widget in table_frame.winfo_children():
        widget.destroy()

    # Get the table data (16 numbers per 4x4 table)
    numbers = tables[index]
    table_data = [numbers[i:i + 4] for i in range(0, len(numbers), 4)]  # Split into rows of 4

    # Update the table number display
    table_number_label.config(text=f"Table {index + 1} of {len(tables)}")

    # Create a 4x4 grid of labels
    for i, row in enumerate(table_data):
        for j, num in enumerate(row):
            label = tk.Label(table_frame, text=str(num), width=5, height=2, borderwidth=1, relief="solid",
                             font=("Arial", 14))
            label.grid(row=i, column=j, padx=5, pady=5)


def on_yes_button_click():
    """Add the top-left number to the total, move to the next table."""
    global current_table_index, total

    try:
        # Add the top-left number of the current table to the total
        total += tables[current_table_index][0]

        # Move to the next table
        current_table_index += 1
        if current_table_index < len(tables):
            show_table(current_table_index)
        else:
            # Display the final result
            result_label.config(text=f"Your number: {total}")
    except IndexError:
        messagebox.showinfo("Invalid", "This is the last table.")


def on_no_button_click():
    """Increment the no_count and move to the next table."""
    global current_table_index, no_count, total

    no_count += 1
    
    if no_count == 5:
        result_label.config(text=f"Your number: 32")
        return
    if current_table_index == 4:  # Show total only when at the 5th table (index 4)
        result_label.config(text=f"Your number: {total}")
        return
    try:
        # Move to the next table
        current_table_index += 1
        if current_table_index < len(tables):
            show_table(current_table_index)
    except IndexError:
        messagebox.showinfo("Invalid", "This is the last table.")





# Create the main Tkinter window
root = tk.Tk()
root.title("Binary Bit Position Game")
root.geometry("500x500")
root.resizable(False, False)
label=tk.Label(root,text="Guess the number",font=("Arial", 14))
label.pack()
# Label to display the current table number
table_number_label = tk.Label(root, text="", font=("Arial", 14))
table_number_label.pack(pady=10)

# Create a frame to display the current table
table_frame = tk.Frame(root)
table_frame.pack(pady=20)

# Create Yes and No buttons
yes_button = tk.Button(root, text="Yes", width=10, command=on_yes_button_click, bg="green", fg="white")
no_button = tk.Button(root, text="No", width=10, command=on_no_button_click, bg="red", fg="white")


yes_button.pack(side=tk.LEFT, padx=10)
no_button.pack(side=tk.RIGHT, padx=10)

# Create a label to display the result
result_label = tk.Label(root, text="", font=("Arial", 16))
result_label.pack(pady=20)

# Show the first table
show_table(current_table_index)

# Run the Tkinter event loop
root.mainloop()
