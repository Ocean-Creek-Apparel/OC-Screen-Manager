Author:  Cullen Gostel
Version: 08/02/24

This software is designed for Ocean Creek Apparel. It is intended to allow employees to easily
locate screens within the warehouse.

*** FOLDERS ***
- Documentation, includes diagrams and other additional documentation
- Screen Manager Forms Application, Visual Studio solution folder
- Database, SQL database folder

*** OBJECTS/RECORDS ***
SCREEN
- Unique Identifier       "ScreenID" (SQL)     "ID" (C#)
- Location information    "LocationID" (SQL)   "LocationID" (C#)
- Design information      "Design" (SQL)       "Design" (C#)
- Customer information    "CustomerName" (SQL) "CustomerName" (C#)
- Additional information  "Description" (SQL)  "Description" (C#)

LOCATION
- Unique Identifier       "LocationID" (SQL)   "ID" (C#)
- Additional information  "Description" (SQL)  "Description" (C#)

*** ADDITIONAL PACKAGES USED ***
- Microsoft.Data.Sqlite, necessary for SQL integration
