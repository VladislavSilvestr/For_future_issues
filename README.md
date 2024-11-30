
---

# Documentation for "Password Generator" Project

## Table of Contents
1. [Project Description](#project-description)
2. [Installation](#installation)
3. [Usage](#usage)
   - [Graphical User Interface](#graphical-user-interface)
4. [Functions](#functions)
5. [Dependencies](#dependencies)
6. [License](#license)

## Project Description
The "Password Generator" project allows users to generate secure passwords based on specified parameters such as password length, number of passwords, and complexity level. Generated passwords can include uppercase letters, digits, and special characters. Users can also save the generated passwords to a text file.

## Installation
To run the project, you will need Python and a few libraries. Follow the steps below:

1. Ensure you have Python installed (recommended version 3.6 or higher).
2. Install the required libraries by running the command:
   ```bash
   pip install pyperclip
   ```
3. Download or copy the project code to your local directory.

## Usage

### Graphical User Interface
1. Run the `main.py` file:
   ```bash
   python main.py
   ```
2. In the opened window, enter the parameters:
   - Password length
   - Number of passwords
   - Complexity level (Low, Medium, High)
   - Select additional options (use uppercase letters, numbers, special characters).
3. Click the "Generate password" button to generate passwords.
4. The generated passwords will be displayed in the interface. You can choose the option to save them to a text file.

## Functions
- `generate_password(length, use_uppercase, use_numbers, use_special_chars)`: Generates a password of the specified length considering the selected parameters.
- `generate_and_display_passwords()`: Processes user input, generates passwords, and displays them in the interface.
- `copy_to_clipboard(password)`: Copies the specified password to the clipboard.
- `save_passwords(passwords)`: Saves the generated passwords to a text file.

## Dependencies
- `tkinter`: Library for creating the graphical user interface.
- `pyperclip`: Library for clipboard functionality.


---
