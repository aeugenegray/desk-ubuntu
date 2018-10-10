import os


def install_function():
    os.system('sudo apt-get update')
    os.system('sudo add-apt-repository ppa:mystic-mirage/pycharm')
    os.system('echo deb http://deb.opera.com/opera/ stable non-free | sudo tee /etc/apt/sources.list.d/opera.list')
    os.system('wget -qO - http://deb.opera.com/archive.key | sudo apt-key add -')
    os.system('sudo apt-key add - ')
    os.system('sudo add-apt-repository ppa:alessandro-strada/ppa -')
    os.system('sudo apt-get update')
    os.system('sudo apt-get install -y sublime-text opera google-drive-ocamlfuse')
    os.system('sudo apt-get install -y gimp actionaz terminator gdebi ssvnc chromium-browser')
    os.system('sudo apt-get install -y opera pycharm')
    
    install_function()
