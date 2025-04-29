
# WifiSpy - Advanced Wi-Fi Security Assessment Toolkit

## About

WifiSpy is a powerful rogue Access Point framework designed for professional red team engagements and thorough Wi-Fi security assessments. Security professionals can use WifiSpy to efficiently perform targeted Wi-Fi association attacks to achieve man-in-the-middle positions against wireless clients. The toolkit facilitates custom phishing campaigns against connected clients for credential capture or payload deployment.

> **Important:** This tool is intended for authorized security testing only. Misuse of this tool against networks without proper permission is illegal and unethical.

## Key Features

- **High Performance**: Optimized to run efficiently even on modest hardware like Raspberry Pi
- **Multiple Attack Vectors**: Supports Evil Twin, KARMA, and Known Beacons attacks
- **Modular Design**: Easily extendable with custom Python modules
- **Intuitive Terminal UI**: Clean interface guides you through attack setup
- **Advanced Techniques**: Implements cutting-edge methods like Known Beacons and Lure10
- **Comprehensive Reporting**: Detailed JSON reports and CSV credential exports
- **Cross-Platform**: Primarily designed for Linux, with guidance for other platforms

## How It Works

<p align="center">
  <img src="https://wifiphisher.github.io/wifiphisher/diagram.jpg" width="70%" />
  <br><i>MITM Attack Diagram</i>
</p>

WifiSpy operates in two main phases:

1. **Initial Position**:
   - Creates fake networks that mimic legitimate ones (Evil Twin)
   - Exploits automatic connection behaviors (KARMA)
   - Broadcasts common network names to trigger connections (Known Beacons)
   - Sends deauthentication packets to disconnect users from legitimate networks

2. **Exploitation**:
   - Harvests credentials through convincing phishing pages
   - Analyzes network traffic
   - Delivers custom payloads
   - Assesses vulnerabilities of connected clients

## Requirements

- A Linux system (Kali Linux recommended)
- Wireless network adapter supporting AP & Monitor mode with injection capabilities
- Python 3.9 or higher
- Root/sudo privileges

### Windows Compatibility

While WifiSpy is primarily designed for Linux systems, Windows users can:
1. Install WifiSpy in WSL (Windows Subsystem for Linux)
2. Use a Linux virtual machine with USB passthrough for wireless adapters
3. Boot from a Kali Linux live USB for full hardware access

> **Note**: Direct Windows execution is not fully supported due to dependencies on Linux-specific wireless modules and the curses library.

## Installation

### From Source

```bash
# Clone the repository
git clone https://github.com/MD-HACKER07/wifispy.git

# Navigate to the directory
cd wifispy

# Install dependencies
sudo python setup.py install

# Make scripts executable
chmod +x bin/wifispy
chmod +x run_wifispy.sh
```

### From Release Package

1. Download the latest release from the [Releases page](https://github.com/MD-HACKER07/wifispy/releases)
2. Extract the archive: `tar -xzf wifispy-2.0.tar.gz`
3. Make scripts executable: 
   ```bash
   chmod +x wifispy/bin/wifispy
   chmod +x wifispy/run_wifispy.sh
   ```

## Quick Start

### Launch WifiSpy

```bash
# Start with the launcher script (recommended)
sudo ./run_wifispy.sh

# Alternatively, run directly
sudo python bin/wifispy
```

### Basic Usage

When you run WifiSpy without options, it will:
1. Find available wireless interfaces automatically
2. List all nearby wireless networks
3. Let you select a target network
4. Present phishing scenario options
5. Execute the attack with both Evil Twin and KARMA techniques

## Usage Examples

### Basic Evil Twin Attack

Target a specific Wi-Fi network with a firmware upgrade phishing page:

```bash
sudo ./run_wifispy.sh -e "Target-WiFi" -p firmware-upgrade
```

### KARMA Attack with OAuth Phishing

Create an open hotspot that leverages KARMA attacks with an OAuth login page:

```bash
sudo ./run_wifispy.sh --essid "Free Airport WiFi" -p oauth-login -kB
```

### Advanced Configuration

Specify interfaces and enable advanced options:

```bash
sudo ./run_wifispy.sh -aI wlan0 -eI wlan1 -p firmware-upgrade --channel-monitor --logging
```

### Command Line Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Show help message |
| `-e ESSID, --essid ESSID` | ESSID of the rogue Access Point |
| `-p SCENARIO, --phishingscenario SCENARIO` | Phishing scenario to run |
| `-aI INTERFACE, --apinterface INTERFACE` | Interface for the Access Point |
| `-eI INTERFACE, --extensionsinterface INTERFACE` | Interface for monitoring/attacks |
| `-pK KEY, --presharedkey KEY` | Add WPA/WPA2 protection to the rogue AP |
| `-kB, --known-beacons` | Enable known beacons attack |
| `--logging` | Enable detailed logging |
| `-rP PATH, --report-path PATH` | Path for saving reports |

For a complete list of options, run `sudo ./run_wifispy.sh --help`

## Report Generation

WifiSpy automatically generates detailed reports including:
- Target network information
- Connected victim details
- Captured credentials

Reports are saved in JSON format and can be found in `~/wifispy-reports/` by default.

## Screenshots

<p align="center">
  <img src="https://wifiphisher.github.io/wifiphisher/ss5.png" />
  <br><i>Targeting an access point</i>
</p>

<p align="center">
  <img src="https://wifiphisher.github.io/wifiphisher/ss2.png" />
  <br><i>A successful attack</i>
</p>

<p align="center">
  <img src="https://wifiphisher.github.io/wifiphisher/ss7.png" />
  <br><i>Fake router configuration page</i>
</p>

## Contact

Feel free to reach out for any questions, suggestions, or collaboration:

- GitHub: [@MD-HACKER07](https://github.com/MD-HACKER07)
- Instagram: [@iammd_18_](https://www.instagram.com/iammd_18_)
- LinkedIn: [MD Abu Shalem Alam](https://in.linkedin.com/in/md-abu-shalem-alam-726a93292)
- Website: [abushalem.site](https://abushalem.site/)

## License

WifiSpy is licensed under the GPLv3 license. See [LICENSE](LICENSE) for more information.

## Disclaimer

Usage of WifiSpy for attacking infrastructures without prior mutual consent can be considered an illegal activity. It is the end user's responsibility to obey all applicable local, state, and federal laws. Authors assume no liability and are not responsible for any misuse or damage caused by this program.
