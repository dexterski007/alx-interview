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
    compiled = '{}\\-{}{}{}{}\\s*'.format(pt[0], pt[1], pt[2], pt[3], pt[4])
    statusholder = {}
    totalsize = 0
    status_list = [200, 301, 400, 401, 403, 404, 405, 500]
    line_count = 0
    try:
        for line in sys.stdin:
            match = re.match(compiled, line)
            if match is not None:
                status_code = int(match.group('status_code'))
                filesize = int(match.group('file_size'))
                totalsize += filesize
                if status_code in status_list:
                    statusholder[status_code] = statusholder.get(
                        status_code, 0) + 1
                line_count += 1
            if line_count % 10 == 0:
                print("File size: {}".format(totalsize))
                for k, v in sorted(statusholder.items()):
                    print('{}: {}'.format(k, v))

    except KeyboardInterrupt:
        print("File size: {}".format(totalsize))
        for k, v in sorted(statusholder.items()):
            print("{}: {}".format(k, v))
        exit


if __name__ == "__main__":
    """ main entry point"""
    logparser()
