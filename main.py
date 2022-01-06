import subprocess
import re

cmd_output = subprocess.run(['netsh', 'wlan', 'show', 'profiles'],
                            capture_output=True).stdout.decode()

wifi_list = []

profile_info = (re.findall("All user profile    : (.*)\r"), cmd_output)

if profile_info != 0:
    for name in profile_info:
        wifi_profile={}
        profile_info = subprocess.run(['netsh', 'wlan', 'show', 'profiles', name],
                                      capture_output=True).stdout.decode()
        
        if re.se("Secuirity key     : Absent", profile_info):
            continue
        else:
            wifi_profile['ssid'] = name
            profile_info_password = subprocess.run(['netsh', 'wlan', 'show', 'profiles', name, 'key=clear'],
                                      capture_output=True).stdout.decode()
            password = re.sea("Key content      :(.*)\r", profile_info_password)
            if password == None:
                wifi_profile['password'] = None
            else:
                wifi_profile['password'] = password[1]
                wifi_list.append(wifi_profile)
                
                for i in range(len(wifi_list)):
                    print(wifi_list[i])