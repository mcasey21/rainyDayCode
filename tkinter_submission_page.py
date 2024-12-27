import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Grid Manager Demo")

def submit():
    # Create and place widgets using the grid manager
    label_username = tk.Label(root, text="Username:")
    label_password = tk.Label(root, text="Password:")
    entry_username = tk.Entry(root)
    entry_password = tk.Entry(root, show="*")  # Show '*' for password input
    button_submit = tk.Button(root, text="Submit", command=submit)

    # Grid layout configuration
    label_username.grid(row=0, column=0, sticky="E")  # Align to the right (East)
    label_password.grid(row=1, column=0, sticky="E")  # Align to the right (East)
    entry_username.grid(row=0, column=1)
    entry_password.grid(row=1, column=1)
    button_submit.grid(row=2, column=1, pady=10)  # Add some padding to the y-axis
    
    # Start the Tkinter event loop
    root.mainloop()

submit()
