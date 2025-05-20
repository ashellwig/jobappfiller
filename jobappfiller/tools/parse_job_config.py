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
"""Parses job resume configuration file."""

import tomllib

from jobappfiller.util.logger import setup_logger

logger = setup_logger(log_file=None)


def parse_resume(resume_config_file: str) -> dict:
    """Reads the resume configuration file into a dictionary.

    Args:
        resume_config_file (str): Path to configuration file as a string.

    Returns:
        dict: Dictionary containing the contents of the resume configuration.
    """
    with open(resume_config_file, "rb") as f:
        data: dict = tomllib.load(f)

    return data


def list_companies(resume_data: dict) -> list[str]:
    companies: list[str] = []
    experience_data = resume_data.get("default")[0]["experience"]
    for i in range(0, len(experience_data)):
        companies.append(experience_data[i]["name"])

    return companies


def add_one(number: int) -> int:
    """Increments the given number by one.

    Args:
        number (int): Number to increment.

    Returns:
        int: Incremented number.
    """
    logger.info("Running add_one")
    return number + 1
