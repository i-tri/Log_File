# Remote CLI Command Executor with Excel Logging

This Python project connects to remote devices via SSH using Netmiko, executes CLI commands, and logs the results into an Excel file. 
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
