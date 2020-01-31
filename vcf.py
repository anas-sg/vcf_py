import os, subprocess, csv
input("vCard Generator v1.0\n\nThis program helps you to export multiple phone contacts from a Microsoft Excel SpreadSheet to your phone.\nBefore starting, please ensure the following:\n\n* Column A contains the names of the people and column B contains the corresponding phone numbers\n* The SpreadSheet does not contain any commas or column headers\n* The rest of the SpreadSheet is empty\n* You have saved the file in the CSV (Comma delimited) (*.csv) format\n* The CSV file is in the same location as this program\n\nPress ENTER after verifying the above...")
while True:
    files = os.listdir(os.getcwd())
    files_csv = [i for i in files if i.lower().endswith('.csv')]
    if len(files_csv)>1:
        for file in files_csv:
            print(f"{str(files_csv.index(file))}) {file}")
        n = input("\n\nEnter the index number of the CSV file: ")
        if n.isnumeric():
            if (int(n) in range(len(files_csv))):
                print(f"Reading {files_csv[int(n)]}...\n")
                with open(files_csv[int(n)]) as data:
                    contacts = {name:num.replace(" ","") for name,num in list(csv.reader(data))}
            else:
                print("\nInvalid input!\n\n")
                continue
        else:
            print("\nInvalid input!\n\n")
            continue                
    elif len(files_csv)==1:
        print(f"Reading {files_csv[0]}...\n")
        with open(files_csv[0]) as data:   
        	contacts = {name:num.replace(" ","") for name,num in list(csv.reader(data))}
    else:
        input(f"\nError! No CSV file in current folder. Save CSV file to\n{os.getcwd()}\n\nPress ENTER to try again..")
        continue    
    if all(contacts.keys()) and all(contacts.values()):
        for name in contacts:
            if not contacts[name].isnumeric():
                input("Invalid data! Check that column B contains only numeric digits.\nPress ENTER to try again...")
                continue
        else:
            break            
    else:
        input("Error! Check that the number of names is equal to the number of phone numbers. Remove any empty data and press ENTER to try again...")
        continue
prefix = input("Enter text to prefix to contacts' names (if needed): ").strip()
input(f"contacts.vcf will be created/overwritten at {os.getcwd()}\nPress ENTER to continue...")
with open("contacts.vcf", "w") as vcf:
    for i in contacts:
        vcf.write(f"BEGIN:VCARD\nVERSION:3.0\nFN:{prefix} {i}\nN:;{prefix} {i}\nTEL;TYPE=CELL:{contacts[i]}\nEND:VCARD\n")
print("Operation completed successfully!")
os.startfile(os.getcwd())