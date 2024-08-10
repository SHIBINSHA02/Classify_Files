import win32com.client
import os
from datetime import datetime
import hidden
import time

def scan_images(scanner, save_directory, num_scans):
    # Ensure the directory exists (create it if it doesn't)
    os.makedirs(save_directory, exist_ok=True)

    for i in range(num_scans):
        input(f"Please change the page and press Enter to start scan {i + 1}...")
        # Scan the image directly (acquire the image from the scanner)
        image = scanner.Items[1].Transfer()
        image_file = os.path.join(save_directory, f"scanned_image_{i + 1}.jpg")

        # Save the scanned image
        image.SaveFile(image_file)
        print(f"Scan {i + 1} saved as {image_file}")

def main():
    # Initialize the WIA CommonDialog
    wia = win32com.client.Dispatch("WIA.CommonDialog")

    # Show the scanner selection dialog
    scanner = wia.ShowSelectDevice(1, False, True)  # 1 corresponds to ScannerDeviceType

    if scanner is None:
        print("No scanner selected.")
        return

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    print("Selected scanner:", scanner.Properties("Name").Value)

    # Set the directory where you want to save the images
    save_directory = f"{hidden.file_direct}/Date{timestamp}"
    
    # Number of scans to perform
    num_scans = int(input("Total Count of copies:") )# Change this to the number of scans you want

    # Perform the scans and save the images
    scan_images(scanner, save_directory, num_scans)

if __name__ == "__main__":
    main()
