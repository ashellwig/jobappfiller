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

import pyperclip
import tkinter as tk
from tkinter import ttk

from jobappfiller.tools.parse_job_config import list_descriptions, list_companies, parse_resume
from jobappfiller.util.logger import setup_logger

logger = setup_logger(log_file=None)

company_list: list[str] = list_companies(
        resume_data=parse_resume(resume_config_file="resume.toml")
)

description_list: list[str] = list_descriptions(
        resume_data=parse_resume(resume_config_file="resume.toml")
)

LARGEFONT = ("Verdana", 35)


def button_click(event):
    pyperclip.copy(f"{event.widget.master.description}")
    logger.info("Copying description for: %s", event.widget.master.company_name)
    logger.info("Description = %s", event.widget.master.description)


class TkinterApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

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
        # for f in (StartPage):
        # frame = f(container, self)
        # self.frames[f] = frame
        # frame.grid(row=0, column=0, sticky="nsew")
        startpage_frame = StartPage(container, self)
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
            # self.frames.update(frame)
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(cont=0)

    def show_frame(self, cont):
        if cont is None:
            cont = self.frames.get(0)
        else:
            cont = self.frames[cont]
        frame = cont
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

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


if __name__ == "__main__":
    app = TkinterApp()
    app.mainloop()
