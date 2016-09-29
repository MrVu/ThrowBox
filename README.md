# ThrowBox
A simple file sharing platform, partly inspired by dropbox.

##Screenshots
* Index
![Index](http://i.imgur.com/4E8Y6Ab.jpg)

* Browsing interface
![Browsin interface](http://i.imgur.com/eio9v5P.jpg)

* Example folder with files inside
![Example folder with files inside](http://i.imgur.com/b4UXXRs.jpg)

* Example empty folder
![Example empty folder](http://i.imgur.com/ZYWkiFn.jpg)

* Example 404 message
![Example 404 message](http://i.imgur.com/Jc4IeDs.jpg)

##Install

ThrowBox has only **one dependency** that is not a part of the default library - **Flask**.

Before running ThrowBox, run script `install.py`.
For now, that script only creates a *folder* named `REPO` in the root of the project directory.

You can **configure ThrowBox to your liking** with file `throwbox.conf`.

For testing purposes, you can **run**: 
```
python3 app.py
```
which will host the project on localhost, **port 8080**.

However, prefered hosting method is via gunicorn, using nginx as a proxy.
You can check my personal nginx and systemd config files in miscellaneous folder.

##Use
**Just throw all the files and folders in the `REPO` folder.**
Also, if you want to have a private files downloadable only via link, name the file so it beggins with a dot(`.`).

For example;
Folder with files `file1 .file2 file3` will only list file1 and file2. However, you can download .file3 via a direct link (.file3 is, so to speak, *hidden*).
