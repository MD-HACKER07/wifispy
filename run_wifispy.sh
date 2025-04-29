#!/bin/bash

# WifiSpy Linux launch script
# By MD-HACKER

# ASCII art logo
echo -e "\033[1;32m"
cat << "EOF"
  __        ___ ___ _  ___ ____   __ 
  \ \      / (_) __(_)/ __|  _ \ / _|
   \ \ /\ / /| | _| _| (__| |_) | |_ 
    \ V  V / | ||_|| |\___| .__/|  _|
     \_/\_/  |_|  |_|     |_|   |_|   
                    Version 2.0
EOF
echo -e "\033[0m"

# Check if running as root
if [ "$EUID" -ne 0 ]; then
  echo -e "\033[1;31m[!] This script must be run as root\033[0m"
  echo "Try: sudo ./run_wifispy.sh"
  exit 1
fi

# Get the directory of the script
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

# Set up Python path
export PYTHONPATH="$SCRIPT_DIR:$PYTHONPATH"

# Check for necessary tools
command -v python3 >/dev/null 2>&1 || { 
  echo -e "\033[1;31m[!] Python 3 is required but not installed.\033[0m" 
  echo "Install with: apt install python3"
  exit 1
}

# Start WifiSpy
echo -e "\033[1;32m[+] Starting WifiSpy...\033[0m"
python3 bin/wifispy "$@" 