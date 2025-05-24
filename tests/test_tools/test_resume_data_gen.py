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

from jobappfiller.tools.resume_data_gen import ResumeDataGen


def test_company_list(conf_file):
    resume_data = ResumeDataGen(conf_file, date_format="yyyy-MM")

    assert resume_data.company_list[0] == "TAKKION (TP&L Management Solutions)"
    assert resume_data.company_list[1] == "American Express"
