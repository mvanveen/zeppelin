zeppelin
========

An App Engine command-line tool for Humans.

-----

## Introduction

From environment setup, to deployment and testing/debugging, `zeppelin` is a tool designed to make the
whole lifecycle of App Engine development more friendly.

We've packed `zeppelin` with hydrogen.  This tool brings App Engine package management in-line with 
the rest of the Python community's best practices by providing compatibility with `pip`'s 
`requirements.txt` depdendancy declaration format.

Excited?  That's just the tip of the iceberg.

![](http://24.media.tumblr.com/tumblr_m6yvhgBLnG1qk8zxso1_250.gif)

## Examples

### Deployment

`zeppelin` makes deployments a breeze.  It automatically installs your `requirements.txt` 
dependencies, and will warn you of non-Pure Python libraries.

### Features

- `requirements.txt` dependency management compatibility
- `oauth2` login by default

### Examples

```bash
$ zeppelin deploy .
```

### Shell

```bash
$ zeppelin shell
```

`zeppelin`'s shell is a full IPython runtime with batteries included.  It connects to any
locally running `dev_appserver.py` instance by default, and can alternatively connect
to remote instances.


### Tests

```bash
$ zeppelin test .
````
