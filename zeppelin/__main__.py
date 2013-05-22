from manage import Manager

manager = Manager()


@manager.command
def deploy():
  """Enter an AppeNgine Python shell"""
  return 'this is where the deploy command goes!'

@manager.command
def shell():
  """Enter an AppeNgine Python shell"""
  return 'this is where the shell command goes!'

#TODO: think about install/freeze/build CLI interface.
#      what is the best verb to pick?

manager.main()
