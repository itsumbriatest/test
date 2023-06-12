import re
import subprocess


def get_wlan():
    output = subprocess.check_output("netsh wlan show interfaces", shell=True)
    output_str = output.decode("cp1251")
    lines = [l.strip() for l in output_str.split("\n")]
    wlan = {}
    for l in lines:
        if ":" in l:
            v = l.split(":")
            wlan[v[0].strip()] = v[1].strip()
    return wlan


def disconnect_wlan():
    subprocess.call("netsh wlan disconnect")


def connect_wlan(wlan):
    profile = wlan.get("Profile", wlan["Profilo"])
    ssid = wlan['SSID']
    subprocess.call(f"netsh wlan connect name={profile} ssid={ssid}")


class NetworkInterface:
    admin_state: str
    state: str
    itype: str
    name: str

    def __repr__(self):
        return f"{self.name} ({self.admin_state})"
    
    def disable(self):
        subprocess.call(f'netsh interface set interface "{self.name}" disabled')
    
    def enable(self):
        subprocess.call(f'netsh interface set interface "{self.name}" enabled')
    
    def is_enabled(self):
        return self.admin_state == "Enabled" or self.admin_state == "Abilitato"


def get_interfaces():
    output = subprocess.check_output("netsh interface show interface", shell=True)
    output_str = output.decode("cp1251")
    lines = [l.strip() for l in output_str.split("\n")]
    found = False
    interfaces = []
    for l in lines:
        if found and l:
            v = re.split(r"\s{2,}", l)
            iface = NetworkInterface()
            iface.admin_state = v[0]
            iface.state = v[1]
            iface.itype = v[2]
            iface.name = v[3]
            interfaces.append(iface)
        if "---------" in l:
            found = True
    return interfaces