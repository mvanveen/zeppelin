# 1. make a temporary directory
# 2. cp app directory over
# 3. pip install --target -r requirements.txt build/
# 4. check for intersection. (dry run)
# 5.  if no intersection, move over to top-level
# 5.1   optionally run tests
# 6.  push up to app engine

from google.appengine.tools.appcfg import AppCfgApp, StatusUpdate

def main(*args):
  try:
    result = AppCfgApp(['appcfg.py', 'update'] + list(args)).Run()
    if result:
      sys.exit(result)
  except KeyboardInterrupt:
    StatusUpdate('Interrupted.')
    sys.exit(1)
