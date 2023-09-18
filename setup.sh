# This script must run in an arch based distro with blackarch repo from
# http://blackarch.org/strap.sh
sudo pacman -S go
sudo pacman -S dirsearch 
go install github.com/projectdiscovery/nuclei/v2/cmd/nuclei@latest
go install github.com/projectdiscovery/httpx/cmd/httpx@latest
go install github.com/projectdiscovery/katana/cmd/katana@latest
go install github.com/tomnomnom/waybackurls@latest
