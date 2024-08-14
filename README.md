# QR Code Generator

A simple and interactive QR Code Generator built using Python's Tkinter library for the GUI, `qrcode` for generating QR codes, and `Pillow` for image processing.

![image](https://github.com/user-attachments/assets/b7dddd65-b941-4e6b-bfcd-47ab908a9343)


## Features
- **Text/URL Input:** Enter text or a URL to generate a QR code.
- **Image Embedding:** Optionally embed an image in the center of the QR code.
- **Random File Naming:** Generated QR codes are saved with unique filenames.
- **Custom Styling and Animations:** Dark theme with animated text effects.

## Installation

### Prerequisites
- Python 3.x
- Required Python libraries:
  - `qrcode`
  - `Pillow`
  - `tkinter` (usually included with Python)

Install the required libraries using pip:
```bash
pip install qrcode[pil] pillow
```

### Running the Application
1. Clone or download the repository.
2. Run the script:
   ```bash
   python qr_code_generator.py
   ```
3. The application window will open, and you can start generating QR codes.

## Usage
1. **Enter Text/URL:** Input the text or URL for the QR code.
2. **Select an Image (Optional):** Click "Select Image" to embed an image.
3. **Generate QR Code:** Click "Generate QR Code" to create and display the QR code.
4. **Save and View:** The QR code is saved with a random filename, and you'll be notified of the save location.

## GUI Details
- **Theme:** Dark background with neon cyan text and orange hover effects.
- **Fade-in Animation:** Smooth text color transition on hover.
- **Custom Cursor:** Crosshair cursor on hover.

## License
This project is open-source and available for free use. Contributions are welcome.
