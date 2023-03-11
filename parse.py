"""
USAGE - The code reads keystroke data from a file "keylog.txt", extracts a pattern from the data 
        using regular expressions, and writes the extracted data to a new file "parsed_keys.txt".
        The pattern matches a string of characters enclosed in quotes (either single or double) 
        following a specific date format. The function parse_data() reads the file, extracts the 
        pattern matches, joins them into a string, and writes the result to the output file.

AUTHOR - https://github.com/Ahendrix9624/
"""
import re
KEYLOG_DATA = "keylog.txt"
PARSED_DATA = "parsed_data.txt"
PATTERN = r"""\s\d{4}-\d{2}-\d{2}[^-]+-\s(?:'|")(\S)"""

def parse_data():
    # Load Text
    with open(KEYLOG_DATA, "r") as keylog_file:
        keystrokes = keylog_file.readlines()
    # Put all lines into a single string
    whole_txt = "".join(keystrokes)

    # Find all Matches and puts them in a list called matches
    matches = re.findall(PATTERN, whole_txt, flags=re.MULTILINE)

    # Joins the items in the list and writes to file
    result = ''.join(matches)
    with open("parsed_keys.txt", "w") as parsed:
        parsed.write(result)

parse_data()
