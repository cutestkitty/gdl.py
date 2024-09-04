import subprocess
import sys

gdl_path = './gallery-dl.exe'  # gallery-dl.exe path

def print_red(text):
    RED = '\033[91m'
    RESET = '\033[0m'
    print(f"{RED}{text}{RESET}")

def main():
    while True:
        user_input = input("Enter URLs for gallery-dl (type 'quit', 'exit', or '3' to exit)\n> ")
        if user_input.lower() in ['quit', 'exit', '3']:
            break

        user_input = user_input.replace('"', '')
        urls = user_input.split()
        command = [gdl_path] + urls

        try:
            result = subprocess.run(command, stdout=sys.stdout, stderr=sys.stderr)
        except FileNotFoundError:
            print_red(f"\ngallery-dl was not found. Change gdl_path to your gallery-dl.exe\ngdl_path: {gdl_path}\n")

if __name__ == "__main__":
    main()