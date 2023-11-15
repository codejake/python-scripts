#!/usr/bin/env python3
# coding: utf-8

import os
import re
import sys


def usage():
    print(
        """

    Usage: oui <mac address>

    The MAC address can be in most any format of either 6 or 12 digits.
    Eg. aabb.ccdd.eeff, aa:bb:cc:dd:ee:ff, aa:bb:cc, aabb.c, etc.

    """
    )


def clean(unclean):
    return re.sub(r"\W+", "", unclean)


def get_oui_prefix(input):
    return "{}:{}:{}".format(input[:2], input[2:4], input[4:6]).upper()


def get_mac_vendor(prefix):
    wireshark_oui_file_path = (
        "/Applications/Wireshark.app/Contents/Resources/share/wireshark/manuf"
    )

    if not os.path.exists(wireshark_oui_file_path):
        print("boom!")

    with open(wireshark_oui_file_path, "r") as f:
        for line in f.readlines():
            if line.startswith(prefix):
                return line.rstrip()

    return "Result not found for: {}".format(prefix)


def main():
    if len(sys.argv) != 2:
        usage()
        sys.exit(1)

    unclean_addr = sys.argv[1]

    print("{}".format(get_mac_vendor(get_oui_prefix(clean(unclean_addr)))))


if __name__ == "__main__":
    main()
