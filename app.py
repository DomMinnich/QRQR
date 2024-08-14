import qrcode
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import filedialog, messagebox
import random
import string
import os

def generate_random_title(length=10):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

def generate_qr_code(text, image_path=None):
    random_filename = generate_random_title() + ".png"
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(text)
    qr.make(fit=True)
    qr_img = qr.make_image(fill_color="black", back_color="white").convert('RGB')

    if image_path:
        icon = Image.open(image_path)
        qr_width, qr_height = qr_img.size
        icon_size = qr_width // 4
        icon = icon.resize((icon_size, icon_size), Image.LANCZOS)
        x_pos = (qr_width - icon_size) // 2
        y_pos = (qr_height - icon_size) // 2
        qr_img.paste(icon, (x_pos, y_pos))

    qr_img.save(random_filename)
    return random_filename

def select_image():
    image_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp")])
    image_label.config(text=image_path)

def generate_qr():
    text = text_entry.get()
    image_path = image_label.cget("text")
    if not text:
        messagebox.showwarning("Input Error", "Please enter the text or URL for the QR code.")
        return
    
    try:
        output_file = generate_qr_code(text, image_path if image_path else None)
        img = Image.open(output_file)
        img.thumbnail((200, 200))
        img = ImageTk.PhotoImage(img)
        result_label.config(image=img)
        result_label.image = img
        full_path = os.path.abspath(output_file)
        messagebox.showinfo("Success", f"QR Code generated and saved as {full_path}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to generate QR Code: {str(e)}")

# Setting up the GUI
root = tk.Tk()
root.title("QR Code Generator")
root.geometry("600x600")
root.configure(bg="#0e0e0e")  # Dark background

# Style configuration
style_config = {
    "font": ("Helvetica", 14, "bold"),
    "bg": "#0e0e0e",  # Dark background
    "fg": "#00ffff",  # Neon cyan text
}

# Animations
def fade_in(widget, final_color="#00ffff", step=2):
    color = widget.cget("fg")
    rgb = [int(color[i:i+2], 16) for i in (1, 3, 5)]
    r, g, b = rgb[0], rgb[1], rgb[2]
    fr, fg, fb = [int(final_color[i:i+2], 16) for i in (1, 3, 5)]
    
    if (r, g, b) != (fr, fg, fb):
        r += step if r < fr else -step if r > fr else 0
        g += step if g < fg else -step if g > fg else 0
        b += step if b < fb else -step if b > fb else 0
        color = f"#{r:02x}{g:02x}{b:02x}"
        widget.config(fg=color)
        widget.after(30, fade_in, widget, final_color, step)

def on_hover(event):
    fade_in(event.widget, final_color="#ff6600")

def on_leave(event):
    fade_in(event.widget, final_color="#00ffff")

# Text input for QR code
text_label = tk.Label(root, text="Enter text or URL for the QR code:", **style_config)
text_label.pack(pady=10)
text_entry = tk.Entry(root, width=50, font=("Helvetica", 12), bg="#1f1f1f", fg="#00ffff", insertbackground="#00ffff")
text_entry.pack(pady=10)

# Button to select an image
image_label = tk.Label(root, text="No image selected", **style_config)
select_button = tk.Button(root, text="Select Image", command=select_image, font=("Helvetica", 12), bg="#1f1f1f", fg="#00ffff", activebackground="#333333", activeforeground="#00ffff")
select_button.pack(pady=10)
image_label.pack(pady=10)

# Button to generate the QR code
generate_button = tk.Button(root, text="Generate QR Code", command=generate_qr, font=("Helvetica", 14, "bold"), bg="#1f1f1f", fg="#00ffff", activebackground="#333333", activeforeground="#00ffff")
generate_button.pack(pady=20)

# Label to display the generated QR code
result_label = tk.Label(root, bg="#0e0e0e")
result_label.pack(pady=10)

# Hover effect on buttons
select_button.bind("<Enter>", on_hover)
select_button.bind("<Leave>", on_leave)
generate_button.bind("<Enter>", on_hover)
generate_button.bind("<Leave>", on_leave)

# Custom cursor and animation effect
root.config(cursor="hand2")
root.bind("<Enter>", lambda e: root.config(cursor="crosshair"))
root.bind("<Leave>", lambda e: root.config(cursor="hand2"))

# Developer Credit
credit_label = tk.Label(root, text="Developed by Dominic Minnich", font=("Helvetica", 10), bg="#0e0e0e", fg="#ff6600")
credit_label.pack(side="bottom", pady=10)

# Start the GUI event loop
root.mainloop()
