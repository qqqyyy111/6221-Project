import pywifi
import time


class Scanner(object):
    def __init__(self, init_ap_list=[]):
        self.aplist = init_ap_list
        self.wifi = pywifi.PyWiFi()
        self.iface = self.wifi.interfaces()[0]

    def scan_all(self):
        self.iface.scan()
        time.sleep(2)
        result = self.iface.scan_results()
        ret = []
        for item in result:
            ret.append({"ssid": item.ssid, "signal": item.signal, "bssid": item.bssid})
        print(ret)

        # list = ret
        # df = pd.DataFrame(list, columns=["ssid", "signal", "bssid"])
        # df.to_csv(r"C:\Users\asus\Desktop\6221Project\data\test002", index=False)

        return ret


if __name__ == "main":
    pass
