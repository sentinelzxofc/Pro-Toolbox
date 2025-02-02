#!/data/data/com.termux/files/usr/bin/python3

import os
import sys
import subprocess

class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    RESET = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def show_banner():
    banner = f"""
{Colors.CYAN}{Colors.BOLD}
╔════════════════════════════════════════════════════════════╗
║                                                            ║
║  {Colors.YELLOW}▓█████▄  ██▀███   ▒█████   █     █░ ▄▄▄       ██▀███  {Colors.CYAN}║
║  {Colors.YELLOW}▒██▀ ██▌▓██ ▒ ██▒▒██▒  ██▒▓█░ █ ░█░▒████▄    ▓██ ▒ ██▒{Colors.CYAN}║
║  {Colors.YELLOW}░██   █▌▓██ ░▄█ ▒▒██░  ██▒▒█░ █ ░█ ▒██  ▀█▄  ▓██ ░▄█ ▒{Colors.CYAN}║
║  {Colors.YELLOW}░▓█▄   ▌▒██▀▀█▄  ▒██   ██░░█░ █ ░█ ░██▄▄▄▄██ ▒██▀▀█▄  {Colors.CYAN}║
║  {Colors.YELLOW}░▒████▓ ░██▓ ▒██▒░ ████▓▒░░░██▒██▓  ▓█   ▓██▒░██▓ ▒██▒{Colors.CYAN}║
║  {Colors.YELLOW} ▒▒▓  ▒ ░ ▒▓ ░▒▓░░ ▒░▒░▒░ ░ ▓░▒ ▒   ▒▒   ▓▒█░░ ▒▓ ░▒▓░{Colors.CYAN}║
║  {Colors.YELLOW} ░ ▒  ▒   ░▒ ░ ▒░  ░ ▒ ▒░   ▒ ░ ░    ▒   ▒▒ ░  ░▒ ░ ▒░{Colors.CYAN}║
║  {Colors.YELLOW} ░ ░  ░   ░░   ░ ░ ░ ░ ▒    ░   ░    ░   ▒     ░░   ░ {Colors.CYAN}║
║  {Colors.YELLOW}   ░       ░         ░ ░      ░        ░  ░   ░     {Colors.CYAN}║
║  {Colors.YELLOW} ░                                                  {Colors.CYAN}║
║                                                            ║
║  {Colors.WHITE}Versão: 3.0{Colors.CYAN}                                             ║
║  {Colors.WHITE}Criado por: sentinelzxofc{Colors.CYAN}                               ║
║                                                            ║
╚════════════════════════════════════════════════════════════╝
{Colors.RESET}
"""
    print(banner)

def check_internet():
    print(f"{Colors.BLUE}[*] Verificando conexão com a internet...{Colors.RESET}")
    try:
        subprocess.check_call(["ping", "-c", "1", "8.8.8.8"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print(f"{Colors.GREEN}[+] Conexão com a internet está ativa.{Colors.RESET}")
    except subprocess.CalledProcessError:
        print(f"{Colors.RED}[-] Sem conexão com a internet.{Colors.RESET}")
        sys.exit(1)

def update_packages():
    print(f"{Colors.BLUE}[*] Atualizando pacotes do Termux...{Colors.RESET}")
    try:
        os.system("pkg update -y && pkg upgrade -y")
        print(f"{Colors.GREEN}[+] Pacotes atualizados com sucesso.{Colors.RESET}")
    except Exception as e:
        print(f"{Colors.RED}[-] Erro ao atualizar pacotes: {e}{Colors.RESET}")

def install_essential_packages():
    essential_packages = ["python", "git", "wget", "curl", "nano", "vim", "tar", "zip", "unzip", "fish", "tmux", "htop"]
    print(f"{Colors.BLUE}[*] Instalando pacotes essenciais...{Colors.RESET}")
    for package in essential_packages:
        try:
            os.system(f"pkg install -y {package}")
            print(f"{Colors.GREEN}[+] {package} instalado com sucesso.{Colors.RESET}")
        except Exception as e:
            print(f"{Colors.RED}[-] Erro ao instalar {package}: {e}{Colors.RESET}")

def install_metasploit():
    print(f"{Colors.BLUE}[*] Instalando Metasploit...{Colors.RESET}")
    try:
        os.system("pkg install unstable-repo -y && pkg install metasploit -y")
        print(f"{Colors.GREEN}[+] Metasploit instalado com sucesso.{Colors.RESET}")
    except Exception as e:
        print(f"{Colors.RED}[-] Erro ao instalar Metasploit: {e}{Colors.RESET}")

def install_sqlmap():
    print(f"{Colors.BLUE}[*] Instalando SQLMap...{Colors.RESET}")
    try:
        os.system("pkg install sqlmap -y")
        print(f"{Colors.GREEN}[+] SQLMap instalado com sucesso.{Colors.RESET}")
    except Exception as e:
        print(f"{Colors.RED}[-] Erro ao instalar SQLMap: {e}{Colors.RESET}")

def install_nmap():
    print(f"{Colors.BLUE}[*] Instalando Nmap...{Colors.RESET}")
    try:
        os.system("pkg install nmap -y")
        print(f"{Colors.GREEN}[+] Nmap instalado com sucesso.{Colors.RESET}")
    except Exception as e:
        print(f"{Colors.RED}[-] Erro ao instalar Nmap: {e}{Colors.RESET}")

def install_ngrok():
    print(f"{Colors.BLUE}[*] Instalando Ngrok...{Colors.RESET}")
    try:
        os.system("pkg install wget -y && wget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-arm.zip && unzip ngrok-stable-linux-arm.zip && mv ngrok /data/data/com.termux/files/usr/bin/ && rm ngrok-stable-linux-arm.zip")
        print(f"{Colors.GREEN}[+] Ngrok instalado com sucesso.{Colors.RESET}")
    except Exception as e:
        print(f"{Colors.RED}[-] Erro ao instalar Ngrok: {e}{Colors.RESET}")

def install_ssh_server():
    print(f"{Colors.BLUE}[*] Instalando e configurando servidor SSH...{Colors.RESET}")
    try:
        os.system("pkg install openssh -y && sshd")
        print(f"{Colors.GREEN}[+] Servidor SSH instalado e configurado com sucesso.{Colors.RESET}")
    except Exception as e:
        print(f"{Colors.RED}[-] Erro ao configurar SSH: {e}{Colors.RESET}")

def install_wordlist_generator():
    print(f"{Colors.BLUE}[*] Instalando gerador de wordlists (crunch)...{Colors.RESET}")
    try:
        os.system("pkg install crunch -y")
        print(f"{Colors.GREEN}[+] Crunch instalado com sucesso.{Colors.RESET}")
    except Exception as e:
        print(f"{Colors.RED}[-] Erro ao instalar Crunch: {e}{Colors.RESET}")

def install_hydra():
    print(f"{Colors.BLUE}[*] Instalando Hydra...{Colors.RESET}")
    try:
        os.system("pkg install hydra -y")
        print(f"{Colors.GREEN}[+] Hydra instalado com sucesso.{Colors.RESET}")
    except Exception as e:
        print(f"{Colors.RED}[-] Erro ao instalar Hydra: {e}{Colors.RESET}")

def install_wifi_tools():
    print(f"{Colors.BLUE}[*] Instalando ferramentas de rede Wi-Fi...{Colors.RESET}")
    try:
        os.system("pkg install aircrack-ng -y")
        print(f"{Colors.GREEN}[+] Ferramentas de rede Wi-Fi instaladas com sucesso.{Colors.RESET}")
    except Exception as e:
        print(f"{Colors.RED}[-] Erro ao instalar ferramentas de rede Wi-Fi: {e}{Colors.RESET}")

def install_ffmpeg():
    print(f"{Colors.BLUE}[*] Instalando FFmpeg...{Colors.RESET}")
    try:
        os.system("pkg install ffmpeg -y")
        print(f"{Colors.GREEN}[+] FFmpeg instalado com sucesso.{Colors.RESET}")
    except Exception as e:
        print(f"{Colors.RED}[-] Erro ao instalar FFmpeg: {e}{Colors.RESET}")

def install_youtube_dl():
    print(f"{Colors.BLUE}[*] Instalando YouTube-DL...{Colors.RESET}")
    try:
        os.system("pkg install python -y && pip install youtube-dl")
        print(f"{Colors.GREEN}[+] YouTube-DL instalado com sucesso.{Colors.RESET}")
    except Exception as e:
        print(f"{Colors.RED}[-] Erro ao instalar YouTube-DL: {e}{Colors.RESET}")

def install_termux_api():
    print(f"{Colors.BLUE}[*] Instalando Termux API...{Colors.RESET}")
    try:
        os.system("pkg install termux-api -y")
        print(f"{Colors.GREEN}[+] Termux API instalado com sucesso.{Colors.RESET}")
    except Exception as e:
        print(f"{Colors.RED}[-] Erro ao instalar Termux API: {e}{Colors.RESET}")

def install_rclone():
    print(f"{Colors.BLUE}[*] Instalando Rclone...{Colors.RESET}")
    try:
        os.system("pkg install rclone -y")
        print(f"{Colors.GREEN}[+] Rclone instalado com sucesso.{Colors.RESET}")
    except Exception as e:
        print(f"{Colors.RED}[-] Erro ao instalar Rclone: {e}{Colors.RESET}")

def install_gh_cli():
    print(f"{Colors.BLUE}[*] Instalando GitHub CLI...{Colors.RESET}")
    try:
        os.system("pkg install gh -y")
        print(f"{Colors.GREEN}[+] GitHub CLI instalado com sucesso.{Colors.RESET}")
    except Exception as e:
        print(f"{Colors.RED}[-] Erro ao instalar GitHub CLI: {e}{Colors.RESET}")

def install_neofetch():
    print(f"{Colors.BLUE}[*] Instalando Neofetch...{Colors.RESET}")
    try:
        os.system("pkg install neofetch -y")
        print(f"{Colors.GREEN}[+] Neofetch instalado com sucesso.{Colors.RESET}")
    except Exception as e:
        print(f"{Colors.RED}[-] Erro ao instalar Neofetch: {e}{Colors.RESET}")

def install_php():
    print(f"{Colors.BLUE}[*] Instalando PHP...{Colors.RESET}")
    try:
        os.system("pkg install php -y")
        print(f"{Colors.GREEN}[+] PHP instalado com sucesso.{Colors.RESET}")
    except Exception as e:
        print(f"{Colors.RED}[-] Erro ao instalar PHP: {e}{Colors.RESET}")

def install_nodejs():
    print(f"{Colors.BLUE}[*] Instalando Node.js...{Colors.RESET}")
    try:
        os.system("pkg install nodejs -y")
        print(f"{Colors.GREEN}[+] Node.js instalado com sucesso.{Colors.RESET}")
    except Exception as e:
        print(f"{Colors.RED}[-] Erro ao instalar Node.js: {e}{Colors.RESET}")

def install_ruby():
    print(f"{Colors.BLUE}[*] Instalando Ruby...{Colors.RESET}")
    try:
        os.system("pkg install ruby -y")
        print(f"{Colors.GREEN}[+] Ruby instalado com sucesso.{Colors.RESET}")
    except Exception as e:
        print(f"{Colors.RED}[-] Erro ao instalar Ruby: {e}{Colors.RESET}")

def install_golang():
    print(f"{Colors.BLUE}[*] Instalando Go (Golang)...{Colors.RESET}")
    try:
        os.system("pkg install golang -y")
        print(f"{Colors.GREEN}[+] Go instalado com sucesso.{Colors.RESET}")
    except Exception as e:
        print(f"{Colors.RED}[-] Erro ao instalar Go: {e}{Colors.RESET}")

def install_wget2():
    print(f"{Colors.BLUE}[*] Instalando Wget2...{Colors.RESET}")
    try:
        os.system("pkg install wget2 -y")
        print(f"{Colors.GREEN}[+] Wget2 instalado com sucesso.{Colors.RESET}")
    except Exception as e:
        print(f"{Colors.RED}[-] Erro ao instalar Wget2: {e}{Colors.RESET}")

def clear_screen():
    os.system("clear")

def main_menu():
    clear_screen()
    show_banner()
    print(f"{Colors.MAGENTA}[1] Verificar conexão com a internet{Colors.RESET}")
    print(f"{Colors.MAGENTA}[2] Atualizar pacotes do Termux{Colors.RESET}")
    print(f"{Colors.MAGENTA}[3] Instalar pacotes essenciais{Colors.RESET}")
    print(f"{Colors.MAGENTA}[4] Instalar Metasploit{Colors.RESET}")
    print(f"{Colors.MAGENTA}[5] Instalar SQLMap{Colors.RESET}")
    print(f"{Colors.MAGENTA}[6] Instalar Nmap{Colors.RESET}")
    print(f"{Colors.MAGENTA}[7] Instalar Ngrok{Colors.RESET}")
    print(f"{Colors.MAGENTA}[8] Instalar servidor SSH{Colors.RESET}")
    print(f"{Colors.MAGENTA}[9] Instalar Crunch (Wordlist Generator){Colors.RESET}")
    print(f"{Colors.MAGENTA}[10] Instalar Hydra{Colors.RESET}")
    print(f"{Colors.MAGENTA}[11] Instalar ferramentas de rede Wi-Fi{Colors.RESET}")
    print(f"{Colors.MAGENTA}[12] Instalar FFmpeg{Colors.RESET}")
    print(f"{Colors.MAGENTA}[13] Instalar YouTube-DL{Colors.RESET}")
    print(f"{Colors.MAGENTA}[14] Instalar Termux API{Colors.RESET}")
    print(f"{Colors.MAGENTA}[15] Instalar Rclone{Colors.RESET}")
    print(f"{Colors.MAGENTA}[16] Instalar GitHub CLI{Colors.RESET}")
    print(f"{Colors.MAGENTA}[17] Instalar Neofetch{Colors.RESET}")
    print(f"{Colors.MAGENTA}[18] Instalar PHP{Colors.RESET}")
    print(f"{Colors.MAGENTA}[19] Instalar Node.js{Colors.RESET}")
    print(f"{Colors.MAGENTA}[20] Instalar Ruby{Colors.RESET}")
    print(f"{Colors.MAGENTA}[21] Instalar Go (Golang){Colors.RESET}")
    print(f"{Colors.MAGENTA}[22] Instalar Wget2{Colors.RESET}")
    print(f"{Colors.MAGENTA}[23] Sair{Colors.RESET}")
    choice = input(f"{Colors.YELLOW}[?] Escolha uma opção: {Colors.RESET}")
    return choice

def main():
    while True:
        choice = main_menu()
        if choice == "1":
            check_internet()
        elif choice == "2":
            update_packages()
        elif choice == "3":
            install_essential_packages()
        elif choice == "4":
            install_metasploit()
        elif choice == "5":
            install_sqlmap()
        elif choice == "6":
            install_nmap()
        elif choice == "7":
            install_ngrok()
        elif choice == "8":
            install_ssh_server()
        elif choice == "9":
            install_wordlist_generator()
        elif choice == "10":
            install_hydra()
        elif choice == "11":
            install_wifi_tools()
        elif choice == "12":
            install_ffmpeg()
        elif choice == "13":
            install_youtube_dl()
        elif choice == "14":
            install_termux_api()
        elif choice == "15":
            install_rclone()
        elif choice == "16":
            install_gh_cli()
        elif choice == "17":
            install_neofetch()
        elif choice == "18":
            install_php()
        elif choice == "19":
            install_nodejs()
        elif choice == "20":
            install_ruby()
        elif choice == "21":
            install_golang()
        elif choice == "22":
            install_wget2()
        elif choice == "23":
            print(f"{Colors.RED}[*] Saindo...{Colors.RESET}")
            break
        else:
            print(f"{Colors.RED}[-] Opção inválida. Tente novamente.{Colors.RESET}")
        input(f"{Colors.YELLOW}[?] Pressione Enter para continuar...{Colors.RESET}")

if __name__ == "__main__":
    main()
