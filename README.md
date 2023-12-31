# Trustpilot Reviews Parser

A Python script for parsing Trustpilot reviews of a specified website and recording the data in a Google Sheets document. Additionally, an Apps Script is provided for exporting the data to a Google Docs document and creating a PDF report.

## Features

- **parser.py**: Python script to scrape and record Trustpilot review data.
- **apps_script.js**: Google Apps Script for exporting data to a Google Docs document and generating a PDF report.
- **requirements.txt**: List of Python packages required to run the script.
- **credentials.json**: Google Sheets API credentials file (required for data recording).

## Usage

1. Clone the repository to your local machine.
2. Install the required Python packages by running:

```
pip install -r requirements.txt
```

3. Set up your Google Sheets API credentials:

- Create a project on the [Google Cloud Console](https://console.cloud.google.com/).
- Enable the Google Sheets API and create credentials.
- Download the credentials JSON file and save it as `credentials.json` in the project directory.

4. Modify the `url` variable in `parser.py` to specify the Trustpilot review page URL you want to scrape.

5. Run the Python script to start scraping data and recording it to a Google Sheets document:

```
python trustpilot_parser.py
```

6. To generate a PDF report, execute the `generateReportPDF` function in `apps_script.js` via Google Apps Script. Refer to the [Google Apps Script documentation](https://developers.google.com/apps-script) for more information on running scripts.

## Notes

- Data is recorded in a Google Sheets document. Ensure you have the necessary permissions to access and edit this document.
- The PDF report generated by `generateReportPDF` in `apps_script.js` includes the scraped data in tabular form along with chart images from your Google Sheets document.

## Author

- Alibek Zhubekov 

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


