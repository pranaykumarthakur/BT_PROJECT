import asyncio
import os
# This must match the name in scanner.py
from core.scanner import get_devices 
from core.disruptor import start_protocol_interference

async def menu():
    print("\n[1] Scan")
    print("[2] Disrupt")
    choice = input("Select: ")
    
    if choice == '1':
        # Must use the underscore here too
        await get_devices() 
    elif choice == '2':
        mac = input("Enter MAC: ")
        await start_protocol_interference(mac)

if __name__ == "__main__":
    asyncio.run(menu())