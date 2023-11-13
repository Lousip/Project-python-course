# Import required packages
import qpcr
import csv


# Set up which files are the samples and which is the housekeeping gene 
assay_files = input("Name of assay file: ")
open(assay_files, 'r')
normaliser_files = input("Name of normaliser file: ")
open(normaliser_files, 'r')

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
# visualise the plot and save it in png
fig = results.preview()
fig.savefig("results_pcr.png")

# To save the datas to a new csv file
results_csv = [results]
# A new file .csv gets created in the current working directory. New file is the normalisation of the assays 12S to the housekeeping gene 18S
# Input names of your normaliser and assay to output name of your new file
nameassay = input("name gene assay: ")
namenorm = input("name gene normaliser: ")
name_csv = nameassay + "ddct" + namenorm + ".csv"
with open (name_csv,'w',newline = '') as csvfile:
    my_writer = csv.writer(csvfile, delimiter = ' ')
    my_writer.writerows(results_csv)


