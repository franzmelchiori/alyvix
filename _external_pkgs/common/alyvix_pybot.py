# Alyvix allows you to automate and monitor all types of applications
# Copyright (C) 2015 Alan Pipitone
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Developer: Alan Pipitone (Violet Atom) - http://www.violetatom.com/
# Supporter: Wuerth Phoenix - http://www.wuerth-phoenix.com/
# Official website: http://www.alyvix.com/

import os
import sys
import time
import shutil
import tempfile
import argparse
from robot import run
from datetime import datetime

save = os.dup(1), os.dup(2)

null_fds = [os.open(os.devnull, os.O_RDWR) for x in xrange(2)]

parser = argparse.ArgumentParser()
parser.add_argument("testsuite", help="the file containing the testcase(s)")
parser.add_argument("--outputdir", help="robot framework output directory") #, default=None)
parser.add_argument("--test", help="the test case to run")

#parse arguments
args = parser.parse_args()

if args.outputdir:
    output_dir = args.outputdir
else:  
    #we must always set the output folder (probably due to a Robot Framework Api bug).

    path_tree = args.testsuite.split(os.sep)
    suite_name =  path_tree[-1].split(".")[0]
    
    #save the log folder into the user temp directory
    output_dir = tempfile.gettempdir() + os.sep + "alyvix_pybot" + os.sep + suite_name
    
    if args.test:
        output_dir = output_dir + os.sep + args.test
        
    try:
        shutil.rmtree(output_dir) #delete all logs of previous run.
    except:
        pass
        
#builds a string for logging purposes
if args.testsuite and args.test:
    check_target = 'test case "%s" in test suite "%s"' % (args.test, args.testsuite)
else:
    check_target = 'test suite "%s"' % args.testsuite

#disable console output
os.dup2(null_fds[0], 1)
os.dup2(null_fds[1], 2)

if args.test:
    #run testsuite with only one testcase
    run(args.testsuite, outputdir=output_dir, test=args.test)
else:
    #run testsuite with all testcases
    run(args.testsuite, outputdir=output_dir)
    
#enable console output
os.dup2(save[0], 1)
os.dup2(save[1], 2)
os.close(null_fds[0])
os.close(null_fds[1])

output = os.getenv("alyvix_std_output")
exitcode = os.getenv("alyvix_exitcode")

#checks if test/testsuite has generated any output
if output is None and exitcode is None:
    print("UNKNOWN - %s generated no output or exit code." % check_target)
    sys.exit(3)

#exit with alyvix output/performance data and exit code
print(output)
sys.exit(int(exitcode))