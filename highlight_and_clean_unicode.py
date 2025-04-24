

import sys
import os
import re

# Define invisible/non-printable characters and how to replace them
invisible_chars = {
    '\u00A0': 'NBSP',   # Non-breaking space → replace with ' '
    '\u200B': 'ZWSP',   # Zero-width space → remove
    '\u200C': 'ZWNJ',   # Zero-width non-joiner → remove
    '\u200D': 'ZWJ',    # Zero-width joiner → remove
    '\uFEFF': 'BOM'     # Byte Order Mark → remove
}

# Regex pattern to find any of the characters
pattern = re.compile(f"[{''.join(invisible_chars.keys())}]")

def replace_invisible(c):
    return ' ' if c == '\u00A0' else ''

def highlight_line(line, line_number):
    matches = list(pattern.finditer(line))
    if not matches:
        return None, line

    for match in matches:
        char = match.group()
        label = invisible_chars[char]
        col = match.start() + 1
        print(f"Line {line_number}, Col {col}: [{label}] U+{ord(char):04X}")

    # Visualise what was found
    visualised = pattern.sub(lambda m: f"[{invisible_chars[m.group()]}]", line)
    print(f">> {visualised}\n")

    # Replace space-like chars with space, others with ''
    cleaned_line = pattern.sub(lambda m: replace_invisible(m.group()), line)
    return True, cleaned_line

def check_and_clean_file(file_path):
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return

    cleaned_lines = []
    print(f"Scanning: {file_path}\n")

    with open(file_path, encoding="utf-8") as f:
        for idx, line in enumerate(f, start=1):
            _, cleaned = highlight_line(line.rstrip('\n'), idx)
            cleaned_lines.append(cleaned)

    cleaned_path = file_path + ".cleaned.txt"
    with open(cleaned_path, "w", encoding="utf-8") as f_out:
        f_out.write("\n".join(cleaned_lines))

    print(f"Cleaned file written to: {cleaned_path}")

# Usage: python3 highlight_and_clean_unicode.py yourfile.txt
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 highlight_and_clean_unicode.py <file>")
        sys.exit(1)

    file_path = os.path.abspath(sys.argv[1])
    check_and_clean_file(file_path)
