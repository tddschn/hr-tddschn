# hr-tddschn

Fork of [hr.py](https://github.com/euangoddard/hr.py), with python3 support.

The good old [hr](https://github.com/LuRsT/hr) in python3.

- [hr-tddschn](#hr-tddschn)
  - [Why fork?](#why-fork)
  - [Intro](#intro)
  - [Inspiration](#inspiration)
  - [Install](#install)
  - [How to use it?](#how-to-use-it)
    - [From the command-line:](#from-the-command-line)
    - [From another python script (it could happen, right?)](#from-another-python-script-it-could-happen-right)
  - [Requirements](#requirements)
## Why fork?

Version 0.1 of the original `hr.py` 
(the current latest version of `hr` on [PyPI](https://pypi.org/project/hr/)) doesn't work with python3,

this project adds python3 support.

## Intro

Horizontal rule for your terminal - in python3!

Tired of not finding things in your terminal because there's a lot of logs and
garbage? Tired of destroying the Enter key by creating a "void zone" in your
terminal so that you can see the error that you're trying to debug?

Use the old `<hr />` tag, but in your terminal.

## Inspiration

The original version of the hr script was implement in bash (https://github.com/LuRsT/hr), and I thought, "why not have a python version?". So here we are!

## Install

```
$ pip install hr-tddschn
```

Or, if you only want to use it as a CLI app:
```
$ pipx install hr-tddschn
```

Then run it with `hr`.

## How to use it?

### From the command-line:

    $ hr
    ################################## # Till the end of your terminal window
    $

    $ hr '*'
    ********************************** # Till the end of your terminal window
    $

You can also make "beautiful" ASCII patterns

    $ hr - '#' -
    ----------------------------------
    ##################################
    ----------------------------------
    $ hr '-#-' '-' '-#-'
    -#--#--#--#--#--#--#--#--#--#--#--
    ----------------------------------
    -#--#--#--#--#--#--#--#--#--#--#--

### From another python script (it could happen, right?)

    >>> from hr_tddschn import hr
    >>> hr()
    ################################## # Till the end of your terminal window
    >>> hr('*')
    ********************************** # Till the end of your terminal window
    >>> hr('-', '#', '-')
    ----------------------------------
    ##################################
    ----------------------------------
    >>> hr('-#-', '-', '-#-')
    -#--#--#--#--#--#--#--#--#--#--#--
    ----------------------------------
    -#--#--#--#--#--#--#--#--#--#--#--

## Requirements

The only requirement is python2.7+ or python3 (tested in python 3.10)
