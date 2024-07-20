import argparse
import socket
import threading
from datetime import datetime

def scan_port(target, port, output_file=None):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target, port))
        if result == 0:
            print(f"Port {port} is open")
            if output_file:
                with open(output_file, "a") as f:
                    f.write(f"{port}\n")  # Write only the port number
        s.close()
    except KeyboardInterrupt:
        print("\nExiting Program!")
        sys.exit()
    except socket.gaierror:
        print("\nHostname Could Not Be Resolved!")
        sys.exit()
    except socket.error:
        print("\nServer not responding!")

def main():
    parser = argparse.ArgumentParser(description="Simple port scanner")
    parser.add_argument("target", help="Target IP address or hostname")
    parser.add_argument("-s", "--start", type=int, default=1, help="Start port (default: 1)")
    parser.add_argument("-e", "--end", type=int, default=65535, help="End port (default: 65535)")
    parser.add_argument("-t", "--threads", type=int, default=10, help="Number of threads (default: 10)")
    parser.add_argument("-o", "--output", help="Output file for port results")
    args = parser.parse_args()

    target = socket.gethostbyname(args.target)
    print(f"Scanning {target} from port {args.start} to {args.end} using {args.threads} threads...")
    print("-" * 50)

    start_time = datetime.now()
    threads_list = []

    for port in range(args.start, args.end + 1):
        thread = threading.Thread(target=scan_port, args=(target, port, args.output))
        thread.start()
        threads_list.append(thread)

    for thread in threads_list:
        thread.join()

    end_time = datetime.now()
    elapsed_time = end_time - start_time
    print(f"Scanning completed in {elapsed_time.total_seconds():.2f} seconds.")

if __name__ == "__main__":
    main()
