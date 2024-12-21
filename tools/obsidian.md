# Obsidian Markdown Editor
## What is it?

A private application for writing and note taking. It's power is in its simplicity and community plugins. Notes are taken in markdown which makes stylizing much easier than using something like Google Docs. The appearance is also very customizable, especially with pre-made themes.
## Appearance

I have Obsidian set to `Dark Mode` with the `Things` theme.
## Plugins

Plugins are vault specific so a plugin installed in one vault will not be seen or used in another unless also installed in that other vault. Commonly used plugins and ones that I use:
- Dataview
	- Allows querying among your notes, transforming your notebook into a database.
	- Two videos on YouTube are great for the basics: [Video 1](https://youtu.be/ccN5vJzXwvo?si=BltJmQh4q2HRXaDg), [Video 2](https://youtu.be/JTObSymEvWA?si=_As8YrZ95TeC19Ws)
- Advanced Tables
	- Markdown tables are automatically formatted
	- Starts simply by entering `| Col 1|`, hit `Enter`, then `|-|` will create the automatically formatting table
	- Use `Ctrl` + `Shift` + `d` to open the side bar editor or add your own hotkeys for table management.
- Advanced Slides
	- Create presentation slides in Markdown as notes
	- The presentation is converted to `reveal.js` and is automatically locally hosted showing the presentation in the browser.
	- This gives the functionality of `reveal.js` such as horizontal and vertical slides.
	- The presentation can be exported as html or to a pdf
	- Check out this [video](https://youtu.be/LtBK_iNcVEQ?si=M4Rio__CJJ0B5U-E) by Nicole van der Hoeven on Advanced Slides.
- Excalidraw
	- Adds drawing and diagramming features into Obsidian
	- Also allows conversion of Mermaid charts into drawing style diagrams
- Linter
	- Allows you to configure linting rules for yaml and markdown
	- I've configured it to operate on `Ctrl` + `s`
- Calendar
	- Adds a calendar that is visible in the right sidebar
	- Easily integrates with daily notes and can be configured to your date style
- Vault Changelog
	- Adds a changelog showing the most recently edited files.
- Settings Search
	- Adds a search bar so a user can search for specific settings
	- This should be a standard feature anyways
- Plugin Update Tracker
	- Lets the user know when a plugin can be updated.
- Kanban
	- Adds markdown backed kanban functionality to Obsidian
	- Great for development projects
- Templater
	- Repeats the basic functionality of the core plugin Templates.
	- Is much more dynamic allowing you to use variables and conditions to format the template for each note instance.
	- Use JS to actively modify values and note data.
	- This is a good [introduction video](https://youtu.be/5j9fAvJCaig?si=QzUUmubywis_gB-U) for Templater by Nicole van der Hoeven
- Git
	- Integrates Git version control for backing up
- Zotero Integration
	- Insert and import data from Zotero

## Linter Settings
- General
	- Lint on Save
- Content
	- Default Language for Code Fences
		- Bash
	- Remove Empty List Markers
	- Remove Multiple Spaces
- Spacing
	- Consecutive Blank Lines
	- Remove Empty Lines Between List Markers and Checklists
	- Remove Link Spacing
	- Trailing Spaces
## Set up Git on Linux Desktop

- My repository is already connected to my remote repository in Gitea
- After installing the [Git plugin](https://publish.obsidian.md/git-doc/Getting+Started), I configured these settings
	- *Auto commit-and-sync interval (minutes)* to *10*
	- *Pull on startup* to ON
	- *Show the count of modified files in the status bar* to ON
## Set up Git on iPhone

- This is more complicated than on desktop Linux but there is a method using iSH (a shell for iOS)
	- This [obsidian forum](https://forum.obsidian.md/t/mobile-ios-app-to-work-with-hidden-folder/25741) post explains how to find the Obsidian notebooks.
	- Once in the Notebook, git can be used from iSH to clone the repository.
	- Then the git plugin can be configured as it would on desktop.
## Resources
- [Obsidian](https://obsidian.md/)
- [Obsidian Docs](https://help.obsidian.md/Home)
- [Videos by Nicole van der Hoeven](https://www.youtube.com/@nicolevdh)
- [Git Plugin](https://publish.obsidian.md/git-doc/Getting+Started) for Obsidian