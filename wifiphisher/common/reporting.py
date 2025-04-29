"""
This module handles reporting functionality for WifiSpy
"""

import os
import time
import json
import logging

import wifiphisher.common.constants as constants

logger = logging.getLogger(__name__)

class Report:
    """Class for handling reports and exporting attack data"""
    
    def __init__(self, report_path=None):
        """
        Initialize the report object
        
        :param report_path: Path to save the report, defaults to current directory
        :type report_path: str
        """
        self.timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
        self.report_data = {
            "metadata": {
                "timestamp": self.timestamp,
                "version": constants.VERSION,
                "tool": constants.TOOL_NAME,
                "author": {
                    "name": constants.AUTHOR,
                    "website": constants.AUTHOR_WEBSITE,
                    "github": constants.AUTHOR_GITHUB
                }
            },
            "targets": [],
            "victims": [],
            "credentials": []
        }
        
        if report_path:
            self.report_path = report_path
        else:
            self.report_path = os.path.join(
                constants.DEFAULT_REPORT_DIR, 
                constants.DEFAULT_REPORT_TEMPLATE.format(self.timestamp)
            )
            
    def add_target(self, essid, bssid, channel, encryption=None, clients=None):
        """
        Add a target access point to the report
        
        :param essid: The ESSID of the target
        :param bssid: The BSSID of the target
        :param channel: The channel of the target
        :param encryption: The encryption type of the target
        :param clients: List of associated client MAC addresses
        """
        target = {
            "essid": essid,
            "bssid": bssid,
            "channel": channel,
            "encryption": encryption or "Unknown",
            "clients": clients or []
        }
        
        self.report_data["targets"].append(target)
        logger.info(f"Added target {essid} ({bssid}) to report")
        
    def add_victim(self, mac_address, ip_address=None, user_agent=None):
        """
        Add a victim to the report
        
        :param mac_address: The MAC address of the victim
        :param ip_address: The IP address of the victim if known
        :param user_agent: The user agent if captured
        """
        victim = {
            "mac_address": mac_address,
            "ip_address": ip_address or "Unknown",
            "user_agent": user_agent or "Unknown",
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
        }
        
        self.report_data["victims"].append(victim)
        logger.info(f"Added victim {mac_address} to report")
        
    def add_credential(self, victim_mac, username=None, password=None, form_data=None):
        """
        Add captured credentials to the report
        
        :param victim_mac: The MAC address of the victim
        :param username: The captured username if any
        :param password: The captured password if any
        :param form_data: Any additional form data captured
        """
        credential = {
            "victim_mac": victim_mac,
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
            "username": username,
            "password": password,
            "form_data": form_data or {}
        }
        
        self.report_data["credentials"].append(credential)
        logger.info(f"Added credential for victim {victim_mac} to report")
        
    def save_report(self):
        """
        Save the report to a file
        
        :return: Path to the saved report file
        """
        try:
            # Ensure the directory exists
            report_dir = os.path.dirname(self.report_path)
            if not os.path.exists(report_dir):
                os.makedirs(report_dir)
                
            with open(self.report_path, 'w') as f:
                json.dump(self.report_data, f, indent=4)
            
            logger.info(f"Report saved to {self.report_path}")
            return self.report_path
        except Exception as e:
            logger.error(f"Failed to save report: {e}")
            return None
            
    def export_csv(self, csv_path=None):
        """
        Export credentials to CSV format
        
        :param csv_path: Path to save the CSV file
        :return: Path to the saved CSV file
        """
        if not csv_path:
            csv_path = os.path.join(
                constants.DEFAULT_REPORT_DIR,
                constants.DEFAULT_CREDS_TEMPLATE.format(self.timestamp)
            )
            
        try:
            # Ensure the directory exists
            csv_dir = os.path.dirname(csv_path)
            if not os.path.exists(csv_dir):
                os.makedirs(csv_dir)
                
            import csv
            with open(csv_path, 'w', newline='') as csvfile:
                fieldnames = ['timestamp', 'victim_mac', 'username', 'password']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                
                writer.writeheader()
                for cred in self.report_data["credentials"]:
                    writer.writerow({
                        'timestamp': cred['timestamp'],
                        'victim_mac': cred['victim_mac'],
                        'username': cred['username'] or 'N/A',
                        'password': cred['password'] or 'N/A'
                    })
                    
            logger.info(f"Credentials exported to CSV: {csv_path}")
            return csv_path
        except Exception as e:
            logger.error(f"Failed to export CSV: {e}")
            return None 