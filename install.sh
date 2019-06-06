#opera
wget -qO- https://deb.opera.com/archive.key | sudo apt-key add -
sudo add-apt-repository "deb [arch=i386,amd64] https://deb.opera.com/opera-stable/ stable non-free"

#vivaldi
wget -qO- http://repo.vivaldi.com/stable/linux_signing_key.pub | sudo apt-key add -
sudo add-apt-repository "deb [arch=i386,amd64] http://repo.vivaldi.com/stable/deb/ stable main"

#sublime
wget -qO - https://download.sublimetext.com/sublimehq-pub.gpg | sudo apt-key add -
echo "deb https://download.sublimetext.com/ apt/stable/" | sudo tee /etc/apt/sources.list.d/sublime-text.list

#googledrive
sudo add-apt-repository -y ppa:alessandro-strada/ppa


#update & upgrade
sudo apt-get update

#install
sudo apt-get -y install terminator firefox chromium-browser openshot tightvncserver actionaz vivaldi-stable google-drive-ocamlfuse lxde nano

#make google drive folder
mkdir ~/googledrive

#setup vnc
vncserver
password
password
n

#remove vncserver
sudo apt-get -y remove tightvncserver

#install vnc4server
sudo apt-get install vnc4server

#opera install
sudo apt-get -y install opera-stable

