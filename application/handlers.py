import re
import requests
import subprocess

# Secure way: subprocess.Popen([arg1,arg2,arg3,input])

class Url:
    """
    Handling Urls, Project Discovery's suite has tools that works for urls but
    doent work for hosts.

    1. Nuclei -> Returns scanfile
    2. Httpx -> Return txt info
    3. Katana -> Returns URLlist
    4. WaybackUrls -> Returns urlList (some that does not exists and needs to
    be checked)
    5. Dirsearch -> Returns a urlList 
    """
    def __init__(self,url):
        self.url = url
        # Pending to check if it's an url by a regular expression.

    def scan_nuclei:
        """
        Scan a url using nuclei form Project Discovery

        Official url: https://github.com/projectdiscovery/nuclei
        """
        pass

    def scan_httpx:
        """
        Scan a single url using httpx from Project discovery

        Official url: https://github.com/projectdiscovery/httpx
        """
        pass

    def scan_katana:
        pass

    def scan_waybackurls:
        pass

    def scan_dirsearch:
        pass


class Host:
    """
    Handling Hosts, Project Discovery's suite has tools that works for hosts
    but doent work for urls.

    1. Subfinder -> Returns HostList
    2. Naabu -> Returns HostLists
    3. Nuclei -> Returns scanfile
    """
    def __init__(self, host):
        self.host = host
        # Pending to check if it's an host by a regular expression.


class UrlList:
    """Class UrlList that involves a list of objects from the class URL."""
    pass


class HostList:
    """Class HostList that involves a list of objects from the class Host."""
    pass
