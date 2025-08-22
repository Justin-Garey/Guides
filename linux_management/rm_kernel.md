# Remove a Kernel

## Why Remove a Kernel?

One day, you go and update Ubuntu. Then, once you restart the computer, you find broken wifi and GPU drivers. The fix? Reverting your kernel version and removing the problematic one.

To see the current kernel version use `uname -r`. Then startup [GRUB](./grub.md) when booting. Select the last kernel version before the current broken one.

## Removing the Kernel

1. List kernels
    ```bash
    dpkg -i grep linux-image
    ```

2. Remove the bad kernel
    ```bash
    sudo apt purge linux-image-6.14.0-28-generic
    ```

3. Remove the headers
    ```bash
    sudo apt purge linux-headers-6.14.0-27-generic
    ```
4. If repeating 1 shows an unsigned version of the linux image, that is due to the modules still being installed.
    ```bash
    sudo apt purge linux-modules-6.14.0-27-generic
    ```


### Resources

- [General Steps on Ask Ubuntu](https://askubuntu.com/questions/1338398/how-do-i-remove-newest-kernel)
- [Extra Step on Ask Ubuntu](https://askubuntu.com/questions/1170575/removing-linux-image-kernel-causes-linux-image-unsigned-package-to-be-installed)