# Copyright (C) 2025 Ash Hellwig <ahellwig.dev@gmail.com> (https://ashhellwig.netlify.app)
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import pyperclip

import tkinter as tk

from jobappfiller.tools.parse_job_config import list_descriptions, list_companies, parse_resume


def button_click(i):
    pyperclip.copy(f"{i}")
    print("Copied job description to clipboard.")


def run_gui(resume_data: str) -> None:
    company_list: list[str] = list_companies(
            resume_data=parse_resume(resume_config_file=resume_data)
    )

    description_list: list[str] = list_descriptions(
            resume_data=parse_resume(resume_config_file=resume_data)
    )

    r = tk.Tk()
    r.title("Companies")
    for i in range(0, len(company_list)):
        button = tk.Button(
                r,
                text=f"{company_list[i]}",
                width=60,
                command=lambda i=i: button_click(description_list[i])
        )
        button.pack()
    r.mainloop()
