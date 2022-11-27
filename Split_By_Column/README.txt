		---------------- UTILITY -------------------

With this script we get to split a given Excel by the unique
values of a given column.

For example, for a given Excel with 8 columns, being one of them "Country"
where there are 5 Unique Values: Spain, Jamaica, Belice, Guinea and Congo.
We will receive 5 Excels (One for each country) with the 8 columns 
but only with the data of each country.

There is an Excel Example in the folder INPUTS. (Delete before use the script)

	    -------------------- IMPORTANT --------------------

Python must be installed --> 
Microsoft Store, App Store, https://www.python.org/downloads/

Pip must be installed --> 

https://www.neoguias.com/como-instalar-pip-python/#Como_instalar_PIP_en_Windows

Folder structure MUST NOT BE CHANGED

   	   -------------------- INTRUCTIONS ------------------

FOLDER INPUTS --> Where you have to set the Excel to Split
FOLDER Files --> Where the script is located

Excel: Must be closed in order to allow the Script Access
Excel: Data must be in a simple table (Columns with Headers, 
	and rows). Beginning in A1
Excel: There only must be ONE Excel inside INPUTS

Once the Script is Executed, if everything goes good:

     - It is going to request a name for the folder where the OUTPUTS will be saved
       If the folder already Exists, nothing will change.
       If it does not exists, it will be created at the same level of the Executable

     - Finally, it will request you the name of the column which you want to split by.
       You will see the list of columns you have available. You have to introduce the
       name of the column exactly as it is written in the DataFrame (Case sensitive)


------------------------------------------------------------------------------

Dudas a GabinoAntOrt95@gmail.com
