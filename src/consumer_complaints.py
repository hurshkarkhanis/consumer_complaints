import csv
from operator import itemgetter #tried to sort with itemgetter but ended up not needing to use it
import helper as helper_function #helper_function reads CSV file
from pprint import pprint
import os

data = helper_function.Readfile("../input/complaints.csv")

#create a "lean list" only of the columns I need,
lean_list = []

#loop through complaints.csv to populate it with
#product name, year, and company name
for counter in range(1, len(data.details)): 
	prod = data.details[counter][1]
	year = data.details[counter][0][:4]
	company = data.details[counter][7]

	
	lean_list.append([prod, year, company])


#reset counters so program doesnt count the complaints of different compnies for the same company
def reset_counters():
    company_counter = 0
    cmpl_counter = 0
   

#sort lean list by product
sorted_lean_list = sorted(lean_list)

company_counter = 0
cmpl_counter = 0

#create a final list- this is the one that will be written into reports.csv
final_list = []

#check every line in sorted lean list to see if the NEXT line (i+1) has equal elements (product, year, company) as current line
#increment counters above accordingly

#only write new line in CSV if the next complaint's product and/or year are different 
for i in range(len(sorted_lean_list)-1):
    product_name, yr, company_name = sorted_lean_list[i][0], sorted_lean_list[i][1], sorted_lean_list[i][2]
    if sorted_lean_list[i+1][0] == product_name and sorted_lean_list[i+1][1] == yr and sorted_lean_list[i+1][2] == company_name:
            #same product, same year, same comp
            #all bets are off
            cmpl_counter += 1
            reset_counters()
    elif sorted_lean_list[i+1][0] == product_name and sorted_lean_list[i+1][1] == yr and sorted_lean_list[i+1][2] != company_name:
            #same product, same year, diff company
            company_counter += 1
            cmpl_counter += 1
            reset_counters()
    elif sorted_lean_list[i+1][0] == product_name and sorted_lean_list[i+1][1] != yr and sorted_lean_list[i+1][2] == company_name:
            #same product, different year, same company
            #all bets are off
            cmpl_counter += 1
            final_list.append((product_name, yr, cmpl_counter, company_counter, str(round(company_counter/cmpl_counter, 3)*100)))
            reset_counters()
    elif sorted_lean_list[i+1][0] != product_name and sorted_lean_list[i+1][1] == yr and sorted_lean_list[i+1][2] == company_name:
            #different product same year, same company
            #all bets are off
            final_list.append((product_name, yr, cmpl_counter, company_counter, str(round(company_counter/cmpl_counter, 3)*100)))
            reset_counters()
    elif sorted_lean_list[i+1][0] != product_name and sorted_lean_list[i+1][1] != yr and sorted_lean_list[i+1][2] == company_name:
            #different product, different year, same company
            final_list.append((product_name, yr, cmpl_counter, company_counter, str(round(company_counter/cmpl_counter, 3)*100)))
            reset_counters()
    elif sorted_lean_list[i+1][0] != product_name and sorted_lean_list[i+1][1] == yr and sorted_lean_list[i+1][2] != company_name:
            #different product, same year, different company
            company_counter += 1
            final_list.append((product_name, yr, cmpl_counter, company_counter, str(round(company_counter/cmpl_counter, 3)*100)))
            reset_counters()
    elif sorted_lean_list[i+1][0] != product_name and sorted_lean_list[i+1][1] != yr and sorted_lean_list[i+1][2] != company_name:
            #different product, different year, different company
            company_counter += 1
            final_list.append((product_name, yr, cmpl_counter, company_counter, str(round(company_counter/cmpl_counter, 3)*100)))
            reset_counters()

#pprint(final_list)


write_this = "../output/report.csv"
filepath = os.path.abspath(write_this)

with open (write_this, 'w') as f_output:
        csv_output = csv.writer(f_output)
        csv_output.writerows(final_list)









