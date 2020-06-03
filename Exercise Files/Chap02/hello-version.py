#!/usr/bin/env python3 # This is a shebang line. This is primarily used for UNIX based systems.
# Copyright 2009-2017 BHG http://bw.org/

import platform  # the platform module is used to display the version of python you are using.
import hello_main
hello_main.message()
print('This is python version {}'.format(platform.python_version()))
