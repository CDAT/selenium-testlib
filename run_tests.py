import os
import sys
import cdat_info

test_suite_name = 'selenium-testlib'

workdir = os.getcwd()
runner = cdat_info.TestRunnerBase(test_suite_name, get_sample_data=False)
ret_code = runner.run(workdir)

sys.exit(ret_code)

