# vcf_py
## CSV to VCF (virtual contact file) generator

This program allows you to extract the contact information (names and numbers) of multiple people from a CSV file and compile it into a virtual contact file (VCF) which can be easily imported into many devices and platforms such as smartphones and email clients, thereby allowing for a fast and efficient transfer of numerous contacts from spreadsheets to phones.

## Usage
The CSV file containing the contact information should be in the same folder as the vcf.py file and should adopt the following format:
```
name1,number1
name2,number2
```
Microsoft Excel should be used to open and update the contacts for convenience. When doing so, ensure that the names and numbers do not contain any commas. Column A should contain the names and column B should contain the corresponding numbers. The columns, however, should not have headings, i.e. row 1 will be assumed to be the contact for the first person.
