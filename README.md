zeppelin
========

![](http://www.mentalfloss.com/sites/default/legacy/wp-content/uploads/2008/08/Led_Zeppelin_I.jpg)

A Google App Engine command-line tool for Humans.

## Examples

### Deployment

Zeppelin makes deployments a breeze.  It automatically installs your `requirements.txt` 
dependencies, and will warn you of non-Pure Python libraries.

*Deploy the current working directory:*

```bash
    $ zeppelin deploy .
```

### Shell

zeppelin's shell is a full IPython runtime with batteries included.  It connects to any
locally running `dev_appserver.py` instance by default, and can alternatively connect
to remote instances.

** Connect to local instance

```bash
    $ zeppelin shell
```

### Tests

```bash
$ zeppelin test .
````
