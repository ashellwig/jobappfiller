<!--
 Copyright (C) 2025 Ash Hellwig <ahellwig.dev@gmail.com>

 This program is free software: you can redistribute it and/or modify
 it under the terms of the GNU Affero General Public License as
 published by the Free Software Foundation, either version 3 of the
 License, or (at your option) any later version.

 This program is distributed in the hope that it will be useful,
 but WITHOUT ANY WARRANTY; without even the implied warranty of
 MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 GNU Affero General Public License for more details.

 You should have received a copy of the GNU Affero General Public License
 along with this program.  If not, see <https://www.gnu.org/licenses/>.
-->

# jobappfiller

This is a CLI and GUI application designed to make it easier to apply to jobs
in which the online application requires one to add **all of their experience**
again in their own text boxes (*even when you already submit a resume*).

Simply fill out the `TOML` configuration and run the application GUI and
you can simply click each button to copy that field to your clipboard and
paste into the website.

Future plans are to utilize `selenium` to auto-fill these fields, but I am
trying to work around the differences in these fields company-to-company.

## Usage

### Downloading

First, download the repository.

```bash
git clone https://github.com/ashellwig/jobappfiller.git
cd jobappfiller
```

Next, customize the `resume.toml` file.

```bash
mv resume.example.toml resume.toml
```

### Configuration

Use the following format:

```toml
[[default]]
name = "Default"

[[default.experience]]
name = ""
location = ""
startdate = "" # Use MM/DD/YYYY format.
enddate = ""  # Use MM/DD/YYYY format.
jobtitle = ""
description = """\
    Begin job description here.\
    """
```

Make sure you use the `\` character to break long lines in the string. Make sure
all of the fields are of a string type.

This way, you can make **many** of these configuration files to adjust your
experience descriptions on a per-application basis by specifying the resume
configuration file.

### Building

This application has only been tested with `Python 3.13.2` on
`Arch Linux (v6.14.6-arch1-1)`. If you are using other platforms and experience
issues, please open a request.

Assuming you are already in the source directory of the repository and
have completed your configuration, simply build the package with pip.

```bash
python -m venv .venv
source ./.venv/bin/activate
python -m pip install -r requirements.txt  # Probably unnecessary.
python -m pip install --editable .
```

Then you are ready to run!

### Running

```bash
jobappfiller gui -f resume.toml
```

This will open the GUI for your specified configuration. If you have many
experience listings, remove the line `app.geometry("900x350")` in the
[app.py](jobappfiller/tools/app.py) in the `run_gui()` function, or adjust
it to your liking.
