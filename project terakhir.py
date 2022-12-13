import pandas as pd
import csv
import os

file_csv_nya = 'stok kopi.csv'

def clearscreen():
    '''Clear screen function'''
    os.system("cls")


print("===Coffee Inventory===")
opsi_klik = input("")
if opsi_klik == '':
    clearscreen()
    pword = input("Enter your password:")
    print(pword)
    while True:
        if pword == "kopimantap":
            clearscreen()
            print(" [1] Show data \n [2] New data\n [3] Hapus data \n [4] Edit data")    
            opsi_klik_admin = input("")
        
        if opsi_klik_admin == '1':
            clearscreen()
            nama_file = 'stok kopi.csv'
            readdf = pd.read_csv(nama_file, on_bad_lines='skip')
            print(readdf)
            enter = input("")
            print(enter)

        elif opsi_klik_admin == '2':
            clearscreen()
            with open(file_csv_nya, mode='a', newline='') as csvfile:
                fieldnames = ['Code', 'Name', 'Price', 'QTY']
                Writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                print("=--=" * 20)       
                print("=--=--= Add Item =--=--=")
                print("=--=" *20)        
                Codenya = input("Code item: ")
                Namenya = input("Item name: ")
                Pricenya = input("Item price: ")
                QTY = input("Number of item: ")
                print("=--=" * 20) 
                Writer.writerow({'Code' : Codenya, 'Name' : Namenya, 'Price' : Pricenya, 'QTY' : QTY })
        elif opsi_klik_admin == '4':
            clearscreen()
            Itemorgoods = []
            with open(file_csv_nya, mode='r', newline='') as csvfile:
                Csv_reader = csv.DictReader(csvfile)
                for row in Csv_reader:
                    Itemorgoods.append(row)
            
            x = pd.read_csv(file_csv_nya)
            print(x)
            
            Code = input("Choose codes item: ")
            Name = input("New name: ")
            Price = input("New price: ")
            QTY = input("New number of item: ")
    
            Indeks = 0
            for data in Itemorgoods:
                if (data['Code'] == Code):
                    Itemorgoods[Indeks]['Name'] = Name
                    Itemorgoods[Indeks]['Price'] = Price
                    Itemorgoods[Indeks]['QTY'] = QTY

                Indeks = Indeks + 1
            with open(file_csv_nya, mode='w') as csv_file:
                fieldnames = ['Code', 'Name', 'Price', 'QTY']
                Writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                Writer.writeheader()
                for new_data in Itemorgoods:
                    Writer.writerow({'Code' : new_data['Code'], 'Name' : new_data['Name'], 'Price' : new_data['Price'], 'QTY' : new_data['QTY']})
        elif opsi_klik_admin == '3':
            clearscreen()
            The_Item = []
            with open(file_csv_nya, mode="r") as csvfile:
                csv_reader = csv.DictReader(csvfile)
                for row in csv_reader:
                    The_Item.append(row)
            
            x = pd.read_csv(file_csv_nya, on_bad_lines='skip')
            print(x)
            print("--------------------------------------------------------")
            kode = input("Hapus Barang dengan KODE : ")
            indeks = 0
            for data in The_Item:
                if (data['Code'] == kode):
                    The_Item.remove(The_Item[indeks])
                indeks = indeks + 1
            with open(file_csv_nya, mode="w") as csvfile:
                fieldnames = ['Code', 'Name', 'Price', 'QTY']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                for new_data in The_Item:
                    writer.writerow({'Code': new_data['Code'], 'Name': new_data['Name'], 'Price': new_data['Price'], 'QTY': new_data['QTY']})         
            
            
            print("Data sudah terhapus") 
            break
                    
        else:
            clearscreen()
            print("xxxPassword anda salaaahhxxx")
    

            

                

    
        
        

            
            
            






