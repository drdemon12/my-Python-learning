import os
os.system("notepad.exe") # uygulamayı açar

result=os.path.abspath("os.py") # dizini verir
result = os.path.splitext("os.py") # format ile isimi ayırır 
result=result[1] # dosya türü
result=result[0] # dosya adı
print(result)