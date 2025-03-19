# CPE124-MedicalHealthRecordsRetrieval-Group8
This repository contains a Medical Health Record OCR Extractor using OpenCV and Tesseract. It extracts text from printed medical record images, with preprocessing and error handling for file paths and image integrity. 

## Features

- **Image Preprocessing:** Converts the image to grayscale and applies thresholding to improve OCR accuracy.
- **Text Extraction:** Uses Tesseract OCR to extract text from the preprocessed image.
- **Error Handling:** Includes checks for file path validity and image integrity.

## Requirements

- Python 3.x
- OpenCV (`opencv-python`)
- Tesseract OCR (`pytesseract`)
- Tesseract-OCR installed on the system

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/your-username/medical-health-record-ocr.git
   cd medical-health-record-ocr
