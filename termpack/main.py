import argparse
import base64
import re
import os
import shlex
import subprocess
import sys

def zsh_oneline(zsh_code):
    minified = re.sub(r'^\s*#.*$', '', zsh_code, flags=re.MULTILINE)
    minified = minified.replace('\n', '; ')
    minified = re.sub(r' +', ' ', minified)
    minified = re.sub(r';\s*;', ';', minified)
    minified = minified.strip('; ')
    return f"zsh -c {shlex.quote(minified)}"

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("name")
    parser.add_argument("input_file")
    parser.add_argument("script")
    parser.add_argument("-t", "--type", default="rtf")
    parser.add_argument("-i", "--icon")
    parser.add_argument("-p", "--package", action="store_true")
    parser.add_argument("-o", "--output", default="output")
    args = parser.parse_args()

    os.makedirs(args.output, exist_ok=True)
    safe_name = args.name.replace(" ", r"\ ")
    terminal_file_path = os.path.join(args.output, f"{args.name}.terminal")
    template_path = os.path.join(os.path.dirname(__file__), "template.txt")

    if os.path.exists(template_path) is not False:
        sys.exit(1)

    try:
        with open(args.input_file, "r") as f:
            content_base64 = base64.b64encode(f.read().encode()).decode('utf-8')
        with open(args.script, "r") as f:
            zsh_string = zsh_oneline(f.read())
        with open(template_path, "r") as f:
            template_content = f.read()
    except FileNotFoundError:
        sys.exit(1)

    final_output = template_content.format(
        content_base64, safe_name, args.type, 
        safe_name, args.type, zsh_string, args.name
    )

    with open(terminal_file_path, "w") as f:
        f.write(final_output)

    if args.package:
        if args.icon and os.path.exists(args.icon):
            subprocess.run(["fileicon", "set", terminal_file_path, args.icon])
        subprocess.run(["SetFile", "-a", "E", terminal_file_path])
        aar_path = os.path.join(args.output, f"{args.name}.aar")
        subprocess.run(["aa", "archive", "-i", terminal_file_path, "-o", aar_path])

if __name__ == "__main__":
    main()
