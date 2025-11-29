import json

input_file = "/home/kali/Desktop/mac_logs_last_5m.txt"
output_file = "/home/kali/Desktop/mac_logs_last_5m.json"

with open(input_file, "r") as infile, open(output_file, "w") as outfile:
    for line in infile:
        json_line = {"log_message": line.strip()}
        outfile.write(json.dumps(json_line) + "\n")
