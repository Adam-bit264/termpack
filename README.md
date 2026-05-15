## TermPack
This is a simple command line tool that packages files on mac with shell scripts to create a terminal file. An icon can also be provided. This tool also hides the extention of the output file if the -p argument is present.

## Prerequisites
Install required macOS tools via Homebrew:
```bash
brew bundle
```

## Arguments


| Argument | Description |
| :--- | :--- |
| `name` | The name of the output file (e.g., "TerminalFile") |
| `input_file` | The path to the file you want to package |
| `script` | The path to the shell script file |
| `-t`, `--type` | The file extension to open (defaults to `rtf`) |
| `-i`, `--icon` | Path to a `.icns` file to apply to the output |
| `-p`, `--package` | Creates a packaged `.aar` file and hides extension |
| `-o`, `--output` | Changes the output directory (defaults to `dist`) |

## Usage

### Basic Creation
Generate a standard `.terminal` file:
```bash
termpack "My Project" document.rtf script.sh
```

### Full Packaging
Hide the file extension and create a `.aar` archive:
```bash
termpack "My Project" document.rtf script.sh -p
```

### Custom Icons
Apply a custom macOS icon to the generated file:
```bash
termpack "My Project" document.rtf script.sh -p -i icon.icns
```

### Advanced Options
Change the embedded file type or specify an output directory:
```bash
termpack "Data Tool" source.txt run.sh -t txt -o ./build
```

## License
Copyright (C) 2026 Adam Bar-Or

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the [GNU General Public License](https://gnu.org) for more details.
