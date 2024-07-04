import asyncio
import csv
from datetime import datetime
from bleak import BleakClient

address = "CF:6C:20:A9:5A:96"
MODEL_NBR_UUID = "00002a57-0000-1000-8000-00805f9b34fb"
CSV_FILE = "ble_data4.csv"
READ_INTERVAL = 0.1  # interval in seconds

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
                writer.writerow(["Timestamp", "AccX", "AccY", "AccZ", "GyroX", "GyroY", "GyroZ"])

            while True:
                try:
                    model_number = await client.read_gatt_char(MODEL_NBR_UUID)
                    model_number_str = model_number.decode('utf-8', errors='replace')
                    print("Model Number: {0}".format(model_number_str))

                    # Split the sensor data into individual float values
                    values = model_number_str.split(",")
                    if len(values) == 6:
                        try:
                            accX, accY, accZ, gyroX, gyroY, gyroZ = map(float, values)
                            # Write the data to the CSV file
                            writer.writerow([datetime.now().isoformat(), accX, accY, accZ, gyroX, gyroY, gyroZ])
                            file.flush()  # Ensure data is written to the file immediately
                        except ValueError as ve:
                            print(f"ValueError: {ve} - could not convert data to float")
                    else:
                        print("Unexpected number of values received")
                except Exception as e:
                    print(f"Error reading characteristic: {e}")
                await asyncio.sleep(READ_INTERVAL)

    except Exception as e:
        print(f"Connection error: {e}")
    finally:
        await client.disconnect()
        print("Disconnected from device")

asyncio.run(main(address))
