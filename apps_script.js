function generateReportPDF() {
  
  var spreadsheetId = '1FurG8dzyFzl-sOdaYsN57X2Vwfs17WVC8GTVRUQmX1Y';

  var sheetName = 'graph';

  // Access the report data from the specified sheet
  var spreadsheet = SpreadsheetApp.openById(spreadsheetId);
  var sheet = spreadsheet.getSheetByName(sheetName);

  // Create a new Google Docs document to generate the report
  var doc = DocumentApp.create('October 2023 Report on Reviews and Ratings');

  // Access the document's body
  var body = doc.getBody();

  // Access the data from the Google Sheet
  var data = sheet.getDataRange().getValues();

  // Add the data to the document with styling
  var table = [];
  for (var i = 0; i < data.length; i++) {
    var row = data[i];
    table.push(row);
  }

  // Create a table element and apply styling
  var docTable = body.appendTable(table);
  var style = {};
  style[DocumentApp.Attribute.BORDER_COLOR] = '#000000';
  style[DocumentApp.Attribute.BORDER_WIDTH] = 1;
  style[DocumentApp.Attribute.FOREGROUND_COLOR] = '#000000';
  style[DocumentApp.Attribute.FONT_SIZE] = 10;

  for (var i = 0; i < table.length; i++) {
    var row = docTable.getRow(i);
    for (var j = 0; j < table[i].length; j++) {
      var cell = row.getCell(j);
      cell.setAttributes(style);
    }
  }

  // Save and close the document
  doc.saveAndClose();

  // Get the ID of the newly created document
  var docId = doc.getId();

  // Export the document as a PDF
  var pdf = DriveApp.getFileById(docId).getAs('application/pdf');

  // Save the PDF to Google Drive
  var pdfFile = DriveApp.createFile(pdf);

  // Get the URL of the saved PDF
  var pdfUrl = pdfFile.getUrl();

  // Log the PDF URL
  Logger.log('PDF URL: ' + pdfUrl);

  // Delete the temporary Google Docs document
  DriveApp.getFileById(docId).setTrashed(true);
}
