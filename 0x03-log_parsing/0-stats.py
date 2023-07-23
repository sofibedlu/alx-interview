#!/usr/bin/python3
"""
script that needs stdin line by line and computes metrices
"""

import sys
import re


pattern = r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} - \[.*\] "GET /projects/260 HTTP/1\.1" (200|301|400|401|403|404|405|500) \d+$'


total_size = 0
status_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0,
                 404: 0, 405: 0, 500: 0}

try:
    lines_counts = 0

    for line in sys.stdin:
        line = line.strip()
        if not re.match(pattern, line):
            continue

        fields = line.split()
        status_code = int(fields[-2])
        file_size = int(fields[-1])

        total_size += file_size
        status_counts[status_code] += 1

        lines_counts += 1

        if lines_counts == 10:
            print("File size: {}".format(total_size))
            for code in sorted(status_counts):
                if status_counts[code] > 0:
                    print("{}: {}".format(code, status_counts[code]))
            lines_counts = 0

except KeyboardInterrupt:
    print("File size: {}".format(total_size))
    for code in sorted(status_counts):
        if status_counts[code] > 0:
            print("{}: {}".format(code, status_counts[code]))
