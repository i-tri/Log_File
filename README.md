# Remote CLI Command Executor with Excel Logging

This Python project connects to remote devices via SSH using Netmiko, executes CLI commands, and logs the results into an Excel file. 
If you run the script again and use the same Excel file as output, the script will only update the Excel file with changed information.
It features a graphical user interface (GUI) to input the required connection details, the CLI command, and the location to save the Excel file.

## Features

- Execute CLI commands on remote devices via SSH.
- Capture command output and store it in an Excel file.
- GUI to input:
  - Host IP address
  - Username and Password
  - Command to execute
  - Excel file save location
- Automatic filtering of unwanted phrases from the output.
- Prevents duplicate entries in the Excel file.

## Prerequisites

Before running the project, ensure you have the following installed:

- **Python 3.7+**
- **Netmiko**: For SSH connections.
- **pandas**: For Excel file manipulation.
- **openpyxl**: For reading/writing Excel files.
- **Tkinter**: For GUI creation.

You can install the required packages using `pip`:

```bash
pip install netmiko pandas openpyxl
```

**Installation**
1. Clone the repository:

```bash
git clone https://github.com/i-tri/Log_File.git
```
2. Navigate to the project directory:

```bash
cd repository-name
```

3. Run the project using Python:

```bash
python cli_to_excel_gui.py
```
**Usage**
**GUI Interface**
When you run the script, a GUI will appear prompting you to fill in the following fields:

  - **Host IP Address**: The IP address of the remote device.
  - **Username**: The username for SSH login.
  - **Password**: The password for SSH login (hidden while typing).
  - **Command**: The CLI command you wish to execute on the remote device.
  - **Excel File Save Location**: Select or specify the path to save the Excel file.  
After providing the inputs, click the **Execute** button to run the command. The output will be logged in the specified Excel file.


## Screenshots

### GUI prompting for information:
<img width="245" alt="Log_File_GUI_Blank" src="https://github.com/user-attachments/assets/957d2442-878b-4a28-8964-b7d63a1a7d3c">

### GUI example
<img width="248" alt="Log_File_GUI_Filled" src="https://github.com/user-attachments/assets/87782aef-f5ca-416b-a004-ac39c825d129">



**Example Usage**
1. Run the script:

```bash
python cli_to_excel_gui.py
```
2. Fill out the GUI fields:

- **Host IP Address**: 192.168.1.1
- **Username**: admin
- **Password**: password123
- **Command**: show version
- **Excel File Save Location**: /path/to/save/output.xlsx
Click **Execute**.  
The script will connect to the device, execute the command, and save the output to the specified Excel file.

**Code Overview**
**Main Functions**
- **run_command()**: Establishes an SSH connection using Netmiko, executes the specified command, and returns the output.
- **filter_output()**: Filters out unwanted phrases from the command output before saving it.
- **remove_illegal_characters()**: Removes illegal characters from the output that can't be stored in Excel files.
- **update_excel()**: Updates the Excel file with the new command output, avoiding duplicates.
- **execute_command()**: Orchestrates the process, connecting the GUI input to the command execution and Excel file update.


**License**  
This project is licensed under the MIT License. See the LICENSE file for details.

**Acknowledgments**
- **Netmiko** for SSH connection handling.
- **Tkinter** for GUI creation.
- **pandas and openpyxl** for Excel file manipulation.








