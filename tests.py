# Task  1 deadline is 21/09/2022
import requests
import json
import openpyxl


book = openpyxl.Workbook()
sheet = book.active

response = requests.get(url="https://jsonplaceholder.typicode.com/todos")
data = response.json()
print(data)

 # запись объектов в файл json
for k, value in enumerate(data):
        filename = f'files/data.json{k}'
        with open(filename, 'w', encoding="utf-8") as f:
                json.dump(data[k], f, ensure_ascii=False, indent=8)

# прочитать все файлы из папки и сохранить в массив
data_from_folders = []
for i in range(0, len(data)):
        filename = f'files/data.json{i}'
        data_dict= open(filename)    #deserialization
        dt= json.load(data_dict)
        data_from_folders.append(dt)
        print((f'Saved file {filename}'))
print("Datatype after de-serialisation: " + str(type(dt)))



sheet['A1'] = "userId"
sheet['B1'] = "id"
sheet['C1'] ="title"
sheet['D1'] ="completed"
row = 2
for i in range(0, len(data)):
        filename = f'files/data.json{i}'
        data_dict= open(filename)     #deserialization
        dt= json.load(data_dict)
        for i in range(len(dt)):
                sheet[row][0] .value= dt["userId"]
                sheet[row][1].value = dt["id"]
                sheet[row][2].value = dt["title"]
                sheet[row][3] .value= dt["completed"]
                row +=1
        print(f'Saved file {filename}')

book.save("my_book.xlsx")
book.close()
print("Total saved files: " ,  len(data))
