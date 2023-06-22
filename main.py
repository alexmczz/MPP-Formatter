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



import tkinter as tk
from tkinter import filedialog
import datetime
import csv


# Used to format the file name which is going to be the month day year followed by .csv
current_date = datetime.date.today()
formatted_date = current_date.strftime("%m%d%Y")


# Creates a tkinter window (drop box)
def handle_drop(event):
    file_path = filedialog.askopenfilename()  # Used to get the file path
    if file_path:
        file_name = file_path.split("/")[-1]  # Extract the file name from the path
        # Process the dropped file or use the file name as desired
        print("Dropped file:", file_name)
        # Used for debugging to ensure the correct file was selected

        # Read the input text file
        with open(file_path, 'r') as text_file:
            lines = text_file.readlines()

        # Remove leading/trailing whitespace and split the lines into columns
        rows = [line.strip().split('\t') for line in lines]

        # Remove the original header row
        header_row = rows.pop(0)

        # Sort rows based on the 'FeeTransaction' column as strings
        sorted_rows = sorted(rows, key=lambda x: x[0])

        # Insert the new header row
        new_header_row = ["FeeTransactionName", "Description", "StudentID", "Full", "Reduced", "Free", "DueDate",
                          "IssueDate", "AccountCode", "ExternalFeeID", "FundingAccountName", "NewFeesNotification",
                          "Rate Plan Name"]
        sorted_rows.insert(0, new_header_row)

        # Writing to the new file
        with open(f'{formatted_date}.csv', 'w', newline='') as mpp_fees_formatted:
            writer = csv.writer(mpp_fees_formatted)
            writer.writerows(sorted_rows)


window = tk.Tk()

# Create a label to act as the dropbox
drop_label = tk.Label(window, text="Drop File Here", font=("Arial", 14), padx=50, pady=70)
drop_label.pack()

# Bind the left mouse button click event to the label
drop_label.bind('<Button-1>', handle_drop)

window.mainloop()
