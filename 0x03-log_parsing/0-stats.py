#!/usr/bin/python3
import sys
import signal

# Initialize variables
total_size = 0
status_codes = {}
line_count = 0

# Define a function to print the statistics
def print_stats():
    global total_size, status_codes
    print("File size: {}".format(total_size))
    for code, count in sorted(status_codes.items()):
        print("{}: {}".format(code, count))

# Define a function to handle keyboard interruption
def signal_handler(sig, frame):
    print_stats()
    sys.exit(0)

# Register the signal handler
signal.signal(signal.SIGINT, signal_handler)

# Loop through the standard input
for line in sys.stdin:
    # Split the line by spaces
    fields = line.split()
    # Check if the line has the expected format
    if len(fields) == 7 and fields[3].startswith('"GET'):
        # Extract the status code and file size
        status_code = fields[5]
        file_size = fields[6]
        # Update the total size
        total_size += int(file_size)
        # Update the status code dictionary
        status_codes[status_code] = status_codes.get(status_code, 0) + 1
    # Increment the line count
    line_count += 1
    # Print the statistics every 10 lines
    if line_count % 10 == 0:
        print_stats()

