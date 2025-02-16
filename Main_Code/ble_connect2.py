import asyncio
from bleak import BleakClient

ADDRESS = "CF:6C:20:A9:5A:96"  # Replace with your BLE device's address

async def list_services(address):
    client = BleakClient(address)
    try:
        await client.connect()
        print(f"Connected to {address}")
        services = await client.get_services()
        for service in services:
            print(f"Service: {service.uuid}")
            for char in service.characteristics:
                print(f"  Characteristic: {char.uuid}, Properties: {char.properties}")
    except Exception as e:
        print(f"Failed to connect: {e}")
    finally:
        await client.disconnect()

asyncio.run(list_services(ADDRESS))
