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

import click
import json
from rich import print_json

from jobappfiller.tools.parse_job_config import add_one, parse_resume, list_companies
from jobappfiller.tools.gui import run_gui


@click.command()
@click.option('-f', '--file', type=str)
def cli_print_resume_json(file: str):
    parsed_dictionary: dict = parse_resume(resume_config_file=file)
    parsed_dictionary_json: str = json.dumps(parsed_dictionary)
    print_json(parsed_dictionary_json)


@click.command()
@click.option('-f', '--file', type=str)
def cli_print_companies(file: str):
    parsed_dictionary: dict = parse_resume(resume_config_file=file)
    list_of_companies: list[str] = list_companies(parsed_dictionary)

    for company in list_of_companies:
        print(company)


@click.command()
@click.option('-f', '--file', type=str, help='Resume config file.')
def cli_start_gui(file: str):
    run_gui(resume_data=file)


@click.command()
@click.option('-n', '--num', type=int)
def cli_add_one(num: int):
    click.echo(str(add_one(number=num)))
