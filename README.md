Intro
This is a basic python business logic script with a tinker GUI that looks at a master excel revenue report and returns only select customer data that is inside a separate customer DB excel file. I developed this report as an internal tool in order to automate a monthly report; previously the person doing this report would take a week to create the end report, but I developed this tool that automates the task with a couple clicks.

こちらはTinkerのGUIで簡単なPython営業スクリプトを開発したプロジェクトになります。このスクリプトはマスターExcelファイルから選択したお客のみ収入を取り出せるスクリプトになります。このプロジェクトは弊社ツールとして開発していて、開発した前に一種間ほどの報告が２分程な程度で作れるようになりました。

Use case
For this demonstration, let us pretend that we are an ingredient supplier for various fast food and fast casual restaurant companies, and we are in charge of the Japan region. Every month we receive a master revenue file that contains our regions' customers revenue listed inside of it; however, it is buried within hundreds of other revenue data for all other regions our company operates in. Our task is to create an easy to read report that lists our customer name, revenue for the month of December 2025 and 2024, the account owner, the region the account belongs to, and finally, the restaurant industry the customer can be categorized as.

使うケース
弊社はレストランで素材を売っている、そして私たちは日本地方の担当者になります。毎月すべて地方の収入報告もらいます。私たち毎月この報告を見て日本地方のみの収入を取り出して、弊社地方収入報告を作ります。マスター収入Ｅｘｃｅｌファイルは何百の客が入っているので大変手作業になります。
弊社の客収入する後に、弊社の客のアカウント担当者、お客の地方、そしてお客のカテゴリを付けて弊社の報告を作ります。

The raw excel files
Master Revenue File
Inside this repo are two example documents: one a master revenue report that contains a list of fast food companies, their revenue for December of 2025 and 2024, and other rows that would contain other business data that the script ignores.

Excelファイルの説明
Master収入報告
このファイルはすべての会社お客の収入が入っています。いくつのカラムがあって、Customer name, 12 2025 Revenue, 12 2024 revenue, そしていくつに使わないカラムも付けます。

The Customer DB file
The customer DB file lists twenty Japanese fast food company names that are all within Japan. There are columns denoting each restaurants account owner, the region, and the industry. In this case, the account owners are Kenji, Sarah, and Mateo, the regions are divided between Tokyo, Kyoto, and Osaka, and finally the industry is either fast food or fast casual.

お客DBファイル
お客DBファイルは弊社の２０お客にリストして、そしてお客ずつのアカウント担当者、地方、そしてカテゴリがつけます。


Report for 12 Month.xlsx
This is the end result after running the script, it will take the company names from the customer db template file and scrape the revenue data from the master revenue file. It will also add the account owner, region, and industry details from the customer db file to the end report.

１２月報告
これはスクリプトを作られている結果になります。マスターExcelファイルからお客DBに入っているお客の収入が入って

The script itself
The business logic script, inside the Business_Logic.py file, uses the pandas library to load the excel file, gather the customers inside the customer DB, then scrape the master revenue file for those customers and returning their December revenue for 2025 and 2024. This is then exported into a excel sheet, an example of the end product being the Report for 12 month file in the repo.

スクリプトの説明
業務論理スクリプトはPandasで使ってマスターファイルとお客DBファイルをロードをします。そして、お客ＤＢに入っているお客名前を取り出してマスターファイルに探しています。見つかる後にお客の１２月２０２５年や１２月２０２４年の収入を取りました。最後、お客ＤＢに入っている情報ととっている収入情報を組み合わせて結果Excelファイルを作ります。

GUI

The GUI (graphic user interface) is made with tinker and has four buttons: load master revenue file, load customer DB file, create report, or exit application. It also has a selection textbox to select the month. After selecting the files and a month, the user can click the create report button, which then passes the month information and two files to the business logic which runs and produces the end result, an excel file, that will appear in the same file as the script. I didn't bother adding error handling for instances where a user selects the wrong files as I deemed it not necessary to deal with at the time of development.

GUI
PythonのTinkerライブラリを使って簡単なGUIを作っています。GUIにはファイルを選択したり月選択したりスクリプトを行ったりプログラムを消せることができます。すべての情報に入れいると報告作るバトンをクリックして業務論理スクリプトを動いて新しExcelファイルを作ってくれます。
