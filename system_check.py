import platform
import subprocess
import shutil


def show_system_info():
    print("\nSystem Information:")
    print(f"Operating System: {platform.system()} {platform.release()}")
    print(f"Computer Name: {platform.node()}")
    print(f"Processor: {platform.processor()}")
    print(f"Python Version: {platform.python_version()}")


def check_internet():
    host = "8.8.8.8"

    if platform.system().lower() == "windows":
        command = ["ping", "-n", "1", host]
        encoding = "cp850"
    else:
        command = ["ping", "-c", "1", host]
        encoding = "utf-8"

    try:
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            encoding=encoding,
            errors="ignore",
            timeout=5
        )

        if result.returncode == 0:
            print("\nInternet connection seems to be working.")
        else:
            print("\nNo internet connection detected.")
    except Exception as error:
        print("\nCould not test the internet connection.")
        print(f"Error: {error}")


def show_memory_info():
    try:
        memory = shutil.disk_usage("C:\\") if platform.system().lower() == "windows" else shutil.disk_usage("/")
        total_gb = memory.total / (1024 ** 3)
        used_gb = memory.used / (1024 ** 3)
        free_gb = memory.free / (1024 ** 3)

        print("\nDisk Information:")
        print(f"Total Space: {total_gb:.2f} GB")
        print(f"Used Space: {used_gb:.2f} GB")
        print(f"Free Space: {free_gb:.2f} GB")
    except Exception as error:
        print("\nCould not retrieve disk information.")
        print(f"Error: {error}")


def show_basic_ram_note():
    print("\nRAM Information:")
    print("Detailed RAM information is not included in this version.")
    print("This version focuses on system, disk, and connectivity checks.")


def main():
    while True:
        print("\nSystem Health Check Tool")
        print("1 - Show system information")
        print("2 - Test internet connection")
        print("3 - Show disk information")
        print("4 - Show RAM note")
        print("5 - Exit")

        choice = input("Enter a number: ").strip()

        if choice == "1":
            show_system_info()
        elif choice == "2":
            check_internet()
        elif choice == "3":
            show_memory_info()
        elif choice == "4":
            show_basic_ram_note()
        elif choice == "5":
            print("\nExiting program.")
            break
        else:
            print("\nInvalid input. Please try again.")


if __name__ == "__main__":
    main()