# 🚀 Fast Command Prompt

<div align="center">

![Python](https://img.shields.io/badge/Python-3.6+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Version](https://img.shields.io/badge/Version-1.0-orange.svg)
![Platform](https://img.shields.io/badge/Platform-Linux%20%7C%20Windows-lightgrey.svg)

**A fast and intuitive command-line tool for managing Linux packages with error handling, safety confirmations, and a beautiful interactive interface**

[Features](#-features) • [Installation](#-installation) • [Usage](#-usage) • [Commands](#-available-commands) • [Safety Features](#-safety-features) • [Contributing](#-contributing)

</div>

---

## 📋 Table of Contents

- [Features](#-features)
- [Requirements](#-requirements)
- [Installation](#-installation)
- [Usage](#-usage)
- [Available Commands](#-available-commands)
- [Safety Features](#-safety-features)
- [Error Handling](#-error-handling)
- [Screenshots](#-screenshot-preview)
- [Important Notes](#-important-notes)
- [Contributing](#-contributing)
- [Author](#-author)
- [License](#-license)

---

## ✨ Features

- 🎨 **Beautiful Interface**: Professional ASCII Art design with an elegant menu
- ⚡ **Fast & Simple**: Quick access to the most commonly used Linux package management commands
- 🔧 **Essential Commands**: Support for update, upgrade, cleanup, and system management
- 🧹 **Auto Cleanup**: Automatically remove unnecessary packages and clean cache
- 💻 **User-Friendly**: Interactive menu-driven interface, easy to use for beginners
- 🚀 **Lightweight**: Simple Python script with no external dependencies
- 🛡️ **Error Handling**: Comprehensive error handling with clear error messages
- ✅ **Safety Confirmations**: Confirmation prompts for dangerous operations (upgrade, reboot)
- 📱 **Cross-Platform**: Works on both Linux and Windows (screen clearing)
- 🔄 **Smart Clear**: Efficient screen clearing without restarting the application
- ⌨️ **Keyboard Interrupt Handling**: Graceful handling of Ctrl+C with exit confirmation
- 📊 **Status Messages**: Clear visual indicators (✓, ✗, !, +) for operations

---

## 📦 Requirements

- **Python 3.6+**
- **Linux System** (Debian/Ubuntu based distributions) for package management commands
- **Windows** support for screen clearing functionality
- **sudo/root privileges** (required for system commands on Linux)

---

## 🔧 Installation

### Quick Install

1. **Clone the repository:**
```bash
git clone https://github.com/Glitch01110/Fast-command-prompt.git
cd Fast-command-prompt
```

2. **Run the tool:**
```bash
python3 Fast-command-prompt.py
```

Or on Windows:
```bash
python Fast-command-prompt.py
```

**Note:** You may need `sudo` privileges to execute certain system commands on Linux.

---

## 🎯 Usage

### Getting Started

1. **Launch the application:**
```bash
python3 Fast-command-prompt.py
```

2. The interactive menu will be displayed
3. Select the number or command you want to execute
4. For dangerous operations, confirm when prompted
5. Wait for the operation to complete

### Example Workflow

```bash
# Start the tool
python3 Fast-command-prompt.py

# Choose option 1 to update package lists
Fast-Command-Prompt~#: 1
[+] Updating package list...
[✓] Updating package list completed successfully!

# Choose option 2 to upgrade system (will ask for confirmation)
Fast-Command-Prompt~#: 2
[!] This will upgrade all system packages. Continue? (yes/no): yes
[+] Performing full system upgrade...
[✓] Performing full system upgrade completed successfully!

# Clear screen (instant, no restart)
Fast-Command-Prompt~#: c

# Exit the tool
Fast-Command-Prompt~#: 99
[+] Goodbye!
```

---

## 📝 Available Commands

| Option | Command | Description | Confirmation |
|:---:|:---:|---|:---:|
| `1` | `apt update` | Update the package list from repositories | ❌ No |
| `2` | `apt full-upgrade -y` | Perform a full system upgrade (non-interactive) | ✅ Yes |
| `3` | `reboot` | Restart the system (5 second delay) | ✅ Yes |
| `4` | `apt autoremove -y` | Remove unnecessary packages automatically | ❌ No |
| `5` | `apt autoclean` | Clean the package cache | ❌ No |
| `c` / `clear` | `clear` | Clear the screen and refresh menu | ❌ No |
| `99` | `exit` | Exit the application | ❌ No |

### Command Details

- **Option 1 (Update)**: Refreshes the package list from all configured repositories
- **Option 2 (Upgrade)**: Upgrades all installed packages to their latest versions. **Requires confirmation**
- **Option 3 (Reboot)**: Restarts the system. **Requires confirmation** and has a 5-second cancellation window
- **Option 4 (Autoremove)**: Removes packages that were automatically installed as dependencies but are no longer needed
- **Option 5 (Autoclean)**: Cleans the local repository cache of retrieved package files
- **Clear (c)**: Instantly clears the screen and redraws the menu without restarting the program
- **Exit (99)**: Gracefully exits the application

---

## 🛡️ Safety Features

### Confirmation Prompts

The tool includes safety confirmations for potentially dangerous operations:

- **System Upgrade**: Confirms before upgrading all packages
- **System Reboot**: Confirms before restarting, then provides a 5-second cancellation window

### Example Safety Flow

```bash
Fast-Command-Prompt~#: 3

[!] This will restart your system. Continue? (yes/no): yes

[!] System will restart in 5 seconds...
[!] Press Ctrl+C to cancel

# User can press Ctrl+C within 5 seconds to cancel
```

---

## ⚠️ Error Handling

The tool includes comprehensive error handling:

### Error Types Handled

- ✅ **Command Execution Errors**: Displays clear error messages when commands fail
- ✅ **Keyboard Interrupts**: Graceful handling of Ctrl+C with exit confirmation
- ✅ **Invalid Input**: Informative messages for unrecognized commands
- ✅ **Unexpected Errors**: Catches and reports unexpected exceptions

### Error Message Examples

```bash
# Command failure
[✗] Error: Command failed with return code 1

# Invalid option
[✗] Invalid option: 'xyz'. Please try again.

# Operation cancelled
[!] Operation cancelled by user.

# Exit confirmation
[!] Use '99' to exit, or Ctrl+C again to force quit.
Exit? (yes/no):
```

---

## 🎨 Screenshot Preview

```
░░██████  ░██ ░██   ░██               ░██          ░████     ░██     ░██     ░██     ░████   
░██   ░██ ░██       ░██               ░██         ░██ ░██  ░████   ░████   ░████    ░██ ░██  
░██        ░██ ░██░████████  ░███████  ░████████  ░██ ░████   ░██     ░██     ░██   ░██ ░████ 
░██  █████ ░██ ░██   ░██    ░██    ░██ ░██    ░██ ░██░██░██   ░██     ░██     ░██   ░██░██░██ 
░██     ██ ░██ ░██   ░██    ░██        ░██    ░██ ░████ ░██   ░██     ░██     ░██   ░████ ░██ 
 ░██  ░███ ░██ ░██   ░██    ░██    ░██ ░██    ░██  ░██ ░██    ░██     ░██     ░██    ░██ ░██  
  ░█████░█ ░██ ░██    ░████  ░███████  ░██    ░██   ░████   ░██████ ░██████ ░██████   ░████

                       ---------------------------
                       + Fast Command Prompt Tool +  
                       --------------------------- 

                       [+] By: https://github.com/Glitch01110
                       [+] Version: 1.0

[1] update tool  [2] full upgrade system  [3] Restart the system  [c] clear screen

[4] autoremove unnecessary packages  [5] autoclean package cache

[99] Exit

Fast-Command-Prompt~#: 
```

---

## ⚠️ Important Notes

### Warnings

- ⚠️ **Use with caution**: Some commands require elevated privileges and may affect your system
- 🔒 **Backup your data**: Always backup important data before performing system upgrades
- 💻 **Linux commands**: Package management commands (`apt`) only work on Debian/Ubuntu-based Linux distributions
- 🛡️ **Root access**: Some commands require `sudo` or root access to execute
- ⏱️ **Reboot delay**: System restart has a 5-second cancellation window for safety

### Best Practices

- ✅ Always update the package list (`option 1`) before upgrading (`option 2`)
- ✅ Use `autoremove` (`option 4`) regularly to keep your system clean
- ✅ Use `autoclean` (`option 5`) to free up disk space periodically
- ✅ Only restart the system (`option 3`) when necessary and after saving your work
- ✅ Read confirmation prompts carefully before confirming dangerous operations
- ✅ Use Ctrl+C if you need to cancel an operation

### Status Indicators

- `[+]` - Information or operation start
- `[✓]` - Success/completion
- `[✗]` - Error/failure
- `[!]` - Warning or important notice

---

## 🏗️ Code Structure

The code is well-organized with the following functions:

- `clear_screen()`: Cross-platform screen clearing
- `GUI()`: Displays the main menu and ASCII art
- `execute_command()`: Executes commands with comprehensive error handling
- `confirm_action()`: Handles user confirmation for dangerous operations
- `Command()`: Main command loop with input validation
- `main()`: Application entry point

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

### How to Contribute

1. **Fork the repository**
2. **Create your feature branch** (`git checkout -b feature/AmazingFeature`)
3. **Commit your changes** (`git commit -m 'Add some AmazingFeature'`)
4. **Push to the branch** (`git push origin feature/AmazingFeature`)
5. **Open a Pull Request**

### Contribution Guidelines

- Follow the existing code style (PEP 8)
- Add docstrings to new functions
- Include error handling in new features
- Add confirmation prompts for dangerous operations
- Test your changes thoroughly
- Update documentation if needed

---

## 🐛 Issues & Bug Reports

If you encounter any bugs or have suggestions, please open an issue on [GitHub Issues](https://github.com/Glitch01110/Fast-command-prompt/issues).

When reporting bugs, please include:
- Operating system and version
- Python version
- Steps to reproduce the issue
- Expected vs actual behavior
- Any error messages

---

## 💡 Future Enhancements

- [ ] Add more package management commands
- [ ] Support for other package managers (yum, pacman, dnf)
- [ ] Configuration file support
- [ ] Colored output for better readability
- [ ] Logging functionality to file
- [ ] GUI version with Tkinter or PyQt
- [ ] Command history
- [ ] Batch command execution
- [ ] Progress bars for long-running operations

---

## 👤 Author

<div align="center">

**Glitch01110**

🔗 [GitHub Profile](https://github.com/Glitch01110)

</div>

---

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

<div align="center">

**⭐ If you like this project, don't forget to give it a star! ⭐**

Made with ❤️ by Glitch01110

---

[⬆ Back to Top](#-fast-command-prompt)

</div>
