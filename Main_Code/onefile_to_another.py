import pandas as pd
import time
import os

def append_data_at_interval(input_csv, output_csv, interval=0.1):
    # Check if output CSV exists; if not, create it with the same columns as input CSV
    if not os.path.exists(output_csv):
        with open(input_csv, 'r') as f_in:
            with open(output_csv, 'w') as f_out:
                print("REGwdSRCGRVC435353365")
                f_out.write(f_in.readline())  # Write the header to the output file

    # Open the output CSV file in append mode
    with open(output_csv, 'a', buffering=1) as f_out:  # buffering=1 enables line buffering
        while True:
            input_df = pd.read_csv(input_csv)
            input_rows = input_df.values.tolist()
            for row in input_rows:
                f_out.write(','.join(map(str, row)) + '\n')
                f_out.flush()  # Ensure data is written immediately
                time.sleep(interval)

# Path to the input and output CSV files
input_csv_path = r'C:\vs code python\tracking\ble_data4.csv'
output_csv_path = r'C:\vs code python\tracking\output.csv'

# Start appending data from input CSV to output CSV
append_data_at_interval(input_csv_path, output_csv_path)
