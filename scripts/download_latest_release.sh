#!/usr/bin/env zsh

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

latest_release="releases/latest/download/jobappfiller-cli"

if type "wget" >/dev/null; then
    wget "https://github.com/ashellwig/jobappfiller/${latest_release}"
    chmod +x ./jobappfiller-cli
    echo -e "\033[1,32mSuccessfully downloaded ${latest_release}\033[0m"
elif type "curl" >/dev/null; then
    echo -e "\033[1,33mUsing curl to download ${latest_release}\033[0m"
    curl \
        -L "https://github.com/ashellwig/jobappfiller/${latest_release}" \
        >jobappfiller-cli
    chmod +x ./jobappfiller
    echo -e "\033[1,32mSuccessfully downloaded ${latest_release}\033[0m"
else
    echo -e "\033[1,31mPlease install either wget or curl.\033[0m"
    exit 1
fi
