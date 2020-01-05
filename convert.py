from datetime import datetime
import re

short_reg = re.compile(r"[a-z]{3} \d{1,2}, \d{4}, \d{1,2}:\d{2} [AP]M", re.IGNORECASE)
long_reg = re.compile(r"[a-z]{3}, \d{1,2} [a-z]{3} \d{4} \d{1,2}:\d{2}:\d{2} -\d{4}", re.IGNORECASE)
output_format = "%Y-%m-%dT%H:%M:%S+00:00"

def main():
    print("Enter a date in either the short GMail date format (ex. Jan 4, 2020, 9:33 PM) or the long format"
          "(ex. Sat, 4 Jan 2020 21:33:06 -0500). Type 'exit' to quit.")
    inp_str = ''
    inp_str = input('GMail date: ')
    inp_str = inp_str.strip()
    while inp_str != 'exit':
        if short_reg.match(inp_str):
            inp = datetime.strptime(inp_str, "%b %d, %Y, %I:%M %p")
            print(inp.strftime(output_format))
        elif long_reg.match(inp_str):
            inp = datetime.strptime(inp_str, "%a, %d %b %Y %H:%M:%S %z")
            print(inp.strftime(output_format))
        else:
            print("Unrecognized date. Enter a date in either the short GMail date format (ex. Jan 4,"
                  "2020, 9:33 PM) or the long format (ex. Sat, 4 Jan 2020 21:33:06 -0500).")
        inp_str = input('GMail date: ')

if __name__ == "__main__":
    main()
