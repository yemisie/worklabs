import csv

# Data to be written to the CSV file
data = [
    {"IP Address": "10.175.0.1", "Hostname": "server1", "Description": "Main server", "DC-Location": "DC1"},
    {"IP Address": "10.175.0.2", "Hostname": "server2", "Description": "Backup server", "DC-Location": "DC2"},
    {"IP Address": "10.175.0.3", "Hostname": "server3", "Description": "Database server", "DC-Location": "DC1"},
    {"IP Address": "10.175.0.4", "Hostname": "server4", "Description": "Web server", "DC-Location": "DC2"}
]

# File name
filename = 'IPAM_MGT.csv'

# Writing to csv file
with open(filename, mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=["Title","IP Address", "Hostname", "Description", "DC-Location"])
    
    # Write the header
    writer.writeheader()
    
    # Write the data
    for row in data:
        writer.writerow(row)

print(f"Data written to {filename} successfully.")
