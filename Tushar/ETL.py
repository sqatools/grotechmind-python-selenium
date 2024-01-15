import pandas as pd

source = pd.read_csv(r"C:\Users\Lenovo\Desktop\emp.csv", sep=",")
print("TC1:Following are the columns name in source file:")
print(source.columns)

print("TC2:Rows X columns in the source file")
print(source.shape)

print("TC3: Number of rows under each column")
print(source.count())

print("TC4: Duplicate records in the source")
print(source.duplicated().sum())

print("TC5: Duplicate records saved in the file below")
dupes = source[source.duplicated()].to_csv("duplicated.csv")


# source=pd.read_csv ("emp.csv",sep=",")
# print("TC1:Following are the columns name in source file:")
# print(source.columns)

# import pandas as pd
#
# dict = {'Name' :['john', 'jenny', 'Dan'], 'Age' : [30, 40, 50]}
#
# df = pd.DataFrame(dict)
# print(df)
