import tkinter as tk
import random
import string

# Create the window
window = tk.Tk()
window.title("Password Generator")

# Create the label to display the password
password_label = tk.Label(window, text="", font=("Arial", 18))
password_label.pack(pady=10)

# Create the input fields
length_label = tk.Label(window, text="Length:")
length_label.pack(pady=5)

length_entry = tk.Entry(window)
length_entry.pack(pady=5)

include_digits_var = tk.IntVar()
include_digits_checkbutton = tk.Checkbutton(window, text="Include digits", variable=include_digits_var)
include_digits_checkbutton.pack()

include_symbols_var = tk.IntVar()
include_symbols_checkbutton = tk.Checkbutton(window, text="Include symbols", variable=include_symbols_var)
include_symbols_checkbutton.pack()

# Create the generate password function
def generate_password():
    # Get the length of the password
    try:
        length = int(length_entry.get())
    except ValueError:
        password_label.config(text="Please enter a valid length.")
        return

    # Check that the length is within the valid range
    if length < 5 or length > 32:
        password_label.config(text="Password length must be between 5 and 32.")
        return

    # Determine which characters to include in the password
    include_letters = True
    include_digits = include_digits_var.get()
    include_symbols = include_symbols_var.get()

    # Generate the password
    characters = string.ascii_letters
    if include_digits:
        characters += string.digits
    if include_symbols:
        characters += string.punctuation

    password = "".join(random.choice(characters) for i in range(length))

    # Display the password
    password_label.config(text=password)

# Create the generate button
generate_button = tk.Button(window, text="Generate", command=generate_password)
generate_button.pack(pady=10)

# Run the window
window.mainloop()
