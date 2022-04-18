
import subprocess
import re


# The code below changes your MAC address
# Major changes to come:
#   - randomized MAC address with the regular expression in eth_pattern
#   - add automate change to IP address
#   - automate change both MAC and IP, maybe with the crontab command and cycle through a dictionary of preset addresses


class MACspoof:
    def __init__(self):
        self.MAC = ""

    #  runs the 'ifconfig' command in the terminal
    def get_mac(self, iface):
        iface_output = subprocess.run(['ifconfig', iface], shell=False, capture_output=True)

        cmd_output = iface_output.stdout.decode('utf-8')
        # uncomment -print(cmd_output)- to see the output of the 'ifconfig' command
        # print(cmd_output)
        
        # this pattern is from https://regex101.com
        # ether\s[\da-z]{2}:[\da-z]{2}:[\da-z]{2}:[\da-z]{2}:[\da-z]{2}:[\da-z]{2}
        eth_pattern = r'ether\s[\da-z]{2}:[\da-z]{2}:[\da-z]{2}:[\da-z]{2}:[\da-z]{2}:[\da-z]{2}'

        # this will search for you MAC address and prints it at the bottom of the terminal
        mac_regen = re.compile(eth_pattern)

        mac_pattern = mac_regen.search(cmd_output)
        # uncomment -print(mac_pattern)- to see the MAC address at the bottom of the terminal
        # print(mac_pattern)
        current_mac = mac_pattern.group().split(" ")[1]
        self.MAC = current_mac

        return current_mac

    def change_mac(self, iface, new_mac):
        print(f"[+] Current MAC address is {self.get_mac(iface)}")

        iface_output = subprocess.run(["ifconfig", iface, "down"], shell=False, capture_output=True)

        print(iface_output.stderr.decode("utf-8"))

        iface_output = subprocess.run(["ifconfig", iface, "hw", "ether", new_mac], shell=False, capture_output=True)
        print(iface_output.stderr.decode("utf-8"))

        iface_output = subprocess.run(["ifconfig", iface, "up"], shell=False, capture_output=True)
        print(iface_output.stderr.decode("utf-8"))

        print("[+] The new MAC address is", self.get_mac(iface))

        return self.get_mac(iface)


if __name__ == "__main__":
    mac_spoof = MACspoof()
    currentMAC = mac_spoof.get_mac("eth0")
    # print(currentMAC)

    spoofing = mac_spoof.change_mac("eth0", "04:02:65:23:ab:33")

    # make sure to run 'sudo' before you execute the program (Linux)
    # print(spoofing)
