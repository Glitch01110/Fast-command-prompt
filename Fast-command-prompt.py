import subprocess
import sys
import os
from platform import system

# Version information
VERSION = "1.0"
AUTHOR = "Glitch01110"
GITHUB_URL = "https://github.com/Glitch01110"

def clear_screen():
    """Clear the terminal screen based on the operating system."""
    os.system('cls' if system() == 'Windows' else 'clear')


def GUI():
    """Display the main menu and ASCII art banner."""
    clear_screen()
    print(""" 
            
  ░██████  ░██ ░██   ░██               ░██          ░████     ░██     ░██     ░██     ░████   
 ░██   ░██ ░██       ░██               ░██         ░██ ░██  ░████   ░████   ░████    ░██ ░██  
░██        ░██ ░██░████████  ░███████  ░████████  ░██ ░████   ░██     ░██     ░██   ░██ ░████ 
░██  █████ ░██ ░██   ░██    ░██    ░██ ░██    ░██ ░██░██░██   ░██     ░██     ░██   ░██░██░██ 
░██     ██ ░██ ░██   ░██    ░██        ░██    ░██ ░████ ░██   ░██     ░██     ░██   ░████ ░██ 
 ░██  ░███ ░██ ░██   ░██    ░██    ░██ ░██    ░██  ░██ ░██    ░██     ░██     ░██    ░██ ░██  
  ░█████░█ ░██ ░██    ░████  ░███████  ░██    ░██   ░████   ░██████ ░██████ ░██████   ░████                                                                                                                                                                                                                                                                                            

                       ---------------------------
                       + Fast Command Prompt Tool +  
                       --------------------------- 

                       [+] By: {github}
                       [+] Version: {version}
            
             [1] update tool  [2] full upgrade system  [3] Restart the system  [c] clear screen
            
             [4] autoremove unnecessary packages  [5] autoclean package cache

             [99] Exit

             """.format(github=GITHUB_URL, version=VERSION))


def execute_command(command, description=""):
    """
    Execute a shell command with error handling.
    
    Args:
        command (str): The command to execute
        description (str): Optional description of what the command does
    """
    try:
        if description:
            print(f"\n[+] {description}...")
        result = subprocess.run(command, shell=True, check=True)
        if description:
            print(f"[✓] {description} completed successfully!\n")
        return result
    except subprocess.CalledProcessError as e:
        print(f"\n[✗] Error: Command failed with return code {e.returncode}\n")
        return None
    except KeyboardInterrupt:
        print("\n\n[!] Operation cancelled by user.\n")
        return None
    except Exception as e:
        print(f"\n[✗] Unexpected error: {str(e)}\n")
        return None


def confirm_action(message):
    """
    Ask user for confirmation before executing a potentially dangerous action.
    
    Args:
        message (str): The confirmation message
        
    Returns:
        bool: True if user confirms, False otherwise
    """
    response = input(f"\n[!] {message} (yes/no): ").strip().lower()
    return response in ['yes', 'y']


def Command():
    """Main command loop to handle user input and execute commands."""
    while True:
        try:
            choice = input("Fast-Command-Prompt~#: ").strip().lower()
            
            if choice == "1":
                execute_command("apt update", "Updating package list")
                
            elif choice == "2":
                if confirm_action("This will upgrade all system packages. Continue?"):
                    execute_command("apt full-upgrade -y", "Performing full system upgrade")
                else:
                    print("[!] Upgrade cancelled.\n")
                    
            elif choice == "3":
                if confirm_action("This will restart your system. Continue?"):
                    print("\n[!] System will restart in 5 seconds...")
                    print("[!] Press Ctrl+C to cancel\n")
                    try:
                        import time
                        time.sleep(5)
                    except KeyboardInterrupt:
                        print("\n[!] Restart cancelled.\n")
                        continue
                    execute_command("reboot", "Restarting system")
                else:
                    print("[!] Restart cancelled.\n")
                    
            elif choice in ["clear", "c"]:
                GUI()
                
            elif choice == "4":
                execute_command("apt autoremove -y", "Removing unnecessary packages")
                
            elif choice == "5":
                execute_command("apt autoclean", "Cleaning package cache")
                
            elif choice == "99":
                print("\n[+] Goodbye!\n")
                sys.exit(0)
                
            elif choice == "":
                continue
                
            else:
                print(f"\n[✗] Invalid option: '{choice}'. Please try again.\n")
                
        except KeyboardInterrupt:
            print("\n\n[!] Use '99' to exit, or Ctrl+C again to force quit.\n")
            try:
                response = input("Exit? (yes/no): ").strip().lower()
                if response in ['yes', 'y']:
                    print("\n[+] Goodbye!\n")
                    sys.exit(0)
                else:
                    GUI()
            except KeyboardInterrupt:
                print("\n[+] Force quit. Goodbye!\n")
                sys.exit(1)
        except EOFError:
            print("\n\n[+] Goodbye!\n")
            sys.exit(0)


def main():
    """Main entry point of the application."""
    GUI()
    Command()


if __name__ == "__main__":
    main()
