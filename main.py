# DISCLAIMER NOTICE:
# This software is provided as-is without any warranty. It is intended to assist in processing and preparing files to be uploaded to the My Payments Plus system. 
# While efforts have been made to ensure its accuracy and functionality, the developer does not guarantee the completeness, reliability, or suitability of this software for any purpose.
#
# This software is being developed specifically for the Amity Region 5 District, but it is offered as free software for anyone to use. 
# Users are solely responsible for verifying the results and taking appropriate actions based on the processed files. 
# This software is still under development and being tested
#
# The developer and the Amity Region 5 District are not liable for any damages or losses arising from the use of this software.
#
# It is strongly recommended to thoroughly review and validate the output files before uploading them to the Payments Plus system or any other payment processing platform. 
# Users should exercise caution and perform necessary tests to ensure the accuracy and integrity of the data.
#
# By using this software, you acknowledge and agree to the above terms and conditions. If you do not agree to these terms, you should refrain from using this software.
#
# For further inquiries or assistance, please contact the developer at alex.mcpadden@gmail.com


import tkinter as tk
from tkinter import filedialog
import datetime
import csv


#used to format the file name which is going to be the month day year followed by .csv
current_date = datetime.date.today()
formatted_date = current_date.strftime("%m%d%Y")


#creates a tkinter window(drop box)
def handle_drop(event):
    file_path = filedialog.askopenfilename() #used to get the file path 
    if file_path:
        file_name = file_path.split("/")[-1]  # Extract the file name from the path
        # Process the dropped file or use the file name as desired
        print("Dropped file:", file_name)
        # ^^used for debugging to ensure correct file was selected^^
        
        #reading selected file
        with open(file_path, 'r') as mpp_fees:
            reader = csv.DictReader(mpp_fees) #reads whatever file that is going to be processed/formatted
            fieldnames = reader.fieldnames or [] #for the new formated file
            
            
            #writing to new file
            with open(f'{formatted_date}.csv', 'w', newline='') as mpp_fees_formatted:
                writer = csv.DictWriter(mpp_fees_formatted, fieldnames=fieldnames)
                writer.writeheader()  # Write the header row
                writer.writerows(reader)  # Write the remaining rows

window = tk.Tk()

# Create a label to act as the dropbox
drop_label = tk.Label(window, text="Drop File Here", font=("Arial", 14), padx=20, pady=10)
drop_label.pack()

# Bind the left mouse button click event to the label
drop_label.bind('<Button-1>', handle_drop)

window.mainloop()
