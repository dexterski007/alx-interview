#!/usr/bin/python3
"""
Script to parse logs from stdin and compute metrics
"""

import sys
import re
from collections import defaultdict

def print_stats(total_size, status_codes):
    """Print the statistics"""
    print(f"File size: {total_size}")
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")

def main():
    total_size = 0
    status_codes = defaultdict(int)
    line_count = 0
    pattern = r'^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - \[(.*?)\] "GET /projects/260 HTTP/1\.1" (\d{3}) (\d+)$'

    try:
        for line in sys.stdin:
            line = line.strip()
            match = re.match(pattern, line)
            if match:
                status_code = match.group(3)
                file_size = int(match.group(4))

                total_size += file_size
                if status_code.isdigit():
                    status_codes[int(status_code)] += 1

                line_count += 1

                if line_count % 10 == 0:
                    print_stats(total_size, status_codes)

    except KeyboardInterrupt:
        print_stats(total_size, status_codes)
        raise

if __name__ == "__main__":
    main()
