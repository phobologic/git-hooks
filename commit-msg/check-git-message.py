#!/usr/bin/python

import sys

exit_code = 0
with open(sys.argv[1]) as commit_msg:
    for lineno, line in enumerate(commit_msg):
        line = line.strip()
        if lineno == 0:
            if len(line) > 50:
                exit_code = 1
                print "# E%d: First line should be less than 50 " \
                        "characters." % (lineno,)
        elif lineno == 1:
            if line:
                exit_code = 1
                print "# E%d: Second line should be empty." % (lineno,)
        else:
            if line.startswith('#'):
                # ignore comment lines
                continue
            if len(line) > 72:
                exit_code = 1
                print "# E%d: No line should be over 72 characters long." % (
                        lineno,)

sys.exit(exit_code)