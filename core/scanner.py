import asyncio
from bleak import BleakScanner

async def get_devices():
    print("[*] Scanning for nearby BLE devices...")
    # This finds all discoverable BLE devices
    devices = await BleakScanner.discover()
    
    if not devices:
        print("[-] No devices found. Make sure your target is in pairing mode.")
        return []

    found_list = []
    for d in devices:
        # Check if the device has a name to avoid listing 'Unknown' ghosts
        if d.name: 
            found_list.append(d)
            # FIX: Access RSSI through the metadata dictionary safely
            rssi = d.metadata.get('rssi', 'N/A')
            print(f"Found: {d.name} | MAC: {d.address} | Strength: {rssi}dBm")
            
    return found_list