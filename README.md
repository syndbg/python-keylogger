# python-keylogger
A **WORK IN PROGRESS** multiplatform Python keylogger.



## Features (not yet implemented)

* Keylogging on Linux,
* Keylogging on OSX,
* Keylogging on Windows,

* Saving logs to files,
* Saving logs and sending to email,
* Separating logs per application,
* Generating HTML logs,
* Generating PDF logs


## Installation


You can install directly from pip (stable and recommended)

```
pip install python-keylogger
```


Or you can install from git repo (unstable)
```
pip install git+https://github.com/syndbg/python-keylogger.git
```


## Usage (not final yet)


To start the keylogger and let it auto-detect your platform, write:

```
pykeylogger
```

**Note:** auto-detecting isn't that reliable (actually it's not implemented yet)


Supported platforms are: *mac*, *linux* and *windows*.

To start it for a specific platform, ex. windows use:

```
pykeylogger --platform='windows'
```


To log to a specific relative path file:

```
pykeylogger --platform='windows' --output='filename.txt' --path='relative' # path is optional since by default it's relative

# OR
pykeylogger --platform='windows' > filename.txt
```


To log to a specific absolute path file:

```
pykeylogger --platform='windows' --output='/tmp/filename.txt' --path='absolute'
```


To send your logs to an email:

```
pykeylogger --platform='mac' --output='filename' --send-to='email@place.com'
```




