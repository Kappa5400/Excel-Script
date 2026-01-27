
import pandas as pd
from pathlib import Path


def Business_logic(month, excel, customer_db):

    #Load the excel file.
    raw = pd.read_excel(excel, sheet_name=0, skiprows=2)
    raw_df = pd.DataFrame(raw)
    
    #Take excel file and take only the company name and revenue for 2025  and 2024.
    raw_df = pd.DataFrame(raw_df.groupby("COMPANY NAME")[[f"REVENUE {month} 2025",f"REVENUE {month} 2024"]].sum())
    raw_df = raw_df.reset_index()

 

    #Load customer information.
    customer = pd.read_excel(customer_db)

    customer_df = pd.DataFrame(customer)

    #Match the customers we want the revenue for with the original master file.
    Finished_df = pd.merge(raw_df, customer_df, on="COMPANY NAME")

    #Export to excel filetype.
    Finished_df.to_excel(f"Report for {month} month.xlsx")

    print("Success")



Business_logic(12, "Revenue report template.xlsx", "Customer DB Template.xlsx")