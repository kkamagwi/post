'''
Создание таблицы из JSON
Перед работой необходимо в терминале 
установить бибилиотеку pandas командой
pip install pandas
'''
import pandas


data = [
    { "id": "1001", "type": "Regular" },
    { "id": "1002", "type": "Chocolate" },
    { "id": "1003", "type": "Blueberry" },
    { "id": "1004", "type": "Devil's Food" }
    ]
            
df = pandas.DataFrame(data=data)
print(df)
# @endhmPythON