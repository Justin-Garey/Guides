# Symlinks

## What is a Symlink

A symlink or symbolic link is a file which points to a target file. These are normally created to link an executable to a directory in PATH or to make content available to something with limited access. The target file can be deleted without impacting the symlink. The symlink remains pointing to the same location but is now broken.

## Creating a Symlink

To create a new symlink:
```bash
ln -s /path/to/file /path/to/new/symlink
```

To create or update a symlink:
```bash
ln -sf /path/to/file /path/to/symlink
```

## Deleting a Symlink

A symlink is just another type of file so it can be removed with:
```bash
rm /path/to/symlink
```