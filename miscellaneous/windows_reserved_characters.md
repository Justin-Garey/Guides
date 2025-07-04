# Reserved Characters in Windows Filepaths

While trying to clone some of my Obsidian notes repositories onto a Windows partition, I ran into some issues due to filenames that were fine on Linux. Windows [specifies](https://learn.microsoft.com/en-us/windows/win32/fileio/naming-a-file) that certain characters are reserved and cannot be used for filenames. That list includes: 


> - The following reserved characters:
>   - < (less than)
>   - \> (greater than)
>   - : (colon)
>   - " (double quote)
>   - / (forward slash)
>   - \ (backslash)
>   - | (vertical bar or pipe)
>   - ? (question mark)
>   - \* (asterisk)

I wrote a simple [windows name check](../example_programs/python/windows_name_check.py) python script to report files breaking the not conforming to the reserved character list in Windows.
