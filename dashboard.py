#!/usr/bin/env python3
import subprocess
import re
import sys
import time

# Cyberpunk ANSI colors
NEON_GREEN = "\033[38;5;118m"
NEON_MAGENTA = "\033[38;5;198m"
NEON_CYAN = "\033[38;5;51m"
RESET = "\033[0m"
BORDER_COLOR = "\033[38;5;239m"
GLOW = "\033[1m"

def print_header():
    # Clear screen sequence for full effect
    sys.stdout.write("\033[2J\033[H")
    sys.stdout.flush()
    print(f"{BORDER_COLOR}╔═══════════════════════════════════════════════════════════════╗{RESET}")
    print(f"{BORDER_COLOR}║ {GLOW}{NEON_MAGENTA}CYBER_MONITOR OVERRIDE ACTIVE - HOOKING SYS_EXECVE...{RESET}{BORDER_COLOR}       ║{RESET}")
    print(f"{BORDER_COLOR}╚═══════════════════════════════════════════════════════════════╝{RESET}")
    print(f"{NEON_CYAN}[SYSTEM_READY] WAITING FOR NEW PROCESS EXECUTIONS...{RESET}\n")

def run_monitor():
    print_header()
    # Tail the dmesg ring buffer directly and continuously wait for new entries
    process = subprocess.Popen(['dmesg', '-w'], stdout=subprocess.PIPE, text=True)
    
    try:
        for line in iter(process.stdout.readline, ''):
            if "[CYBER_MONITOR] EXECVE:" in line:
                # Extract the filename via regex
                match = re.search(r'\[CYBER_MONITOR\] EXECVE:\s*(.*)', line)
                if match:
                    exe = match.group(1).strip()
                    timestamp = time.strftime("%H:%M:%S")
                    print(f"{BORDER_COLOR}[{timestamp}] ▶{RESET} {NEON_CYAN}PROC DETECTED:{RESET} {GLOW}{NEON_GREEN}{exe}{RESET}")
    except KeyboardInterrupt:
        print(f"\n{BORDER_COLOR}╔═══════════════════════════════════════════════════════════════╗{RESET}")
        print(f"{BORDER_COLOR}║ {GLOW}{NEON_MAGENTA}SYSTEM DISCONNECTED. TERMINATING MONITOR.{RESET}{BORDER_COLOR}                    ║{RESET}")
        print(f"{BORDER_COLOR}╚═══════════════════════════════════════════════════════════════╝{RESET}")
        process.terminate()
        sys.exit(0)

if __name__ == '__main__':
    run_monitor()
