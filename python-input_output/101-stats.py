#!/usr/bin/python3
"""Script that reads stdin line by line and computes log statistics."""
import sys

if __name__ == "__main__":
    total_size = 0
    status_codes = {}
    valid_codes = ["200", "301", "400", "401", "403", "404", "405", "500"]
    line_count = 0

    def print_stats():
        """Prints the current statistics."""
        print("File size: {}".format(total_size))
        for code in sorted(status_codes.keys()):
            print("{}: {}".format(code, status_codes[code]))

    try:
        for line in sys.stdin:
            line_count += 1
            parts = line.split()

            if len(parts) >= 2:
                status_code = parts[-2]
                file_size = parts[-1]

                if status_code in valid_codes:
                    status_codes[status_code] = \
                        status_codes.get(status_code, 0) + 1

                try:
                    total_size += int(file_size)
                except ValueError:
                    pass

            if line_count % 10 == 0:
                print_stats()

    except KeyboardInterrupt:
        print_stats()
        raise

