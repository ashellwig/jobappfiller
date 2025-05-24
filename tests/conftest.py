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

import tomlkit

import pytest

RESUME_CONFIG_STR: str = """
[[default]]

[[default.experience]]
name = "TAKKION (TP&L Management Solutions)"
location = "Broomfield, CO"
startdate = "09/01/2023"
enddate = "03/01/2025"
jobtitle = "IT Cloud Developer"
description = \"\"\"\
    Migrate C#/.NET and Python Applications to the GCP/Azure \
    cloud environment. Implement automated account provisioning on Microsoft \
    Azure Entra ID through Paylocity's API with serverless \
    functions and webhooks.\
    \"\"\"

[[default.experience]]
name = "American Express"
location = "Phoenix, AZ"
startdate = "07/01/2022"
enddate = "09/01/2023"
jobtitle = "Python & SQL Developer"
description = \"\"\"\
    Migrate massive dataset from Teradata to Hive and ensure 1:1 mapping \
    of rules and regulatory reports through TSQL to Hive SQL. Utilize GCP, \
    AWS, JFrog, and Jira for CI/CD. Written a Python package to pull HiveQL \
    Query results and format them using a personally written Python package \
    for CornerStone to convert the data into XML format for reporting \
    requirements as requested by FR, MX, IT, and NL. Utilize Azure cloud \
    functions and Spring Boot for microservices. ETL pipelines. SQLAlchemy \
    library for interaction with Python and C#/.NET.\
    \"\"\"
"""


@pytest.fixture(scope="session")
def conf_file(tmp_path_factory):
    config_file_content = tomlkit.loads(RESUME_CONFIG_STR)
    fn = tmp_path_factory.mktemp("data") / "resume.toml"
    with open(fn, "w", encoding="utf-8") as fp:
        tomlkit.dump(config_file_content, fp)

    return fn
