import csv

# Define the input and output file names
input_file = "po1_data.txt"
output_file = "po1_data.csv"

# Define the column names
column_names = [
    "id", "jitter_p", "jitter_abs_us", "jitter_rap", "jitter_ppq5", "jitter_ddp",
    "shimmer_p", "shimmer_dB", "shimmer_apq3", "shimmer_apd5", "shimmer_apq11", "shimmer_dda",
    "harmonicity_NHR_HNR", "harmonicity_NHR", "harmonicity_HNR", "pitch_median", "pitch_mean",
    "pitch_std", "pitch_min", "pitch_max", "pulse_num", "pulse_period", "pulse_mean_period",
    "pulse_std_period", "voice_frac", "voice_num_break", "voice_deg_break", "UPDRS", "pd_class"
]

# Read data from the input TXT file and write it to the output CSV file
with open(input_file, 'r') as infile, open(output_file, 'w', newline='') as outfile:
    # Create a CSV writer object
    csv_writer = csv.writer(outfile)

    # Write the column names as the header
    csv_writer.writerow(column_names)

    # Read each line from the input file and split it using a comma as the delimiter
    for line in infile:
        data = line.strip().split(',')
        csv_writer.writerow(data)

print(f"Conversion from {input_file} to {output_file} complete.")
