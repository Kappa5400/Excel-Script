Intro
This is a basic python business logic script with a tinker GUI that looks at a master excel revenue report and returns only select customer data that is inside a separate customer DB excel file. I developed this report as an internal tool in order to automate a monthly report; previously the person doing this report would take a week to create the end report, but I developed this tool that automates the task with a couple clicks.

Use case
For this demonstration, let us pretend that we are an ingredient supplier for various fast food and fast casual restaurant companies, and we are in charge of the Japan region. Every month we receive a master revenue file that contains our regions' customers revenue listed inside of it; however, it is buried within hundreds of other revenue data for all other regions our company operates in. Our task is to create an easy to read report that lists our customer name, revenue for the month of December 2025 and 2024, the account owner, the region the account belongs to, and finally, the restaurant industry the customer can be categorized as.

The raw excel files
Master Revenue File
Inside this repo are two example documents: one a master revenue report that contains a list of fast food companies, their revenue for December of 2025 and 2024, and other rows that would contain other business data that the script ignores.

The Customer DB file
The customer DB file lists twenty Japanese fast food company names that are all within Japan. There are columns denoting each restaurants account owner, the region, and the industry. In this case, the account owners are Kenji, Sarah, and Mateo, the regions are divided between Tokyo, Kyoto, and Osaka, and finally the industry is either fast food or fast casual.

Report for 12 Month.xlsx
This is the end result after running the script, it will take the company names from the customer db template file and scrape the revenue data from the master revenue file. It will also add the account owner, region, and industry details from the customer db file to the end report.

The script itself
The business logic script, inside the Business_Logic.py file, uses the pandas library to load the excel file, gather the customers inside the customer DB, then scrape the master revenue file for those customers and returning their December revenue for 2025 and 2024.  

GUI
The GUI (graphic user interface) is made with tinker and has four buttons: load master revenue file, load customer DB file, create report, or exit application. It also has a selection textbox to select the month. After selecting the files and a month, the user can click the create report button, which then passes the month information and two files to the business logic which runs and produces the end result, an excel file, that will appear in the same file as the script. I didn't bother adding error handling for instances where a user selects the wrong files as I deemed it not necessary to deal with at the time of development.
