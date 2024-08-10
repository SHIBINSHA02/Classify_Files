import win32com.client
import os
from datetime import datetime
from hidden import *
# Initialize the WIA CommonDialog
wia = win32com.client.Dispatch("WIA.CommonDialog")

# Show the scanner selection dialog
scanner = wia.ShowSelectDevice(1, False, True)  # 1 corresponds to ScannerDeviceType

if scanner is None:
    print("No scanner selected.")
else:
    print("Selected scanner:", scanner.Properties("Name").Value)

    # Scan the image directly (acquire the image from the scanner)
    image = scanner.Items[1].Transfer()

    # Set the directory where you want to save the image
    save_directory = file_direct

    # Ensure the directory exists (create it if it doesn't)
    os.makedirs(save_directory, exist_ok=True)

    # Create a unique filename using a timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    image_file = os.path.join(save_directory, f"scanned_image_{timestamp}.jpg")

    # Save the scanned image
    image.SaveFile(image_file)
    print(f"Image saved as {image_file}")
