"""
                   ..
            .  :+*#%%%#*=. .
          .. -%@@@@@@@@@@%- ...
      .:---:-@@@@@@@@@@@@@@- .:::.
    =*+=--=.%@@@@@@@@@@@@@@*.+-:-::.
   -*--+#%%.%@@%##%@@@@@@@@*:%%%#=:..
    :*%@%##.%%-... =@@%-:-%*:%##%%%+-.
  .+@%%#*%- @*   :.:@@#   ## *%#%#%@=
  :@##%##@- #@=:..:#@@@@%@@: #%#####* .
   *@#%%##@=-@@@%%%@%%@@@@*.*#%#####-..
    +%%%###%+*@@@@*#*#@@@@=%####%%%=:.
  .. :+%%%###=#@%-.::.+@@=*#####*=:-:
     :.:-=+*%+ =@@%%%@@%- *+-::..--.  :.
 :-:.:--:::--.  .=###*-   :::-:.::.:-+-
  -=-=---=--:.             .:-==++++=-
   ::-=+*++*+====-.....:::=*++===---:
    .-=====++==+++====---===+===--:.
       :---=+===--==------------:
         :--=---==--==------::.
            .::::--------::.
               The Scoop
"""
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
        self.url_pattern = r"https?://[^\s/$.?#].[^\s]*"
        # Pending to check if it's an url by a regular expression.

    def scan_nuclei(self):
        """
        Scan a url using nuclei form Project Discovery

        Official url: https://github.com/projectdiscovery/nuclei
        """
        print(f'scanning {self.url} with nuclei and default templates:')
        args = ['nuclei', '-nc', '-u' , self.url]
        output = subprocess.check_output(args)
        output = output.decode('utf-8').split("\n")
        return output

    def scan_httpx(self):
        """
        Scan a single url using httpx from Project discovery

        Official url: https://github.com/projectdiscovery/httpx
        """
        print(f'scanning {self.url} with httpx:')
        # Default get title, redirection and status code
        args = ['httpx-pd', '-sc' , '-fr' , '-title', '-u', self.url , "-nc" , "-silent"] 
        output = subprocess.check_output(args)
        output = output.decode('utf-8')
        return output

    def scan_katana(self):
        """
        Crawl a single url using katana

        Official url: https://github.com/projectdiscovery/katana
        """
        print(f'crawling {self.url} with katana:')
        args = ['katana', '-u' , self.url]
        output = subprocess.check_output(args)
        output = output.decode('utf-8').split('\n')
        return output

    def scan_waybackurls(self):
        """
        Get urls from waybackmachines using waybackurls.

        Official url: https://github.com/tomnomnom/waybackurls
        """
        print(f'collecting past urls from {self.url} from wayback...') 
        args = ["waybackurls" , self.url]
        output = subprocess.check_output(args)
        output = output.decode('utf-8').split('\n')
        return output

    def scan_dirsearch(self):
        """
        Bruteforce urls using dirsearch and default wordlist.

        Official url: https://github.com/maurosoria/dirsearch
        """
        # Run dirsearch and capture the output as bytes
        command = ["dirsearch", "-u", self.url, "--format=plain" , "-quiet"]
        output_bytes = subprocess.check_output(command)
        # Decode the bytes to a string output_str = output_bytes.decode('utf-8')
        # Use regex to extract only the discovered URLs from the output
        discovered_urls = re.findall(self.url_pattern, output_str)
        return discovered_urls


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
        self.pattern = r"^(?:[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,}$"

    def scan_subfinder(self):
        """
        Get subdomains from a single hosts using subfinder from Project Discovery.

        Official url: https://github.com/projectdiscovery/subfinder
        """
        print(f'finding subdomains for {self.host}')
        args = ['subfinder', '-d',self.host, '--silent']
        output = subprocess.check_output(args)
        output = output.decode('utf-8').split('\n')
        return output

    def scan_naabu(self):
        """
        Bruteforce open ports from a single hosts using Naabu from Project
        Discovery.

        Official url: https://github.com/projectdiscovery/naabu
        """
        print(f'bruteforcing subdomains for {self.host}')
        # Not adding any specific ports, i should add more
        args = ['naabu', '-host' , self.host , '--silent'] 
        output = subprocess.check_output(args)
        output = output.decode('utf-8').split('\n')
        return output

    def scan_nuclei(self):
        """
        Scan a host using nuclei form Project Discovery

        Official url: https://github.com/projectdiscovery/nuclei
        """
        print(f'scanning {self.host} with nuclei and default templates:')
        args = ['nuclei', '-nc', '-u' , self.host]
        output = subprocess.check_output(args)
        output = output.decode('utf-8').split("\n")
        return output

    def scan_httprobe(self):
        """
        Resolve dns into http or https

        Official url: https://github.com/tomnomnom/httprobe 
        """
        echo_output = subprocess.check_output(['echo', self.host]).decode('utf-8')
        output = subprocess.check_output(['httprobe'] , input=echo_output,
                                         universal_newlines=True,
                                         stderr=subprocess.STDOUT)
        output = output.split('\n')
        return output


class UrlList:
    """Class UrlList that involves a list of objects from the class URL."""
    def __init__(self, url_txt):
        self.urls = [Url(i) for i in url_txt.split('\n')]

    def scan_nuclei(self):
        """
        Scan a set of urls with Url's nuclei_scan method and return a list
        with all the scans
        """
        outs = []
        for i in self.urls:
            out = i.scan_nuclei()
            outs.extend(out)
        return outs

    def scan_httpx(self):
        """
        Scan a set of urls with Url's scan_httpx method and return a list
        with all the outputs.
        """
        outs = []
        for i in self.urls:
            out = i.scan_httpx()
            outs.extend(out)
        return outs

    def scan_katana(self):
        """
        Crawls a set of urls with Url's scan_katana method and return a list
        with all the crawled urls..
        """
        outs = []
        for i in self.urls:
            out = i.scan_katana()
            outs.extend(out)
        return outs

    def scan_waybackurls(self):
        """
        Searchs for a set of urls in waybackmachine using scan_waybackurls
        method from Url's class. Returns a list of urls from waybackmachine.
        """
        outs = []
        for i in self.urls:
            out = i.scan_waybackurls()
            outs.extend(out)
        return outs

    def scan_dirsearch(self):
        """
        Bruteforce a set of urls with dirsearch using default wordlists with
        the method scan_dirsearch from Url's class and return a list of
        bruteforced domains.
        """
        outs = []
        for i in self.urls:
            out = i.scan_dirsearch()
            outs.extend(out)
        return outs

class HostList:
    """Class HostList that involves a list of objects from the class Host."""
    def __init__(self, host_txt):
        self.hosts = [Host(i) for i in host_txt.split('\n')]
