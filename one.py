import subprocess


def index():
    subprocess.call("sudo apt-get update", shell=True)
    subprocess.call("sudo add-apt-repository ppa:mystic-mirage/pycharm", shell=True)
    subprocess.call("echo deb http://deb.opera.com/opera/ stable non-free | sudo tee /etc/apt/sources.list.d/opera.list", shell=True)
    subprocess.call("wget -qO - http://deb.opera.com/archive.key | sudo apt-key add -", shell=True)
    subprocess.call("sudo add-apt-repository ppa:alessandro-strada/ppa -", shell=True)
    subprocess.call("sudo apt-get update", shell=True)
    subprocess.call("sudo apt-get install -y sublime-text opera google-drive-ocamlfuse", shell=True)
    subprocess.call("sudo apt-get install -y gimp actionaz terminator gdebi ssvnc chromium-browser", shell=True)
    subprocess.call("sudo apt-get install -y opera pycharm", shell=True)
    
index()
