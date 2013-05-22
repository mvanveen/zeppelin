"""init: initialize app engine environment
"""
import os
import subprocess
import sys

# quick, ugly way to do templating for .pth file with nice whitespace
template = lambda gae_path: """%s
import dev_appserver; dev_appserver.fix_sys_path()
""" % (gae_path, )


def appengine_path():
  """Returns path to `google_appengine` folder.

  On some platforms (primarily OS-X perhaps?) this is found on
  `/usr/local/google_appengine`, but not always

  Returns a kludgy path by following symlink of `dev_appserver`, if
  symlink is set.  Otherwise returns None if no option is found.
  """

  # TODO: accept cmd-line arg for path too

  path = '/usr/local/google_appengine'

  # check if the google_appengine dir is in the usual spot (not always the case)
  if os.path.exists(path):
    return path

  # check to see if symlink is installed
  path = subprocess.check_output(['which', 'dev_appserver.py']).rstrip()

  if 'not found' in path.lower():
    # TODO: verbose logging explain not found
    return

  # follow symlink
  path = os.read_link(path)

  # back out a cludgy version from symlink, if available
  # TODO: emit warning about path being kludgy
  return os.path.abspath(os.path.join(out, '../'))


#TODO(mvv): dry-run option

def main(*args):
  path = appengine_path()

  if path:
    #TODO(mvv): check if in virtualenv, and handle option of no virtualenv
    #    - more generally: look for site-packages wherever it may be.
    #    - also take a commmandline-arg

    # get virtualenvpath
    venv_path = os.environ.get('PATH').split(':')[0]
    venv_path = os.path.abspath(os.path.join(venv_path, '../lib/python2.7/site-packages'))

    pth_file_path = os.path.join(venv_path, 'gae.pth')

    if os.path.exists(pth_file_path):
      print 'Error: file already exists!'
      sys.exit(1)

    print 'writing .pth file...',
    with open(pth_file_path, 'w') as pth_file:
      pth_file.write(template(path))
    print 'ok.'

    #TODO(mvv): better logging, verbose mode
    return

  print 'Error: could not find path!'
  sys.exit(1)
