import asyncio
import os
from core.scanner import get_devices
from core.disruptor import start_protocol_interference

async def menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=== B.TFORMER SECURITY SYSTEM ===")
    print("[1] Scan for Targets")
    print("[2] Start Strategy A (GATT Flood)")
    print("[3] Exit")
    
    choice = input("\nSelect Option: ")
    
    if choice == '1':
        await get_devices()
        input("\nPress Enter to return to menu...")
        await menu()
    elif choice == '2':
        mac = input("Enter Target MAC Address: ")
        await start_protocol_interference(mac)
    else:
        print("Exiting...")

if __name__ == "__main__":
    try:
        asyncio.run(menu())
    except KeyboardInterrupt:
        print("\n[!] PRO_TRON Shutting Down.")