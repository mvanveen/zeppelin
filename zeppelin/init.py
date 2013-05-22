"""init: initialize app engine environment
"""
import os
import subprocess
import sys

template = lambda gae_path: """%s
import dev_appserver; dev_appserver.fix_sys_path()
""" % (gae_path, )

def appengine_path():
  path = '/usr/local/google_appengine'
  if os.path.exists(path):
    return path

  out = subprocess.check_output(['which', 'dev_appserver.py']).rstrip()

  if 'not found' in out:
    return

  return os.path.abspath(os.path.join(out, '../'))

#TODO: dry-run option

def main(*args):
  path = appengine_path()

  if path:
    venv_path = os.environ.get('PATH').split(':')[0]
    venv_path = os.path.abspath(os.path.join(venv_path, '../lib/python2.7/site-packages'))

    pth_file_path = os.path.join(venv_path, 'gae.pth')

    if os.path.exists(pth_file_path):
      print 'Error: file already exists!'
      sys.exit(1)

    print 'writing pth file...',
    with open(pth_file_path, 'w') as pth_file:
      pth_file.write(template(path))
    print 'ok.'

    # TODO: better logging, verbose mode

    return



  print 'Error: could not find path!'
  sys.exit(1)

