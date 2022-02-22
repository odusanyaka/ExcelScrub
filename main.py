#Kehinde Odusanya 
#Scrub CUCM for profiles with specific tags like /T/ which signifies tenants. 
#2/7/2022


import csv
import os



def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    file = input("enter file name with extension include filepath from C:/: ")
    print(file)
    #file = "TenantSheet.csv"


    while exit != 1:

        try:
            TenantsFile = open(file)
        except IOError:
            print('unable to open file')
        
        
        with TenantsFile:
            with open('Export.csv', 'w', newline='') as exportfile:
                #line to search for a key term and return the entire row with that key term
                search = input("what would you like to find?")
                Tenants = csv.reader(TenantsFile, delimiter=' ', quotechar='|')
                for row in Tenants:
                    for cell in row:
                        if (cell.find(search) != -1):

                                TenantExport = csv.writer(exportfile, delimiter=' ',
                                                          quotechar='|', quoting=csv.QUOTE_MINIMAL)
                                TenantExport.writerow(row)
                                print(row)
        
        #append new rows for searched value to bottom of CSV file. 
        appendanswer = input("append?")
        if appendanswer == "y" or appendanswer == "Y":
            while exit != 1:
                with open(file) as TenantsFile:
                    with open("Export.csv", 'a') as ef:
                        search = input("what would you like to find?")
                        ef.write(search + '\n')
                        Tenants = csv.reader(TenantsFile, delimiter=' ', quotechar='|')
                        for row in Tenants:
                            for cell in row:
                                if (cell.find(search) != -1):
                                    for cell in row:
                                        ef.write(cell)
                                    ef.write('\n')
                                    print(row)
                exitanswer = input("exit?")
                if exitanswer == "y" or exitanswer == "Y":
                    exit = 1

                else:
                    exit = 0
        else:
            exitanswer = input("exit?")
            if exitanswer == "y" or exitanswer == "Y":
                exit = 1

            else:
                exit = 0
    os.system("pause")
