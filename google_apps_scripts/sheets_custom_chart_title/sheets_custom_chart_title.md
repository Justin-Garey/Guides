# Custom Chart Title in Sheets

I was trying to make a custom pie chart title to show total expenses for a group of expenditures but found that Google Sheets doesn't have that functionality built in. I found this [tip](https://benlcollins.kit.com/posts/sheets-tip-272-dynamic-chart-heading-in-sheets) from Ben Collins which had the exact solution I was looking for. I've slightly modified the [Apps Script](./sheets_custom_chart_title.gs) to be more readable. All it does is set the title of the chart to a cell every time the sheet is modified. To set it up yourself:

1. In Sheets, in the toolbar, select *Extensions* -> *Apps Script*
2. Copy the [Apps Script](./sheets_custom_chart_title.gs) to your editor, then press save. The script is currently setup to take the value in Cell `A1` in Sheet `sheet1` which can be set to whatever you may need.
3. On the left menu from the code editor, select *Triggers*.
4. Click on the *+ Add Trigger* button.
5. The trigger should be set to the script you are using with the event type being *On edit*.
6. Click *Save*
7. Lastly, you will be prompted to grant your script read and write permissions.

Now when the text changes, so will the chart title.
