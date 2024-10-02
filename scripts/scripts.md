# Scripts

One helpful thing I do on every computer I use regularly is create a `~/scripts` directory that I add to `PATH`. This way I don't have to go searching for something I don't use regularly, and I have quick access to the things I do use a lot.

To add the `scripts` directory to `PATH`, I've added the following line to the end of my `~/.bashrc` file.
```
export PATH="$PATH:~/scripts"
```

Scripts I have:
- A VPN script to access home, work, or wherever else is important to access regularly.
- The [image converter](./image_converter.py) python script converts all photos in a specified directory to a certain file type, then deletes the original images by default. (Default filetype is `.png`)