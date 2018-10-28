# Workaround for Python3 compat
import sys
if sys.version_info > (3,):
  long = int
  integer_types = (int,)
else:
  integer_types = (int, long)
