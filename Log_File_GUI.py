from netmiko import ConnectHandler
import pandas as pd
import os
import tkinter as tk
from tkinter import filedialog, messagebox
import re

# Phrases to remove from output
phrases_to_remove = [
    "Note: If a log seems to disappear then it has probably rotated.",
    "use the index to specify the older log entries to be viewed."
]


# Function to run CLI command on the remote device
def run_command(host, username, password, command):
    try:
        remote_device = {
            'device_type': 'generic',  # Update this according to your device type
            'host': host,
            'username': username,
            'password': password,
            'port': 22,  # Optional, defaults to 22
            'secret': '',  # Optional, if your device requires an enable password
        }

        print("Connecting to the remote unit...")  # Debug log
        # Establish SSH connection
        connection = ConnectHandler(**remote_device)
        print("Connection established.")

        # Send command and capture output
        print(f"Executing command: {command}")  # Debug log
        output = connection.send_command(command)

        connection.disconnect()

        if output:
            print(f"Command output received.")
            return output
        else:
            print("No output received from the command.")
            return None

    except Exception as e:
        print(f"Error connecting or running command: {e}")
        return None


# Function to remove unwanted phrases from the output
def filter_output(output):
    filtered_output = []
    for line in output.splitlines():
        if not any(phrase in line for phrase in phrases_to_remove):
            filtered_output.append(line)
    return "\n".join(filtered_output)

################


def remove_illegal_characters(text):
    # Define a regex pattern that matches illegal XML characters
    illegal_characters = re.compile(r'[\x00-\x1F\x7F]')  # Matches control characters
    return illegal_characters.sub('', text)


#################

# Function to update Excel with new data
def update_excel(new_output, excel_file):
    print(f"Updating Excel file at: {excel_file}")  # Debug log
    cleaned_output = remove_illegal_characters(new_output)

    # Check if Excel file exists
    if os.path.exists(excel_file):
        print("Excel file exists, reading existing data...")  # Debug log
        # Read the existing Excel file
        df_existing = pd.read_excel(excel_file)
    else:
        print("Excel file does not exist, creating new...")  # Debug log
        # Create an empty DataFrame if file does not exist
        df_existing = pd.DataFrame(columns=['Output'])

    # Convert output into a list (one row for each line)
    new_data = new_output.splitlines()
    df_new = pd.DataFrame(new_data, columns=['Output'])

    # Check for duplicates and add only new entries
    df_combined = pd.concat([df_existing, df_new]).drop_duplicates(subset=['Output'])

    # Save updated data to Excel
    try:
        df_combined.to_excel(excel_file, index=False)
        print(f"Excel file updated successfully at {excel_file}.")
    except Exception as e:
        print(f"Error writing to Excel file: {e}")
        raise  # Re-raise the exception to see what exactly goes wrong


# Function to trigger the command execution and Excel update
def execute_command():
    host = host_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    command = command_entry.get()
    excel_file = excel_path.get()
    messagebox.showinfo("Success", "Command executed successfully!")

    if not host or not username or not password or not command or not excel_file:
        messagebox.showerror("Input Error", "All fields must be filled.")
        return

    output = run_command(host, username, password, command)
    if output:
        filtered_output = filter_output(output)
        update_excel(filtered_output, excel_file)
        messagebox.showinfo("Success", f"Command executed and Excel file updated at: {excel_file}")
    else:
        messagebox.showerror("Error", "No output captured or an error occurred.")


# Function to browse and select where to save the Excel file
def browse_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel files", "*.xlsx")])
    excel_path.set(file_path)


# Create GUI
root = tk.Tk()
root.title("Remote CLI Command Executor")




# Host IP entry
tk.Label(root, text="Host IP Address").grid(row=0, column=0, padx=10, pady=5)
host_entry = tk.Entry(root)
host_entry.grid(row=0, column=1, padx=10, pady=5)

# Username entry
tk.Label(root, text="Username").grid(row=1, column=0, padx=10, pady=5)
username_entry = tk.Entry(root)
username_entry.grid(row=1, column=1, padx=10, pady=5)

# Password entry
tk.Label(root, text="Password").grid(row=2, column=0, padx=10, pady=5)
password_entry = tk.Entry(root, show='*')
password_entry.grid(row=2, column=1, padx=10, pady=5)

# Command entry
tk.Label(root, text="Command").grid(row=3, column=0, padx=10, pady=5)
command_entry = tk.Entry(root)
command_entry.grid(row=3, column=1, padx=10, pady=5)

# Excel file path entry
tk.Label(root, text="Save Excel File").grid(row=4, column=0, padx=10, pady=5)
excel_path = tk.StringVar()
tk.Entry(root, textvariable=excel_path).grid(row=4, column=1, padx=10, pady=5)
tk.Button(root, text="Browse", command=browse_file).grid(row=4, column=2, padx=10, pady=5)

# Execute button
tk.Button(root, text="Execute", command=execute_command).grid(row=5, column=1, padx=10, pady=20)

root.mainloop()
