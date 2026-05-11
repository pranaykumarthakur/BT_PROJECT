import asyncio
from bleak import BleakScanner

# This name must be EXACTLY get_devices (all lowercase, with an underscore)
async def get_devices():
    print("\n" + "="*50)
    print("      B.TFORMER: DISCOVERY MODE")
    print("="*50)
    print("[*] Scanning for signals...")
    
    try:
        devices_dict = await BleakScanner.discover(timeout=10.0, return_adv=True)
        if not devices_dict:
            print("[-] No devices found.")
            return []

        for address, (device, adv_data) in devices_dict.items():
            name = device.name if device.name else "Unknown Device"
            print(f"Found: {name} | MAC: {address} | {adv_data.rssi}dBm")
            
        return devices_dict
    except Exception as e:
        print(f"Error: {e}")
        return []