# First need to install and import all packages
import qpcr
import pandas as pd


#Need to set up which files are the samples and which is the housekeeping gene.
assay_files = [r"C:\Users\xlloui\Documents\12S.xlsx", r"C:\Users\xlloui\Documents\COXII.xlsx"]
normaliser_files = [r"C:\Users\xlloui\Documents\18S.xlsx"]

assays = qpcr.read(assay_files)
normalisers = qpcr.read(normaliser_files)
assays[0]

reader = qpcr.DataReader()

# then read the files
assays = reader.read(assay_files)
normalisers = reader.read(normaliser_files)

assays = qpcr.delta_ct(assays)
normalisers = qpcr.delta_ct(normalisers)

results = qpcr.normalise(assays, normalisers)

fig = results.preview()



