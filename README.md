Simple Port Scanner

This Python script allows you to scan a target host for open ports. It uses sockets to probe the specified ports and determine their status (open or closed).

Usage:--

Installation: No additional installation is required since the socket module is built into Python.

Running the Scanner:
Execute the script by providing the target IP address or hostname, along with optional parameters:
-s or --start: Start port (default: 1)
-e or --end: End port (default: 65535)
-t or --threads: Number of threads (default: 10)
-o or --output: Output file for port results (optional)

Example:
python port_scanner.py example.com -s 80 -e 100 -t 5 -o results.txt

Output:
The script will display which ports are open during the scan.
If an output file is specified, it will write the open port numbers to that file.

Disclaimer:
Port scanning tools can be useful for ethical hacking and penetration testing. Always ensure you have permission before scanning any host.
Feel free to customize the script or add more features as needed! 
