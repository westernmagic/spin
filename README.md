# spin

a small utility to assist in setting usage modes of laptop-tablet devices

## about this fork

This is a fork of wdbm/spin. I'm currently working in the yoga12-2nd-gen branch, to get everything working properly with my Thinkpad Yoga 12 2nd Gen machine under Ubuntu 15.10. It's currently not fully done, but getting there. There are some major changes, including:

- Improved the handling of the accelerometer using vector math, so it detects the correct orientation.
- Moved all changes to the screen rotation to the main process, and use messaging from the subprocesses to tell the main process what to do.
- Added support for the rotation lock key on the side of the ThinkPad Yoga 12.
- It now waits for the touchscreen to be ready, before attempting to rotate it.
- Added packaging of the tool into Debian package (.deb) file.

Known issues:

- I've yet to get the display position detector to differentiate when going from tent mode, to tablet or laptop mode, so am currently unable to use it to automatically switch between tablet and laptop modes. It's not ideal, and I've posted about this upstream to the systemd folks, so hopefully we'll have this fully automated some day.
- There is some issue with Wacom calibration getting worse each time you calibrate. I've included some code in spin.py that resets the calibration each time the screen is rotated, but this is not ideal. I need to figure out exactly what is going on here. It may be related to the screen reporting the wrong PPI in Gimp (96x96 on Linux and 144x144 on Windows, correct I believe is 177x177), so if the calibration tool may be getting the incorrect screen size or ppi.

Other than that, it's almost done.

## prerequisites

```Bash
sudo apt-get -y install python-qt4
```

## Building and installation

This tool is set up to build a Debian package for easy installation. Simply run.

```Bash
make install
```

You'll find the .deb file in the build folder, and can install it like you would any .deb package.


## quick start

By default this utiltiy does nothing. To start it run:

```Bash
spin.py --daemon
```

This will run it in the background. It will activate palm rejection, when the pen is in use, and wait for other commands. You can add this to your startup applications, if you want it to run every time you log in.

There are two other commands you can send it.

```Bash
spin.py --mode
```

This tells it to toggle between Tablet and Laptop mode. The tool always starts in laptop mode. Note that the tool cannot currently detect when you flip the screen back.

When in Tablet mode, it will use the accelorometer to adjust the screens orientation. You can lock this, using the rotation lock key on the side of the laptop, or using:

```Bash
spin.py --lock
```

This toggles the display rotation lock when in Tablet mode. You can also use the rotate lock key on the side of the computer. Note that this key also transmits the Super-o keys, which in turn opens up the Unity launcher. A workaround for this, is to assign Super-o to an empty keyboard shortcut in the System Preferences.

In addition there are two applications launchers, which can be found in /usr/share/applications/Yoga Spin - etc, that can run these commands. You can drag these to the Unity launcher, to quickly toggle between modes.

For debugging, you can run spin.py with different log levels, for more info, see:

```Bash
spin.py --help
```


## compatibility

This utility has been tested on the following operating systems:

- Ubuntu 15.10

This utility has been tested on the following computer models:

- ThinkPad S120 Yoga

It should work on the ThinkPad S1 Yoga, but it's not been tested for this branch.

There is evidence that it does not run with full functionality on the ThinkPad Yoga 14.

## future

The next step is to add some nice icons to it, and test it a lot more.
