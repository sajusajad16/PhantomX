from modules.port_scanner import port_scanner
from modules.recon import recon_module
from modules.web_scanner import web_scanner
from modules.utils import type_writer
from colorama import Fore, Style, init

init(autoreset=True)

banner = f"""
{Fore.GREEN}
██████╗ ██╗  ██╗ █████╗ ███╗   ██╗████████╗ ██████╗ ███╗   ███╗
██╔══██╗██║  ██║██╔══██╗████╗  ██║╚══██╔══╝██╔═══██╗████╗ ████║
██████╔╝███████║███████║██╔██╗ ██║   ██║   ██║   ██║██╔████╔██║
██╔═══╝ ██╔══██║██╔══██║██║╚██╗██║   ██║   ██║   ██║██║╚██╔╝██║
██║     ██║  ██║██║  ██║██║ ╚████║   ██║   ╚██████╔╝██║ ╚═╝ ██║
╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝   ╚═╝    ╚═════╝ ╚═╝     ╚═╝

        PhantomX Framework
{Fore.CYAN} Recon • Scan • Detect • Report
{Style.RESET_ALL}
"""

def main():
    type_writer(Fore.GREEN + "[+] Initializing PhantomX...\n")

    while True:
        print(banner)
        print(Fore.GREEN + "1. Port Scanner")
        print(Fore.YELLOW + "2. Recon")
        print(Fore.BLUE + "3. Web Scanner")
        print(Fore.RED + "4. Exit")

        choice = input(Fore.WHITE + "\nSelect option: ")

        if choice == "1":
            port_scanner()
        elif choice == "2":
            recon_module()
        elif choice == "3":
            web_scanner()
        elif choice == "4":
            print(Fore.RED + "\nExiting PhantomX...\n")
            break
        else:
            print(Fore.RED + "Invalid option")

if __name__ == "__main__":
    main()
