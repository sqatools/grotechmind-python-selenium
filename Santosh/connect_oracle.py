#Import Libraries
import cx_Oracle
import pandas as pd
import numpy as np
#Connect to Database
#connstr = cx_Oracle.connect("user/password@server/ServiceName")
connstr = 'hr/hr@localhost:1521/xe'
connection = cx_Oracle.connect(connstr)
cursor = connection.cursor()
#Execute Query
# cursor.execute("select * from employees where department_id=90")
# result = cursor.fetchall()
#
# #Fetch results
# for row in result:
#     print(row)
#Transform Query results into a Pandas Dataframe
#df = pd.DataFrame(result)
#df.columns=[row[0] for row in cursor.description]
var=pd.read_sql_query('select * from employees where department_id=90', connection)
df2=pd.DataFrame(var)
print(df2)
#Commit Changes
# connection.commit()
# #Close Cursor and Connection
# cursor.close()
# connection.close()

# print(" Test Case 1:Following are column Names in source file: \n")
# print(result.columns)
# print('\n')
