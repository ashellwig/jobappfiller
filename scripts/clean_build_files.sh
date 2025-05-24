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

function _pycaches {
    find . -maxdepth 3 -name "*__pycache__*"
    echo "./build"
    echo "./dist"
    echo "./jobappfiller.egg-info"
    echo "./.pytest_cache"
}

typeset -a lines
_pycaches | IFS=$'\n' read -r -d '' -A lines

new_arr=("${lines[@]:0:$#lines-1}")

arr_sizetwo=${#new_arr[@]}

echo "arr_sizetwo: $arr_sizetwo"

for item in "${new_arr[@]}"; do
    if [[ -e $item ]]; then
        echo -e "\033[1;31mRemoving $item\033[0m"
        rm -rf $item
        if [[ ! -e $item ]]; then
            echo -e "\033[1;32m$item Removed.\033[0m"
        fi
    fi
done
