import pandas as pd
import os

def split_col_by_unique_values(df, column, name_output_directory):
    
        
    '''
    
    For a given DataFrame and Column, the output is in a folder, the same DataFrame splited in diferent Excels Files (One for each unique Value)
    The task in Excel would be: 1) Having a column with 8 diferent values
                                2) Filter by the first value, copy, paste and save
                                3) Same for the remaining values
                                4) the result are 8 Excels
    
    INPUTS: 
    
    df : DataFrame to split
    column : col to be split
    name_output_directory : name of the folder where the splitted Excels will be located (If not exists, it is created below this script)
    
    OUTPUT:
    
    Splitted Excels
    
    '''
    import pandas as pd
    import os 
    
    try:
        os.mkdir("../" + str(name_output_directory))
    except:
        print("Not possible create a folder with that name, if it already exists, it will be used to store the Outputs")
    
    df[column] = df[column].fillna('EMPTY')
    
    for value in [e.replace(' ', '_') for e in df[column].unique()]:

        locals()[value] = df[(df[column] == value.replace('_', ' '))]
        
        try:     
            locals()[value].to_excel("../" + name_output_directory + '/' + str(value) + '.xlsx', index = False)
            print("Saved in: " + name_output_directory + '/' + str(value) + '.xlsx')
        except:  
            continue
            
    print("------- Split Done -------")


if len([e for e in os.listdir("../INPUTS") if '.xl' in e.lower()]) == 1:
    
    print("---------------- READING EXCEL -------------------")

    df = pd.read_excel("../INPUTS/" + [e for e in os.listdir("../INPUTS") if '.xl' in e.lower()][0])

    name_output = str(input("Folder name where you want to save the OUTPUTS: "))

    column = str(input(f"""
                            ¿What column you want to split by? The existing columns are the following: 

                            {[e for e in df.columns]}

                            """))

    if column not in [e for e in df.columns]:
        column = str(input(f"""
        Selected column doe snot exist, select one of the shown columns.
        ¿What column you want to split by? The existing columns are the following: 

        {[e for e in df.columns]}

        """))
    if column not in [e for e in df.columns]:
        print("That column does not exist")
    else:

        split_col_by_unique_values(df, column, name_output)

elif len([e for e in os.listdir() if '.xl' in e.lower()]) > 1:
    print("Just one Excel inside the folder, please")
else:
    print("Excel File not found")

