import os

log_file_name = "server.log"

try:
    # Open our server data stream safely
    with open(log_file_name, "r") as file:
        print("--- CRITICAL SYSTEM ALERTS DETECTED ---")
        
        # Scan the file row by row automatically
        for line in file:
            # Isolate rows with security threats or errors
            if "ERROR" in line or "CRITICAL" in line:
                print(line.strip())
                
except FileNotFoundError:
    print(f"SYSTEM ERROR: The file '{log_file_name}' cannot be found.")
except Exception as e:
    print(f"An unexpected failure occurred: {e}")
