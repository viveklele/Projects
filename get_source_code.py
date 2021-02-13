import inspect
import inbuilt      #module name 
line = inspect.getsource(inbuilt)
file = open("source_code.py", "w")
file_data = file.write(line)
print(file_data)
print("File sucessfully written in: source_code.py")
