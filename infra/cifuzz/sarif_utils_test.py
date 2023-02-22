# Copyright 2021 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Tests for sarif_utils."""
import os
import unittest

from clusterfuzz import stacktraces

import sarif_utils

TEST_DATA_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                              'test_data')


class GetSarifDataTest(unittest.TestCase):
  def test_get_sarif_data(self):
    with open(os.path.join(TEST_DATA_PATH, 'example_crash_fuzzer_output.txt')) as fp:
      fuzzer_output = fp.read()

    stack_parser = stacktraces.StackParser(fuzz_target='blah',
                                           symbolized=True,
                                           detect_ooms_and_hangs=True,
                                           include_ubsan=True)
    crash_info = stack_parser.parse(fuzzer_output)
    data = sarif_utils.get_sarif_data(crash_info)
    with open('/tmp/k.sarif', 'w') as fp:
      import json
      fp.write(json.dumps(data))
      # import pdb; pdb.set_trace()


class GetSarifDataTest(unittest.TestCase):
  def test_write_stacktrace_to_sarif(self):
    d=open('/tmp/stack').read()
    import pdb; pdb.set_trace()
    sarif_utils.get_sarif_data(d, '/do_stuff_fuzzer')
    pass
