zeppelin
========

App Engine CLI tooling for Humans.

![](http://www.wallpowper.com/wallpaper/2012/11/16/led-zeppelin-bands-free-music.jpg)

## Introduction

From environment setup to deployment and all the way through to testing/debugging, `zeppelin` is a 
tool designed to make the whole lifecycle of App Engine development more friendly.

## Features

### Deploy With `requirements.txt` Dependency Bundling

`zeppelin` gets App Engine package management in-line with the rest of the modern Python 
community's best practices by providing compatibility with `pip`'s `requirements.txt` 
depdendancy declaration format.

During deployment it bundles your `requirements.txt`dependencies with your app directory 
and automatically warns you of non-Pure Python libraries.


Kill your `deps` directory.  Say goodbye to `sys.path` hacks! Prove to your heroku hipster
friends that you aren't missing anything and their PaaS isn't anything special.

With `zeppelin` your dependency management is on the stairway to heaven.

### Awesome `IPython` Shell.  Remote or Local.

`zeppelin`'s `shell` command provides a full IPython runtime with batteries 
included.  It connects to any locally running `dev_appserver.py` instance by default, 
and can alternatively connect to remote instances.

### Easy Breezy Unit Tests.

Your project's unit test results are just a `zeppelin test` away.  We use `nose` as our default
test runner.

### Environment Setup

`zeppelin init` sets up common preliminaries needed to get an App Engine 
environment working using `virtualenv`.

## Examples

TODO: fancy gif animations?

### Deployment

```bash
$ zeppelin deploy .
```

### Shell

```bash
$ zeppelin shell
```

### Tests

```bash
$ zeppelin test .
````
