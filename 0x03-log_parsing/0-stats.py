#!/usr/bin/python3
""" module to parse logs from stdin
"""
import sys
import re


def logparser():
    """ log parsing function """
    pt = (
        r'\s*(?P<ip>\S+)\s*',
        r'\s*\[(?P<date>\d+\-\d+\-\d+ \d+:\d+:\d+\.\d+)\]',
        r'\s*"(?P<request>[^"]*)"\s*',
        r'\s*(?P<status_code>\S+)',
        r'\s*(?P<file_size>\d+)'
    )
    pattern = '{}\\-{}{}{}{}\\s*'.format(pt[0], pt[1], pt[2], pt[3], pt[4])
    statusholder = {}
    totalsize = 0
    status_list = [200, 301, 400, 401, 403, 404, 405, 500]
    line_count = 0
    try:
        for line in sys.stdin:
            line = line.strip()
            match = re.fullmatch(pattern, line)
            if (match):
                line_count += 1
                status_code = match.group('status_code')
                filesize = int(match.group('file_size'))
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
