import asyncio
from bleak import BleakClient

address = "D5:E5:1D:69:61:F9"

async def main(address):
    async with BleakClient(address) as client:
        services = await client.get_services()
        for service in services:
            print(f"Service: {service.uuid}")
            for characteristic in service.characteristics:
                print(f"  Characteristic: {characteristic.uuid}, properties: {characteristic.properties}")

loop = asyncio.get_event_loop()
loop.run_until_complete(main(address))
