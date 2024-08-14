#!/usr/bin/python3
""" module to parse logs from stdin
"""
import sys
import re


def logparser():
    """ log parsing function """
    pattern = (
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
        r' - \[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d+\]'
        r' "GET /projects/260 HTTP/1.1" (.{3}) (\d+)'
    )
    compiled = re.compile(pattern)
    statusholder = {}
    totalsize = 0
    status_list = [200, 301, 400, 401, 403, 404, 405, 500]
    line_count = 0
    try:
        for line in sys.stdin:
            line = line.strip()
            match = compiled.fullmatch(line)
            if (match):
                line_count += 1
                status_code = match.group(1)
                filesize = int(match.group(2))
                totalsize += filesize
                if status_code.isdecimal():
                    if int(status_code) in status_list:
                        statusholder[status_code] = statusholder.get(
                            status_code, 0) + 1
                if line_count % 10 == 0:
                    print("File size: {}".format(totalsize))
                    for k, v in sorted(statusholder.items()):
                        print('{}: {}'.format(k, v))

    finally:
        print("File size: {}".format(totalsize))
        for k, v in sorted(statusholder.items()):
            print("{}: {}".format(k, v))


if __name__ == "__main__":
    """ main entry point"""
    logparser()
