#!/bin/sh
#
# Auto-check for pep8 so I don't check in bad code
#

#FILES=$(git diff --cached --name-status | grep -v ^D | awk '$1 $2 { print $2}' | grep -e .py$)
FILES=$(git diff --cached --name-status | cut -f2- | grep -e '.py$')
if [ -n "$FILES" ]; then
    flake8 -r $FILES
fi
