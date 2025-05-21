# Copyright (C) 2025 Ash Hellwig <ahellwig.dev@gmail.com>
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
"""Runs a GUI application to copy the data from each experience entry in
the resume configuration to the clipboard in an easy-to-use menu.
"""

import pyperclip
import tkinter as tk
from tkinter import ttk

from jobappfiller.tools.parse_job_config import list_descriptions, list_companies, parse_resume
from jobappfiller.util.logger import setup_logger

logger = setup_logger(log_file=None)


def generate_company_list(resume_config_file: str) -> list[str]:
    company_list: list[str] = list_companies(
            resume_data=parse_resume(resume_config_file=resume_config_file)
    )

    return company_list


def generate_description_list(resume_config_file: str) -> list[str]:
    description_list: list[str] = list_descriptions(
            resume_data=parse_resume(resume_config_file=resume_config_file)
    )
    return description_list


LARGEFONT = ("Verdana", 35)


def button_click(event):
    pyperclip.copy(f"{event.widget.master.description}")
    logger.info("Copying description for: %s", event.widget.master.company_name)
    logger.info("Description = %s", event.widget.master.description)


class TkinterApp(tk.Tk):
    """Top-level app that serves the purpose of switching frames between each
    company selected.

    Args:
        tk (tkinter.Tk): The main Tkinter window.
    """

    def __init__(
            self,
            company_list: list[str] | None,
            description_list: list[str] | None,
            *args,
            **kwargs
    ):
        tk.Tk.__init__(self, *args, **kwargs)

        if company_list is None:
            company_list = generate_company_list(
                    resume_config_file="resume.toml"
            )

        if description_list is None:
            description_list = generate_description_list(
                    resume_config_file="resume.toml"
            )

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        self.company_pages = []

        for i in range(0, len(company_list)):
            self.company_pages.append(
                    CompanyPage(
                            container,
                            self,
                            company_name=company_list[i],
                            description=description_list[i]
                    )
            )

        startpage_frame = StartPage(container, self, company_list=company_list)
        self.frames[0] = startpage_frame
        startpage_frame.grid(row=0, column=0, sticky="nsew")

        for i in range(0, len(company_list)):
            frame = CompanyPage(
                    container,
                    self,
                    company_list[i],
                    description=description_list[i]
            )
            self.frames[i + 1] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(cont=0)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):
    """The homepage of the GUI application, listing all the companies found
    in the user's provided configuration file.

    Args:
        tk (tkinter.Frame): Widget for a `tkinter.Frame`.
    """

    def __init__(self, parent, controller, company_list: list[str] | None):
        tk.Frame.__init__(self, parent)

        if company_list is None:
            company_list = generate_company_list(
                    resume_config_file="resume.toml"
            )

        label = ttk.Label(self, text="Job Application Filler", font=LARGEFONT)
        label.grid(row=0, column=4, padx=10, pady=10)

        for i in range(0, len(company_list)):
            button = ttk.Button(
                    self,
                    text=f"{company_list[i]}",
                    width=60,
                    command=lambda i=i + 1: controller.show_frame(cont=i)
            )
            button.grid(row=i + 1, column=1, padx=10, pady=10)


class CompanyPage(tk.Frame):
    """Page containing the information for each listed experience and a button
    to copy each field to the clipboard.

    Args:
        tk (tkinter.Frame): Widget for a `tkinter.Frame`.
    """

    def __init__(self, parent, controller, company_name, description):
        tk.Frame.__init__(self, parent)
        self.company_name = company_name
        self.description = description

        label = ttk.Label(self, text=self.company_name, font=LARGEFONT)
        label.grid(row=0, column=4, padx=10, pady=10)

        description_button = ttk.Button(self, text="Copy Description")
        description_button.bind("<Button-1>", button_click)
        description_button.grid(row=1, column=1, padx=10, pady=10)

        startpage_button = ttk.Button(
                self,
                text="Start Page",
                command=lambda: controller.show_frame(cont=0)
        )
        startpage_button.grid(row=2, column=1, padx=10, pady=10)


def run_gui(
        company_list: str = "resume.toml",
        description_list: str = "resume.toml"
):
    app = TkinterApp(
            company_list=generate_company_list(company_list),
            description_list=generate_description_list(description_list)
    )
    app.mainloop()


if __name__ == "__main__":
    run_gui()
