# Kavita Books Library

## Installing Kavita

The basic install steps can be found [here](https://github.com/Kareadita/Kavita/blob/develop/INSTALL.txt)

1. Download the linux x64 zip from the [releases page](https://github.com/Kareadita/Kavita/releases).

2. Extract the contents to a writable directory where you would keep applications. I have a directory at *~/Apps* for this kind of stuff.

3. Then ```cd Kavita``` and ```chmod +x ./Kavita```. 

## Running Kavita

Screen or some other method for running kavita in the background would be useful. Currently I am just using screen but I would like to make a startup task of turning on the service. To run, just use ```./Kavita``` in the *~/Apps/Kavita* directory.

## Using Kavita

### Setup 

Upon first time use; a username, email, and password will need to be put in. Just typing ```kavita``` in each field worked for me. Then you can sign in with ```kavita```, ```kavita```. **NOTE** If you want to be able to change the admin email or setup the email server it would be simpler to put a real email in.

Now to modify some settings. Click the gear icon in the top right after signing in. 

Under the *General* tab
- Change the port being used from **5000** to something less common like **9876**. 
- You can lower the number of backups and logs to save. I don't see those being extremely important.
- I disabled the send info to Kavita option
- I also enabled the update library on folder changes to make it easier to update the libraries.
- Now hit save and restart Kavita so the port change takes effect.

Under the *Libraries* tab
- Hit *Add Library*
- Then follow the prompts to add a library
- Start by naming the library (e.g. *Books*)
- Select the type (e.g. *Book*)
- Hit *Next*
- Select the location of the books (This could be in a NAS or a drive but I have a directory *~/DigitalLibraries/Books*)
- Hit *Next*
- I skipped adding a cover but that's up to you; hit *Next* again
- The advanced options also aren't necessary so now hit *Save*
- Now the library *Books* will appear on the side bar. (To update the library with its contents, hit the menu icon and select *Scan Library*)

### Customization

Hit the menu icon next to *Home* on the side bar
- Click Customize
- Click the eye icon to hide any of the side bar locations you won't use
- There is also a Dashboard section that can be customized similarly

### Inviting Users

- Hit the settings gear in the top right
- Click the *Users* tab
- Hit the *Invite* button
- Enter the users email (does not need to be real if you are not using a mail server)
- Lastly select the *Libraries* the user will have access to and the *Roles* the user should have

### Adding Books

This part could be done by hand but is better organized with Calibre. See [below](#calibre). Although a series of books in PDF format should be done by hand.

For a PDF series, start with Calibre since it will organize books based on author and the files are easy to move around. As an example, let's assume you have the Inheritance Cycle by Christopher Paolini. Calibre would sort the books into individual book title folders within the folder *Paolini, Christopher*. Kavita will not pick these up as a series since PDFs don't contain a standard metadata. Kavita will however pick up on naming conventions for *[Specials](https://wiki.kavitareader.com/guides/scanner/managefiles)* due to the lack of metadata. This involves having the series name as a directory under *Paolini, Christopher*, then each book in the series is named as [series] SPO[place in series] [book title]. This would look like
```
books_library
|- Paolini, Christopher
   |- Inheritance Cycle
      |- Inheritance Cycle SPO1 Eragon.pdf
      |- Inheritance Cycle SPO2 Eldest.pdf
      |- Inheritance Cycle SPO3 Brisingr.pdf
      |- Inheritance Cycle SPO4 Inheritance.pdf
```

When I've updated the books in my local storage from Calibre or manually, I use rsync to copy the new files/folders to the machine running Kavita. 
```
rsync -r --ignore-existing ~/DigitalLibraries/Books/ argonite:~/DigitalLibraries/Books/
```
- -r is for recursive copy
- --ignore-existing prevents the copy from wasting resources and overwriting existing files

### Smart Filters

A smart filter can be used to sort books on the side nav or in the dashboard. This is especially handy if you want to see all of the books you have or have not read.

To create a smart filter:
- Hit the green filter-icon button in the top right of the screen
- Remove the top filter with the **-** icon
- Make the second filter *Read Progress* *Equals* *100*
- Click *Apply* to see it happen
- Change the *Filter Name* to *Completed Books* 
- Hit *Save*
- Now click the three dots icon next to *Home* on the side nav
- Select *Customize*
- Finally, add the smart filter 

## Calibre

Calibre is a great tool for organizing a book collection and editing the metadata of epubs. Basic use is as follows:
- Download desired book or books
- Drag and drop into Calibre or Click the *Add books* button and select your books
- Right Click on the book you want to edit and hover over *Edit metadata* then select *Edit metadata individually*
- Verify the title and author are correct
  - If one of those fields are modified, click the arrow button to the right of the field to update the sort fields
  - If there are multiple authors, they can be separated by an ampersand (&)
- If the book is part of a series, enter the series and click out of the field to then verify the series entry number is correct. 
  - The entry number can be fractional for series that contain spinoffs, novellas, etc. that, for example, count as book 1.5.
- Then hit *Ok* in the bottom right of the editor to save the changes
- Repeat the metadata modification and verification process for the rest of your added books
- Before exporting the books for Kavita, hit the preferences button
  - Click *Saving books to disk* under the *Import/export* section
  - Uncheck *Save cover separately* and *Save metadata in separate OPF file*
- Now to export all of the books to disk, hit the *Save to disk* button and select the location to save to (The location should be the root of all the books you are using in Kavita such as *~/DigitalLibraries/Books/) 

### File Structure

By default, Calibre exports the books by {author_sort}/{title}/{title} - {authors}. For the *Inheritance Cycle* example, that would look like
```
|- Paolini, Christopher
   |- Eragon
      |- Eragon - Christopher Paolini.pdf
   |- Eldest
      |- Eldest - Christopher Paolini.pdf
   |- Brisingr
      |- Brisingr - Christopher Paolini.pdf
   |- Inheritance
      |- Inheritance - Christopher Paolini.pdf
```

