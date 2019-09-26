# You can install teradata via PIP: pip install teradata
# to get a list of your odbc drivers names, you could do: teradata.tdodbc.drivers
# You don’t need of coffee driver if using method='rest'.
# See sending data from df to teradata for connection example

import teradata
import pandas as pd

host,username,password, driver = 'ecdwd.it.att.com','DV6CRMLOAD', 'U32_S33mvex35', 'Teradata Database ODBC Driver 16.20'


#Make a connection
udaExec = teradata.UdaExec (appName="test", version="1.0", logConsole=False)
session = udaExec.connect(method="odbc", system=host,
                          username=username, password=password, driver=driver)




#Query
query1 = "SEL DATABASENAME, TABLENAME FROM DBC.TABLES WHERE DATABASENAME = 'DV6CRMDB';"

lst_tables = list()

#Execute query
for row in session.execute(query1):
    lst_tables.append(row)

print(lst_tables[0])


