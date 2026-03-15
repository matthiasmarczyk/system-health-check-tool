import platform


def show_system_info():
    print("System Health Check Tool")
    print()
    print("System Information:")
    print(f"Operating System: {platform.system()} {platform.release()}")
    print(f"Computer Name: {platform.node()}")
    print(f"Processor: {platform.processor()}")
    print(f"Python Version: {platform.python_version()}")


if __name__ == "__main__":
    show_system_info()