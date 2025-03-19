import cv2
import pytesseract
from pytesseract import Output
import os

# Set the working directory to the script's directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Function to preprocess the image
def preprocess_image(image_path):
    # Load the image
    image = cv2.imread(image_path)
    
    # Check if the image was loaded successfully
    if image is None:
        print(f"Error: Unable to load image at {image_path}")
        print("Please check the file path and integrity.")
        return None
    
    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Apply thresholding to get a binary image
    _, binary = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)
    
    return binary

# Function to extract text from the image
def extract_text(image):
    if image is None:
        return
    
    # Use Tesseract to extract text
    custom_config = r'--oem 3 --psm 6'
    details = pytesseract.image_to_data(image, output_type=Output.DICT, config=custom_config)
    
    # Extract and print the text
    extracted_text = pytesseract.image_to_string(image, config=custom_config)
    print("Extracted Text:\n", extracted_text)
    
    # Optionally, you can also print the bounding boxes and confidence levels
    for i in range(len(details['text'])):
        if int(details['conf'][i]) > 60:  # Confidence threshold
            print(f"Text: {details['text'][i]}, Confidence: {details['conf'][i]}")

# Main function
def main():
    image_path = 'medical_record_image.jpg'
    print("Current Working Directory:", os.getcwd())
    print("Image Path:", os.path.abspath(image_path))
    
    preprocessed_image = preprocess_image(image_path)
    if preprocessed_image is not None:
        extract_text(preprocessed_image)

if __name__ == "__main__":
    main()