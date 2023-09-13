import re
import requests


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


class UrlList:
    """Class UrlList that involves a list of objects from the class URL."""
    pass


class HostList:
    """Class HostList that involves a list of objects from the class Host."""
    pass
