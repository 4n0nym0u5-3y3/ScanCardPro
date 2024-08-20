import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter.ttk import Progressbar
from PIL import Image, ImageTk
import pytesseract
from pytesseract import Output
import os
from fpdf import FPDF
import csv

class ScanCardPro:
    def __init__(self, root):
        self.root = root
        self.root.title("ScanCard Pro")
        self.root.geometry("800x500")
        self.root.minsize(600, 500)
        self.filename = None

        # Initialize Tesseract OCR
        self.tesseract_path = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
        pytesseract.pytesseract.tesseract_cmd = self.tesseract_path
        
        self.create_widgets()

    def create_widgets(self):
        # Header Labels
        tk.Label(self.root, text="ScanCard Pro", bg="#FAE3C6", fg="#1C2833", font=("Arial", 18)).pack(fill="x")
        tk.Label(self.root, text="Upload an image file to scan", bg="#FAE3C6", fg="#1C2833", font=("Arial", 12, "italic")).pack(fill="x")
        
        # File Upload Frame
        upload_frame = tk.Frame(self.root, bg="white")
        upload_frame.pack(pady=10, fill="x")
        
        tk.Label(upload_frame, text="Select Image:", bg="white", font=("Arial", 14)).pack(side="left", padx=10)
        tk.Button(upload_frame, text="Browse", command=self.upload_image, bg="#FFA07A", font=("Arial", 12)).pack(side="left", padx=10)
        
        # Status Label
        self.status_label = tk.Label(self.root, text="No image uploaded", bg="white", fg="red", font=("Arial", 12))
        self.status_label.pack()

        # Progress Bar
        self.progress = Progressbar(self.root, orient="horizontal", length=300, mode="determinate")
        self.progress.pack(pady=10)

        # Text Area for Displaying OCR Result
        self.text_area = tk.Text(self.root, height=10, font=("Arial", 14))
        self.text_area.pack(pady=10, fill="x")
        self.text_area.insert("1.0", "OCR results will be displayed here...")

        # Convert and Export Button Frame
        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=10)
        tk.Button(button_frame, text="Scan and Convert", command=self.convert_image, bg="#FFA07A", font=("Arial", 14)).pack(side="left", padx=5)
        tk.Button(button_frame, text="Export as PDF", command=self.export_pdf, bg="#FFA07A", font=("Arial", 14)).pack(side="left", padx=5)
        tk.Button(button_frame, text="Export as CSV", command=self.export_csv, bg="#FFA07A", font=("Arial", 14)).pack(side="left", padx=5)

        # Footer Labels
        tk.Label(self.root, text="© 2024 ScanCard Pro", bg="#1C2833", fg="white", font=("Arial", 10)).pack(side="bottom", fill="x")
        tk.Label(self.root, text="Developed by Your Name", bg="#1C2833", fg="white", font=("Arial", 10, "italic")).pack(side="bottom", fill="x")

    def upload_image(self):
        self.filename = filedialog.askopenfilename(
            title="Select an Image",
            filetypes=[("Image files", "*.jpg;*.jpeg;*.png")]
        )
        if self.filename:
            self.status_label.config(text="Image uploaded successfully", fg="green")
        else:
            self.status_label.config(text="No image uploaded", fg="red")
    
    def convert_image(self):
        if not self.filename:
            messagebox.showwarning("Warning", "Please upload an image first")
            return
        
        try:
            self.status_label.config(text="Scanning image...", fg="blue")
            self.progress.start()
            
            # Perform OCR
            text = pytesseract.image_to_string(self.filename)

            # Display result in the text area
            self.text_area.delete("1.0", tk.END)
            self.text_area.insert("1.0", text)
            
            self.status_label.config(text="Scan complete", fg="green")
            self.progress.stop()
        except Exception as e:
            messagebox.showerror("Error", str(e))
            self.status_label.config(text="Scan failed", fg="red")
            self.progress.stop()
    
    def export_pdf(self):
        if not self.filename:
            messagebox.showwarning("Warning", "Please scan an image first")
            return

        save_path = filedialog.asksaveasfilename(
            defaultextension=".pdf",
            filetypes=[("PDF files", "*.pdf")],
            title="Save as PDF"
        )
        if save_path:
            text = self.text_area.get("1.0", tk.END)
            self.save_as_pdf(text, save_path)
            messagebox.showinfo("Success", f"Exported as {save_path}")

    def export_csv(self):
        if not self.filename:
            messagebox.showwarning("Warning", "Please scan an image first")
            return

        save_path = filedialog.asksaveasfilename(
            defaultextension=".csv",
            filetypes=[("CSV files", "*.csv")],
            title="Save as CSV"
        )
        if save_path:
            fields = self.detect_fields(self.filename)
            self.save_as_csv(fields, save_path)
            messagebox.showinfo("Success", f"Exported as {save_path}")

    def save_as_pdf(self, text, file_path):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.multi_cell(0, 10, text)
        pdf.output(file_path)

    def save_as_csv(self, fields, file_path):
        with open(file_path, 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fields.keys())
            writer.writeheader()
            writer.writerow(fields)

    def detect_fields(self, image_path):
        data = pytesseract.image_to_data(image_path, output_type=Output.DICT)
        fields = {
            'name': '',
            'email': '',
            'phone': ''
        }
        # Placeholder logic for detecting fields (this is an example)
        for i in range(len(data['text'])):
            if "@" in data['text'][i]:
                fields['email'] = data['text'][i]
            elif data['text'][i].replace('-', '').isdigit():
                fields['phone'] = data['text'][i]
            elif fields['name'] == '':
                fields['name'] = data['text'][i]
        return fields

if __name__ == "__main__":
    root = tk.Tk()
    app = ScanCardPro(root)
    root.mainloop()
