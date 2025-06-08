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

venv_dir="${PWD}/.venv"
tgt_python="${PWD}/.venv/bin/python"

function create_env() {
    if [[ -d "${venv_dir}" ]]; then
        echo -e "\033[1;33mFound environment directory... Removing...\033[0m"
        echo -e "\033[1;31mRemoving current environment\033[0m"
        rm -rf "${venv_dir}"
        sleep 1
        if [[ ! -d "${venv_dir}" ]]; then
            echo -e "\033[1;32mSuccessfully removed previous env dir.\033[0m"
            echo -e "\033[1;31mContinuing...\033[0m"
        fi
    fi

    if [[ ! -d "${venv_dir}" ]]; then
        echo -e "\033[1;31mNo virtual env found, creating a new one.\033[0m"
        python -m venv .venv
        if [[ -d "${venv_dir}" ]]; then
            echo -e "\033[1;32mSuccessfully created env dir.\033[0m"
            echo -e "\033[1;31mContinuing...\033[0m"
        fi
    fi

    . "${PWD}/.venv/bin/activate"

    if [[ "$(which python)" != $tgt_python ]]; then
        echo -e "\033[1;33mPython path is not correct. Exiting.\033[0m"
        exit 1
    else
        echo -e "\033[1;31mPython path is correct. Continuing.\033[0m"
        break 1
    fi
}

create_env
