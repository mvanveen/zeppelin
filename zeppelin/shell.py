import argparse

from google.appengine.ext.remote_api import remote_api_stub
from google.appengine.tools.remote_api_shell import DEFAULT_PATH, auth_func

from IPython.frontend.terminal.embed import InteractiveShellEmbed
from IPython.frontend.terminal.ipapp import load_default_config

def config_ipython_env(appid=None, pdb=False):
    """Configure a python shell with which to connect"""

    config = load_default_config()
    config.InteractiveShell.confirm_exit = False
    config.PromptManager.in_template = "%s> " % (appid or ":memory:")
    config.PromptManager.in2_template = "... "
    config.PromptManager.out_template = "\n"
    config.PromptManager.justify = True
    config.IPCompleter.merge_completions = False

    if pdb:
        config.InteractiveShell.pdb = True

    shell = InteractiveShellEmbed(config=config)

    return shell


def repl(appid, _file_name=None, _pdb=False):

    from google.appengine.api import datastore
    from google.appengine.api import memcache
    from google.appengine.api import urlfetch
    from google.appengine.api import users
    from google.appengine.ext import db
    from google.appengine.ext import search

    if not _file_name:
        config_ipython_env(appid=appid, pdb=_pdb)(local_ns=locals())
    else:
        config_ipython_env(appid=appid, pdb=_pdb).safe_execfile(_file_name, locals())


def config_args(parser):
    parser.add_argument('application_id',
                        nargs='?',
                        help="""The appid to connect to, 'local' to connect to a locally
                             running appserver instance, or 'memory' for a shell connected to
                             an in-memory database""")
    parser.add_argument('filename',
                        nargs='?',
                        help="Filename of a python script to run within to the shell")
    parser.add_argument('--pdb', action='store_true')


def run(application_id="local", filename=None, pdb=None):
    """Remote api shell mixed with ipython"""

    if application_id == "memory":
        application_id = None

    path = DEFAULT_PATH
    server_name = "%s.appspot.com" % application_id

    if application_id and not '~' in application_id:
        if application_id not in ['local', 'memory']:
            application_id = "s~" + application_id

    if application_id is "local":
        api_server_port = 52998

        remote_api_stub.ConfigureRemoteApi(
            application_id,
            path,
            lambda: ('', ''),
            servername='localhost:%d' % api_server_port, use_remote_datastore=False)
        remote_api_stub.MaybeInvokeAuthentication()

    elif application_id:
        remote_api_stub.ConfigureRemoteApi(
            application_id, path, auth_func, servername=server_name, save_cookies=True, secure=True)
        remote_api_stub.MaybeInvokeAuthentication()

    elif not application_id:
        pass # do nothing special for in-memory data store manipulation

    repl(application_id, _file_name=filename, _pdb=pdb)


def main(*args):
    parser = argparse.ArgumentParser(description="Open a remote interactive shell")
    config_args(parser)
    args = parser.parse_args(args)
    run(args.application_id, args.filename, args.pdb)
