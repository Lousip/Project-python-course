# Import required packages
import qpcr
import csv


# Set up which files are the samples and which is the housekeeping gene 
assay_files = [r"C:\Users\file"]
normaliser_files = [r"C:\Users\file"]

# Put the xls files in a string variable
assays = qpcr.read(assay_files)
normalisers = qpcr.read(normaliser_files)

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
print(results)
# visualise the plot and save it in the format you need
fig = results.preview()


# To save the datas to a new csv file
results_csv = [results]
 

# A new file .csv gets created in the current working directory. New file is the normalisation of the assays 12S to the housekeeping gene 18S
# Input names of your normaliser and assay to output name of your new file
nameassay = input("name gene assay: ")
namenorm = input("name gene normaliser: ")
name.csv = namearrays + "ddct" + namenorm + ".csv"
with open (name.csv,'w',newline = '') as csvfile:
    my_writer = csv.writer(csvfile, delimiter = ' ')
    my_writer.writerows(results_csv)





