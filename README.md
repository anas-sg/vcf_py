# vcf_py
## CSV to VCF (virtual contact file) generator

This program allows you to extract the contact information (names and numbers) of multiple people from a CSV file and compile it into a virtual contact file (VCF) which can be easily imported into many devices and platforms such as smartphones and email clients, thereby allowing for a fast and efficient transfer of numerous contacts from a spreadsheet.

## Requirements
If the contacts are stored in a Microsoft Excel Spreadsheet, the file should first be opened with Excel and then saved as `CSV (Comma delimited) (*.csv)`. It is recommended to open the generated CSV file using a text editor to ensure that it follows this format:
```
name1,number1
name2,number2
...
```
- Ensure that the **names and numbers do not contain any commas**. 
- Column A should contain the names and column B should contain the corresponding numbers. 
- The columns must not have headings, i.e. row 1 will be assumed to be the contact for the first person.
- The CSV file containing the contact information should be in the same folder as `vcf.py`

## Usage
Run the `vcf.py` script from the Terminal/Command Prompt:
```
python vcf.py
```
Assuming the CSV file is in the same folder as `vcf.py`, the script would automatically detect the CSV file and attempt to read from it.