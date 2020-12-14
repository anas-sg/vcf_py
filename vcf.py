import os, subprocess, csv

def read(file):
    '''Parse CSV and read into dictionary as num:name pairs'''
    with open(file) as data:
        for i, contact in enumerate(csv.reader(data)):
            name, num = contact[0].strip(), contact[1].strip().replace(" ","")
            if not name:
                raise ValueError(f"Name is empty in line {i+1}")
            if not num:
                raise ValueError(f"Number is empty in line {i+1}")
            try:
               int(num)
            except ValueError:
               raise ValueError(f"Number is invalid on line {i+1}")     
            if num in contacts:    
                replace = input(f"{num}:{name} already exists under {contacts[num]}. Replace? y or n: ").lower()[0]
                if replace == 'y':
                    contacts[num] = name
            else:
                contacts[num] = name

input("vCard Generator v2.0\n\nThis program helps you to export multiple phone contacts from a Microsoft Excel SpreadSheet to your phone.\nBefore starting, please ensure the following:\n\n* Column A contains the names of the people and column B contains the corresponding phone numbers\n* The SpreadSheet does not contain any commas or column headers\n* The rest of the SpreadSheet is empty\n* You have saved the file in the CSV (Comma delimited) (*.csv) format\n* The CSV file is in the same location as this program\n\nPress ENTER after verifying the above...")
files_csv = [i for i in os.listdir(os.getcwd()) if i.lower().endswith('.csv')]
contacts = dict()
if len(files_csv) > 1:
    for file in files_csv:
        print(f"{str(files_csv.index(file))}) {file}")
    n = input("\n\nEnter the index number of the CSV file: ")
    if n.isnumeric():
        if (int(n) in range(len(files_csv))):
            print(f"Reading {files_csv[int(n)]}...\n")
            read(files_csv[int(n)])
        else:
            raise ValueError(f"\nInvalid input! {n} is out of range.\n\n")
    else:
        raise ValueError(f"\nInvalid input! {n} is not a number.\n\n")               
elif len(files_csv) == 1:
    print(f"Reading {files_csv[0]}...\n")
    read(files_csv[0])
else:
    raise ValueError(f"\nError! No CSV file in current folder. Save CSV file to\n{os.getcwd()}\n\nPress ENTER to try again..")

prefix = input("Enter text to prefix to contacts' names (if needed): ").strip()
input(f"contacts.vcf will be created/overwritten at {os.getcwd()}\nPress ENTER to continue...")
with open("contacts.vcf", "w") as vcf:
    for num in contacts:
        vcf.write(f"BEGIN:VCARD\nVERSION:3.0\nFN:{prefix} {contacts[num]}\nN:;{prefix} {contacts[num]}\nTEL;TYPE=CELL:{num}\nEND:VCARD\n")
print("Operation completed successfully!")
os.startfile(os.getcwd())