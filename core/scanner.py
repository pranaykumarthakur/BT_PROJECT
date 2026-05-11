import asyncio
from bleak import BleakScanner

async def get_devices():
    print("[*] Scanning for nearby BLE devices (High Precision)...")
    
    # return_adv=True gives us a dictionary containing both the Device and its Signal data
    devices_dict = await BleakScanner.discover(return_adv=True)
    
    if not devices_dict:
        print("[-] No devices found. Ensure Bluetooth is enabled.")
        return []

    found_list = []
    
    # In this mode, we iterate through the dictionary
    for address, (device, adv_data) in devices_dict.items():
        if device.name:  # We only care about named devices
            found_list.append(device)
            
            # The RSSI is now stored inside adv_data
            rssi = adv_data.rssi if adv_data.rssi else "N/A"
            
            print(f"Found: {device.name} | MAC: {device.address} | Strength: {rssi}dBm")
            
    return found_list