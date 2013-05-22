zeppelin
========

An App Engine command-line tool for Humans.

![](http://www.wallpowper.com/wallpaper/2012/11/16/led-zeppelin-bands-free-music.jpg)

## Introduction

From environment setup to deployment and all the way through to testing/debugging, `zeppelin` is a 
tool designed to make the whole lifecycle of App Engine development more friendly.

## Features

### Deploy With `requirements.txt` Dependency Bundling

`zeppelin` brings App Engine package management in-line with 
the rest of the Python community's best practices by providing compatibility with `pip`'s 
`requirements.txt` depdendancy declaration format.  During deployment it bundles your `requirements.txt` 
dependencies with your app directory and automatically you of non-Pure Python libraries.

### Awesome Shell

For example, `zeppelin`'s `shell` command provides a full IPython runtime with batteries 
included.  It connects to any locally running `dev_appserver.py` instance by default, 
and can alternatively connect to remote instances.

### ...And A Whole More!

Excited?  That's just the tip of the iceberg.

## Examples

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
