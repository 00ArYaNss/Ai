import cv2
import numpy as np

def resize_image(input_path, output_path, width=1500, height=900):
    image = cv2.imread(input_path)
    if image is None:
        print("Error: Image not loaded.")
        return

    resized_image = cv2.resize(image, (width, height))

    for quality in range(100, 0, -1):
        success = cv2.imwrite(output_path, resized_image, [cv2.IMWRITE_WEBP_QUALITY, quality])
        if success:
        
            if 100 * 1024 <= os.path.getsize(output_path) <= 200 * 1024:
                print(f"Image saved successfully with quality {quality}")
                break
    else:
        print("Could not save the image within the desired file size range.")

if __name__ == "__main__":
    import os
    input_path = r"C:\Users\sahua\OneDrive\Desktop\Pics\resize.png"  
    output_path = r"C:\Users\sahua\OneDrive\Desktop\test.webp"  

    resize_image(input_path, output_path)
