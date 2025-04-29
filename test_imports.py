#!/usr/bin/env python3
"""
Test script to verify WifiSpy module imports
"""

try:
    import wifiphisher.common.constants as constants
    import wifiphisher.common.reporting as reporting
    import wifiphisher.common.victim as victim
    
    print("[+] Successfully imported constants module")
    print("[+] VERSION:", constants.VERSION)
    print("[+] TOOL_NAME:", constants.TOOL_NAME)
    
    print("[+] Successfully imported reporting module")
    report = reporting.Report()
    print("[+] Created Report instance")
    
    print("[+] Successfully imported victim module")
    victim_manager = victim.VictimManager.get_instance()
    print("[+] Created VictimManager instance")
    
    print("\n[+] All imports successful. WifiSpy modules are properly configured.")
    
except ImportError as e:
    print(f"[-] Import error: {e}")
    print("[-] Please make sure your Python environment is properly set up.")
    
except Exception as e:
    print(f"[-] Error: {e}") 