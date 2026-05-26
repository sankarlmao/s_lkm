# Cyber Monitor (ftrace sys_execve Hook)

This project provides a Linux Kernel Module (LKM) and a user-space Python dashboard to monitor process execution (`sys_execve`) in real-time. It intercepts system calls using the modern `ftrace` framework, making it compatible with modern Linux kernels (6.x+) where traditional `sys_call_table` manipulation is no longer viable. 

The accompanying user-space dashboard displays the intercepted process executions in a highly stylized, cyberpunk-themed terminal UI.

## Features

- **Modern ftrace Hooking**: Safely hooks `__x64_sys_execve` by modifying the instruction pointer dynamically.
- **Kernel 5.7+ Compatibility**: Resolves `kallsyms_lookup_name` via a dummy `kprobe` (as it is no longer exported in recent kernels).
- **Recursion Protection**: Implements checks to prevent the hook from triggering infinite loops.
- **Cyberpunk Dashboard**: Real-time visualization using ANSI escape sequences.

## Prerequisites

- A Linux system with kernel version 5.11+ (tested on 6.x).
- Root privileges.
- Linux kernel headers installed.
- Python 3.x.
- `make` and `gcc`.

### Installing Dependencies (Debian/Ubuntu)

```bash
sudo apt update
sudo apt install build-essential linux-headers-$(uname -r) python3
```

## Compilation

Clone the repository and compile the kernel module:

```bash
make
```
This will generate `monitor.ko`.

## Usage

### 1. Load the Kernel Module

To avoid seeing old logs, you may optionally clear your kernel ring buffer first:

```bash
sudo dmesg -c
```

Insert the kernel module:

```bash
sudo insmod monitor.ko
```

You can verify it has been loaded:
```bash
lsmod | grep monitor
```

### 2. Run the Dashboard

The python script continuously monitors the `dmesg` buffer for intercepted events. Make sure it is executable, then run it:

```bash
chmod +x dashboard.py
python3 dashboard.py
```

Open another terminal and start executing some commands to see the executions populate your neon monitor console.

### 3. Safely Remove the Module

Once you are finished monitoring, stop the Python script using `Ctrl+C`. 
Then, remove the module gracefully from the kernel using `rmmod`:

```bash
sudo rmmod monitor
```

## Disclaimer

Manipulating core system calls like `sys_execve` and interacting with the `ftrace` sub-system should be done cautiously. Bugs in kernel modules can cause kernel panics and destabilize your operating system. This code incorporates recursion protection to maximize stability, but it is provided "as is". Use at your own risk.

## License

GPL
