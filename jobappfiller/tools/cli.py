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

from jobappfiller.tools.parse_job_config import add_one, parse_resume


class DatetimeEncoder(json.JSONEncoder):

    def default(self, o):
        try:
            return super().default(o)
        except TypeError:
            return str(o)


@click.command()
@click.option('-f', '--file', type=str)
def cli_parse_resume(file: str):
    parsed_dictionary: dict = parse_resume(resume_config_file=file)
    parsed_dictionary_json: str = json.dumps(
            parsed_dictionary,
            cls=DatetimeEncoder
    )
    print_json(parsed_dictionary_json)


@click.command()
@click.option('-n', '--num', type=int)
def cli_add_one(num: int):
    click.echo(str(add_one(number=num)))
