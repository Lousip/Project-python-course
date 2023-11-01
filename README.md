# Project-python-course

A python code for calculating ddCT from raw CT files.

Install required packages first using the pcrpy.yml file.


This code will take qPCR CTs stored in .xls files and normalized them to get the ddCT values (normalized fold change) and store it in a new .csv file


CTs values are obtain from the qPCR machine directly. It's the number of cycle the PCR reaction did to obtain a fluorescence superior to the background level.

dCTs are obtain by doing the normalisation between your treated CT and the control CT.

ddCTs are obtain by doing the normalisation between the dCT of your sample and the dCT of your housekeeping gene.


You should be able to run this code using the different examples datas, and always using 18S as the housekeeping gene.



How to run : 
First you need to set up your files
'''
assay_files = [r"path to your file]
normaliser_files = [r"path to your file"]
'''
