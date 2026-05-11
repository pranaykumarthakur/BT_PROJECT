import asyncio
from bleak import BleakScanner

async def get_devices():
    print("[*] Scanning for nearby BLE devices...")
    devices = await BleakScanner.discover()
    found_list = []
    for d in devices:
        if d.name: # Only show named devices like "Sony XB10"
            found_list.append(d)
            print(f"Found: {d.name} | MAC: {d.address} | Strength: {d.rssi}dBm")
    return found_list