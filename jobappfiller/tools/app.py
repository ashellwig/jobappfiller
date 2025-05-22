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

import re
import tkinter as tk
import tkinter.font as tk_font
from tkinter import ttk

import pyperclip

from jobappfiller.tools.parse_job_config import (
        list_companies,
        list_locations,
        list_startdates,
        list_enddates,
        list_jobtitles,
        list_descriptions,
        parse_resume
)
from jobappfiller.util.logger import setup_logger

LARGEFONT = ("calibri", 36, tk_font.BOLD)
SMALLFONT = ("calibri", 14, tk_font.NORMAL)

logger = setup_logger(log_file=None)


def generate_company_list(resume_config_file: str) -> list[str]:
    """Retrieve the list of companies from the resume configuration file.

    Args:
        resume_config_file (str): Path to resume configuration file.

    Returns:
        list[str]: List of companies names under experience.
    """
    company_list: list[str] = list_companies(
            resume_data=parse_resume(resume_config_file=resume_config_file)
    )

    return company_list


def generate_location_list(resume_config_file: str) -> list[str]:
    """Retrieve the list of company locations from the
    resume configuration file.

    Args:
        resume_config_file (str): Path to resume configuration file.

    Returns:
        list[str]: List of company locations.
    """
    location_list: list[str] = list_locations(
            resume_data=parse_resume(resume_config_file=resume_config_file)
    )

    return location_list


def generate_startdate_list(resume_config_file: str,
                            date_format: str | None) -> list[str]:
    """Retrieve the list of company start dates from the
    resume configuration file.


    Args:
        resume_config_file (str): Path to resume configuration file.
        date_format (str | None, optional): Date format. Must be "yyyy/MM",
            "MM/yyyy", "yyyy/MM/dd", or "MM/dd/yyyy". Defaults to "MM/dd/yyyy".

    Returns:
        list[str]: List of company start dates.
    """
    startdate_list: list[str] = list_startdates(
            resume_data=parse_resume(resume_config_file=resume_config_file)
    )
    modified_startdate_list: list[str] = []

    if date_format == "yyyy/MM":
        for i in range(0, len(startdate_list)):
            modified_startdate_list.append(
                    f"{startdate_list[i][-4:]}/{startdate_list[i][:2]}"
            )
    elif date_format == "MM/yyyy":
        for i in range(0, len(startdate_list)):
            modified_startdate_list.append(
                    f"{startdate_list[i][:2]}/{startdate_list[i][-4:]}"
            )
    elif date_format == "yyyy/MM/dd":
        for i in range(0, len(startdate_list)):
            day = re.search(r"\/(.*?)\/", startdate_list[i]).group(1)
            modified_startdate_list.append(
                    f"{startdate_list[i][-4:]}/{startdate_list[i][:2]}/{day}"
            )
    else:
        for i in range(0, len(startdate_list)):
            modified_startdate_list.append(startdate_list[i])

    return modified_startdate_list


def generate_enddate_list(resume_config_file: str,
                            date_format: str | None) -> list[str]:
    """Retrieve the list of company end dates from the
    resume configuration file.


    Args:
        resume_config_file (str): Path to resume configuration file.
        date_format (str | None, optional): Date format. Must be "yyyy/MM",
            "MM/yyyy", "yyyy/MM/dd", or "MM/dd/yyyy". Defaults to "MM/dd/yyyy".

    Returns:
        list[str]: List of company end dates.
    """
    enddate_list: list[str] = list_enddates(
            resume_data=parse_resume(resume_config_file=resume_config_file)
    )
    modified_enddate_list: list[str] = []

    if date_format == "yyyy/MM":
        for i in range(0, len(enddate_list)):
            modified_enddate_list.append(
                    f"{enddate_list[i][-4:]}/{enddate_list[i][:2]}"
            )
    elif date_format == "MM/yyyy":
        for i in range(0, len(enddate_list)):
            modified_enddate_list.append(
                    f"{enddate_list[i][:2]}/{enddate_list[i][-4:]}"
            )
    elif date_format == "yyyy/MM/dd":
        for i in range(0, len(enddate_list)):
            day = re.search(r"\/(.*?)\/", enddate_list[i]).group(1)
            modified_enddate_list.append(
                    f"{enddate_list[i][-4:]}/{enddate_list[i][:2]}/{day}"
            )
    else:
        for i in range(0, len(enddate_list)):
            modified_enddate_list.append(enddate_list[i])

    return modified_enddate_list


def generate_jobtitle_list(resume_config_file: str) -> list[str]:
    """Retrieve the list of job titles from the resume configuration file.

    Args:
        resume_config_file (str): Path to resume configuration file.

    Returns:
        list[str]: List of company job titles.
    """
    jobtitle_list: list[str] = list_jobtitles(
            resume_data=parse_resume(resume_config_file=resume_config_file)
    )

    return jobtitle_list


def generate_description_list(resume_config_file: str) -> list[str]:
    """Retrieve the list of company job descriptions from the
    resume configuration file.

    Args:
        resume_config_file (str): Path to resume configuration file.

    Returns:
        list[str]: List of company job descriptions.
    """
    description_list: list[str] = list_descriptions(
            resume_data=parse_resume(resume_config_file=resume_config_file)
    )

    return description_list


def button_click_company_name(event):
    """Copies the name of the company from experience to the clipboard.

    Args:
        event (tkinter.EventType.ButtonPress): Event caused by
        pressing the Company Name button.
    """
    pyperclip.copy(f"{event.widget.master.company_name}")
    logger.info(
            "Copying Company Name for: %s",
            event.widget.master.company_name
    )
    logger.info("location = %s", event.widget.master.company_name)


def button_click_location(event):
    """Copies the location of the experience to the clipboard.

    Args:
        event (tkinter.EventType.ButtonPress): Event caused by
        pressing the Location button.
    """
    pyperclip.copy(f"{event.widget.master.location}")
    logger.info("Copying location for: %s", event.widget.master.company_name)
    logger.info("location = %s", event.widget.master.location)


def button_click_startdate(event):
    """Copies the startdate of the experience to the clipboard.

    Args:
        event (tkinter.EventType.ButtonPress): Event caused by
        pressing the Start Date button.
    """
    pyperclip.copy(f"{event.widget.master.startdate}")
    logger.info("Copying description for: %s", event.widget.master.company_name)
    logger.info("startdate = %s", event.widget.master.startdate)


def button_click_enddate(event):
    """Copies the enddate of the experience to the clipboard.

    Args:
        event (tkinter.EventType.ButtonPress): Event caused by
        pressing the End Date button.
    """
    pyperclip.copy(f"{event.widget.master.enddate}")
    logger.info("Copying description for: %s", event.widget.master.company_name)
    logger.info("enddate = %s", event.widget.master.enddate)


def button_click_jobtitle(event):
    """Copies the jobtitle of the experience to the clipboard.

    Args:
        event (tkinter.EventType.ButtonPress): Event caused by
        pressing the Job Title button.
    """
    pyperclip.copy(f"{event.widget.master.jobtitle}")
    logger.info("Copying description for: %s", event.widget.master.company_name)
    logger.info("jobtitle = %s", event.widget.master.jobtitle)


def button_click_description(event):
    """Copies the description of the experience to the clipboard.

    Args:
        event (tkinter.EventType.ButtonPress): Event caused by
        pressing the Description button.
    """
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
            location_list: list[str] | None,
            startdate_list: list[str] | None,
            enddate_list: list[str] | None,
            jobtitle_list: list[str] | None,
            description_list: list[str] | None,
            date_format: str | None,
            *args,
            **kwargs
    ):
        tk.Tk.__init__(self, *args, **kwargs)

        if company_list is None:
            company_list = generate_company_list(
                    resume_config_file="resume.toml"
            )

        if location_list is None:
            location_list = generate_location_list(
                    resume_config_file="resume.toml"
            )

        if startdate_list is None:
            startdate_list = generate_startdate_list(
                    resume_config_file="resume.toml",
                    date_format=date_format
            )

        if enddate_list is None:
            enddate_list = generate_enddate_list(
                    resume_config_file="resume.toml",
                    date_format=date_format
            )

        if jobtitle_list is None:
            jobtitle_list = generate_jobtitle_list(
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
                            location=location_list[i],
                            startdate=startdate_list[i],
                            enddate=enddate_list[i],
                            jobtitle=jobtitle_list[i],
                            description=description_list[i]
                    )
            )

        startpage_frame = StartPage(container, self, company_list=company_list)
        self.frames[0] = startpage_frame
        startpage_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        startpage_frame.grid_rowconfigure(0, weight=1)
        startpage_frame.grid_columnconfigure(0, weight=1)
        startpage_frame.grid_columnconfigure(1, weight=1)
        startpage_frame.grid_columnconfigure(2, weight=1)

        for i in range(0, len(company_list)):
            frame = CompanyPage(
                    container,
                    self,
                    company_list[i],
                    location=location_list[i],
                    startdate=startdate_list[i],
                    enddate=enddate_list[i],
                    jobtitle=jobtitle_list[i],
                    description=description_list[i]
            )
            self.frames[i + 1] = frame
            frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
            frame.grid_rowconfigure(0, weight=1)
            frame.grid_columnconfigure(0, weight=1)
            frame.grid_columnconfigure(1, weight=1)
            frame.grid_columnconfigure(2, weight=1)

        self.show_frame(cont=0)

    def show_frame(self, cont):
        """Shows the frame of the specified job.

        Args:
            cont (int): Index of the frame under `self.frames` to display.
        """
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

        # Frame Label (App Title)
        label = ttk.Label(self, text="Job Application Filler", font=LARGEFONT)
        label.grid(row=0, column=1, padx=5, pady=5)

        # Separator
        separator = ttk.Separator(self, orient="horizontal")
        separator.grid(
                row=1,
                column=0,
                columnspan=3,
                sticky="ew",
                padx=5,
                pady=0
        )
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)
        self.grid_rowconfigure(4, weight=1)
        self.grid_rowconfigure(5, weight=1)
        self.grid_rowconfigure(6, weight=1)
        self.grid_rowconfigure(7, weight=1)
        self.grid_rowconfigure(8, weight=1)

        # Company Navigation Buttons
        for i in range(0, len(company_list)):
            button = ttk.Button(
                    self,
                    text=f"{company_list[i]}",
                    width=60,
                    style=ttk.Style().configure(".",
                                                font=SMALLFONT),
                    command=lambda i=i + 1: controller.show_frame(cont=i)
            )
            button.grid(row=(i + 1) + 1, column=1, padx=5, pady=5)


class CompanyPage(tk.Frame):
    """Page containing the information for each listed experience and a button
    to copy each field to the clipboard.

    Args:
        tk (tkinter.Frame): Widget for a `tkinter.Frame`.
    """

    def __init__(
            self,
            parent,
            controller,
            company_name,
            location,
            startdate,
            enddate,
            jobtitle,
            description
    ):
        tk.Frame.__init__(self, parent)
        self.company_name = company_name
        self.location = location
        self.startdate = startdate
        self.enddate = enddate
        self.jobtitle = jobtitle
        self.description = description

        # Company Name Label
        label = ttk.Label(self, text=self.company_name, font=LARGEFONT)
        label.grid(row=0, column=1, padx=5, pady=5)

        # Separator before the buttons
        separator = ttk.Separator(self, orient="horizontal")
        separator.grid(
                row=1,
                column=0,
                columnspan=3,
                sticky="ew",
                padx=5,
                pady=0
        )
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)
        self.grid_rowconfigure(4, weight=1)
        self.grid_rowconfigure(5, weight=1)
        self.grid_rowconfigure(6, weight=1)
        self.grid_rowconfigure(7, weight=1)
        self.grid_rowconfigure(8, weight=1)

        # Company Name Button
        company_name_button = ttk.Button(self, text="Copy Company Name")
        company_name_button.bind("<Button-1>", button_click_company_name)
        company_name_button.grid(row=2, column=1, padx=5, pady=5)

        # Location Button
        location_button = ttk.Button(self, text="Copy Location")
        location_button.bind("<Button-1>", button_click_location)
        location_button.grid(row=3, column=1, padx=5, pady=5)

        # Start Date Button
        startdate_button = ttk.Button(self, text="Copy Start Date")
        startdate_button.bind("<Button-1>", button_click_startdate)
        startdate_button.grid(row=4, column=1, padx=5, pady=5)

        # End Date Button
        enddate_button = ttk.Button(self, text="Copy End Date")
        enddate_button.bind("<Button-1>", button_click_enddate)
        enddate_button.grid(row=5, column=1, padx=5, pady=5)

        # Job Title Button
        jobtitle_button = ttk.Button(self, text="Copy Job Title")
        jobtitle_button.bind("<Button-1>", button_click_jobtitle)
        jobtitle_button.grid(row=6, column=1, padx=5, pady=5)

        # Description Button
        description_button = ttk.Button(self, text="Copy Description")
        description_button.bind("<Button-1>", button_click_description)
        description_button.grid(row=7, column=1, padx=5, pady=5)

        # Return to Start Page Button
        startpage_button = ttk.Button(
                self,
                text="Start Page",
                command=lambda: controller.show_frame(cont=0)
        )
        startpage_button.grid(row=8, column=1, padx=5, pady=5)


def run_gui(
        company_list: str = "resume.toml",
        location_list: str = "resume.toml",
        startdate_list: str = "resume.toml",
        enddate_list: str = "resume.toml",
        jobtitle_list: str = "resume.toml",
        description_list: str = "resume.toml",
        date_format: str | None = None,
):
    """_summary_

    Args:
        company_list (str, optional): List of companies. Defaults
            to "resume.toml".
        location_list (str, optional): List of company locations.
            Defaults to "resume.toml".
        startdate_list (str, optional): List of start dates.
            Defaults to "resume.toml".
        enddate_list (str, optional): List of end dates.
            Defaults to "resume.toml".
        jobtitle_list (str, optional): List of job titles.
            Defaults to "resume.toml".
        description_list (str, optional): List of company job descriptions.
            Defaults to "resume.toml".
        date_format (str | None, optional): Date format. Must be "yyyy/MM",
            "MM/yyyy", "yyyy/MM/dd", or "MM/dd/yyyy". Defaults to "MM/dd/yyyy".
    """
    app = TkinterApp(
            company_list=generate_company_list(company_list),
            location_list=generate_location_list(location_list),
            startdate_list=generate_startdate_list(
                    startdate_list,
                    date_format=date_format
            ),
            enddate_list=generate_enddate_list(
                    enddate_list,
                    date_format=date_format
            ),
            jobtitle_list=generate_jobtitle_list(jobtitle_list),
            description_list=generate_description_list(description_list),
            date_format=date_format
    )

    app.geometry("900x450")

    app.mainloop()


if __name__ == "__main__":
    run_gui()
