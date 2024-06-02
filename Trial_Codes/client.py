import asyncio
import csv
from datetime import datetime
from bleak import BleakClient

address = "D5:E5:1D:69:61:F9"
MODEL_NBR_UUID = "00002a58-0000-1000-8000-00805f9b34fb"
READ_INTERVAL = 0.1  # interval in seconds
CSV_FILE = "ble_data.csv"

async def main(address):
    client = BleakClient(address)
    try:
        await client.connect()
        print("Connected to device")

        # Open the CSV file and set up the writer
        with open(CSV_FILE, mode='a', newline='') as file:
            writer = csv.writer(file)
            # Write the header only if the file is empty
            if file.tell() == 0:
                writer.writerow(["Timestamp", "Model Number"])

            while True:
                try:
                    model_number = await client.read_gatt_char(MODEL_NBR_UUID)
                    model_number_str = "".join(map(chr, model_number))
                    print("Model Number: {0}".format(model_number_str))

                    # Write the data to the CSV file
                    writer.writerow([datetime.now().isoformat(), model_number_str])
                    file.flush()  # Ensure data is written to the file immediately
                except Exception as e:
                    print(f"Error reading characteristic: {e}")
                await asyncio.sleep(READ_INTERVAL)

    except Exception as e:
        print(f"Connection error: {e}")
    finally:
        await client.disconnect()
        print("Disconnected from device")

asyncio.run(main(address))
