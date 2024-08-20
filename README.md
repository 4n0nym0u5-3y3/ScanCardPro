# 🌟 ScanCard Pro

## 📚 Overview

**ScanCard Pro** is a powerful and user-friendly tool designed to help you digitize and organize information from business cards with ease. Simply upload an image of a business card, and ScanCard Pro will extract the text, identify key fields like name, email, and phone number, and allow you to save the information in various formats, including PDF and CSV. 

### 🚀 Features

- **Easy Upload**: Upload images in `.jpg`, `.jpeg`, or `.png` formats.
- **Fast and Accurate OCR**: Leverages Tesseract OCR to extract text from business card images.
- **Field Detection**: Automatically detects and formats key information such as Name, Email, and Phone Number.
- **Export Options**:
  - Save extracted text as a PDF document.
  - Export detected fields as a CSV file for easy import into your contact management system.
- **User-Friendly Interface**: Intuitive GUI built with Python's `tkinter` library.
- **Cross-Platform**: Compatible with Windows, macOS, and Linux.

## 🛠️ Installation

### Prerequisites

- Python 3.7 or higher
- Pip (Python package installer)

### Setup

1. **Clone the Repository**:
    ```sh
    git clone https://github.com/yourusername/scancard-pro.git
    cd scancard-pro
    ```

2. **Install Dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

3. **Download and Install Tesseract**:
    - **Windows**: [Tesseract Installer](https://github.com/tesseract-ocr/tesseract)
    - **macOS**: Install via Homebrew
      ```sh
      brew install tesseract
      ```
    - **Linux**: Install via apt-get
      ```sh
      sudo apt-get install tesseract-ocr
      ```

4. **Run ScanCard Pro**:
    ```sh
    python scancard_pro.py
    ```

## ✨ How It Works

1. **Upload Image**: Select and upload an image of a business card.
2. **Scan & Convert**: The application will process the image and extract the text.
3. **Review & Export**: Review the extracted information and export it as PDF or CSV.

## 🎨 Customization

Feel free to customize ScanCard Pro to suit your needs:
- **Themes**: Modify the color scheme in the `scancard_pro.py` file.
- **Field Detection**: Enhance the `detect_fields` function to better match your requirements.



### Note:
Replace placeholder images, email, and links with actual content relevant to your project.

This `README.md` provides a comprehensive overview of your project while maintaining clarity and organization.
