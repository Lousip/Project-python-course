# Import required packages
import qpcr
import csv


# Set up which files are the samples and which is the housekeeping gene 
assay_files = [r"C:\Users\xlloui\Documents\12S.xlsx"]
normaliser_files = [r"C:\Users\xlloui\Documents\18S.xlsx"]

# Put the xls files in a string variable
assays = qpcr.read(assay_files)
normalisers = qpcr.read(normaliser_files)

reader = qpcr.DataReader()

assays = reader.read(assay_files)
normalisers = reader.read(normaliser_files)

# compute normalisation of dCT
assays = qpcr.delta_ct(assays)
normalisers = qpcr.delta_ct(normalisers)

# compute normalisation ddCT
results = qpcr.normalise(assays, normalisers)

# visualise the plot and save it in the format you need
fig = results.preview()


# To save the datas to a new csv file
input_variable = [results]
 
# A new file .csv gets created in the current working directory
with open ('12SddCT18S.csv','w',newline = '') as csvfile:
    my_writer = csv.writer(csvfile, delimiter = ' ')
    my_writer.writerows(input_variable)





