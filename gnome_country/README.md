# Why?

We need to obtain the country of the genomes

## Step 1: Access the Table with links to each country

Go to this website, scroll down and see the table:
https://www.coriell.org/1/NHGRI/Collections/1000-Genomes-Project-Collection/1000-Genomes-Project#:~:text=The%201000%20Genomes%20Project%20is%20an%20important,relating%20genetic%20variation%20to%20health%20and%20disease.

This table includes links to each of the group (nation) of genomes. For example: **Kinh in Ho Chi Minh City, Vietnam [KHV]** has the link: https://www.coriell.org/1/NHGRI/Collections/1000-Genomes-Project-Collection/Kinh-in-Ho-Chi-Minh-City-Vietnam-KHV


## Step 2: Download Excel file that includes genomes of one country

Continue with the above example of **Kinh in Ho Chi Minh City, Vietnam [KHV]** above.

First, go to link (from the table above):  https://www.coriell.org/1/NHGRI/Collections/1000-Genomes-Project-Collection/Kinh-in-Ho-Chi-Minh-City-Vietnam-KHV

You will see **DNA 124**. Click on **124**, you will go to this link: https://www.coriell.org/Search?grid=0&q=%22Kinh+in+Ho+Chi+Minh+City%22&csId=&f_2=DNA

This link displays a Table. For **Page Size**, select **All** so 124 genomes will be displayed on the first page. Then, select **Export to Excel**. Next, select **All Fields** in the pop-up window, and **Export All Samples in Grid**.

The table will be exported to your local **Downloads** folder, the name of the file has the date, for example: **Coriell-Catalog-Export-07-14-2025.csv**. You can rename the file to indicate the population, for example: **KHV_Coriell-Catalog-Export-07-14-2025.csv**

## Step 3: save this file on git
You will `git add` the file, for example: `git add KHV_Coriell-Catalog-Export-07-14-2025.csv`, and `git commit -m "save KHV csv file"`, and `git push` to save it on git for future reference.

