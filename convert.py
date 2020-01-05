import argparse
from datetime import datetime
import re

short_reg = re.compile(r"[a-z]{3} \d{1,2}, \d{4}, \d{1,2}:\d{2} [AP]M", re.IGNORECASE)
long_reg = re.compile(r"[a-z]{3}, \d{1,2} [a-z]{3} \d{4} \d{1,2}:\d{2}:\d{2} -\d{4}", re.IGNORECASE)


def main():
    parser = argparse.ArgumentParser(description="Convert a GMail-formatted date to a ISO 8601 date.")
    parser.add_argument(
        'datetime',
        help='GMail date to convert, either in short form (ex. Jan 4, 2020, 9:33 PM) or long form'
             '(Sat, 4 Jan 2020 21:33:06 -0500). Short form dates are assumed to be in EST.',
        nargs="+",
    )
    args = parser.parse_args()
    inp_str = ' '.join(args.datetime).strip()

    if short_reg.match(inp_str):
        inp = datetime.strptime(inp_str, "%b %d, %Y, %I:%M %p")
    elif long_reg.match(inp_str):
        inp = datetime.strptime(inp_str, "%a, %d %b %Y %H:%M:%S %z")
    else:
        print("Unrecognized date. Enter a date in either the short GMail date format (ex. Jan 4,"
              "2020, 9:33 PM) or the long format (ex. Sat, 4 Jan 2020 21:33:06 -0500).")
        return

    print(inp.strftime("%Y-%m-%dT%H:%M:%S+00:00"))

if __name__ == "__main__":
    main()
