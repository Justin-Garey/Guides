/**
 * Function: changeChartTitle
 * Description: Changes the specified chart title based on a custom value
 */
function changeChartTitle() {
  const sheetName = 'Sheet1'
  const chartID = 0
  const customTitleCell = 'A1'
  
  const sheet = SpreadsheetApp.getActiveSpreadsheet().getSheetByName(sheetName);
  const chart = sheet.getCharts()[chartID];
  const newTitle = sheet.getRange(customTitleCell).getValue();

  // Update chart
  const chartBuilder = chart.modify();
  chartBuilder.setOption('title', newTitle);
  const updatedChart = chartBuilder.build();
  sheet.updateChart(updatedChart);
}