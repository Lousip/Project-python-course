# Project-python-course

A python code for calculating ddCT from raw CT files.

Install required packages first using the pcrpy.yml file.


This code will take qPCR CTs stored in .xls files and normalized them to get the ddCT values (normalized fold change) and store it in a new .csv file


CTs values are obtain from the qPCR machine directly. It's the number of cycle the PCR reaction did to obtain a fluorescence superior to the background level.

dCTs are obtain by doing the normalisation between your treated CT and the control CT.

ddCTs are obtain by doing the normalisation between the dCT of your sample and the dCT of your housekeeping gene.


You should be able to run this code using the different examples datas, and always using 18S as the housekeeping gene.



How to run : 
First you need to set up your files pathways

```
assay_files = [r"C:\Users\your_file_assay"]
normaliser_files = [r"C:\Users\your_file_normaliser"]
```

Then you need to put your file in a string
```
assays = qpcr.read(assay_files)
normalisers = qpcr.read(normaliser_files)
```

To be able to read the variable with the qpcr package : 
```
reader = qpcr.DataReader()

assays = reader.read(assay_files)
normalisers = reader.read(normaliser_files)
```

To calculate the delta CT of the ass
```
assays = qpcr.delta_ct(assays)
normalisers = qpcr.delta_ct(normalisers)
```

Now that you have your delta CT you need the deltadeltaCT which is the normalisation of your assay to the normaliser
```
results = qpcr.normalise(assays, normalisers)
```

The qpcr package allows to plot the ddCT values
```
fig = results.preview()
```
Using 12S as assay and 18S as normaliser you should have this figure
![image](https://github.com/Lousip/Project-python-course-LL/assets/144322022/6b532969-8cad-4ca9-bfe2-86678293ce06)


Finally you want to export your data in a new .txt file
Enter the names of your assay and normaliser
```
nameassay = input("name gene assay: ")
namenorm = input("name gene normaliser: ")
```
Export in csv
```
results_csv = [results]

name.csv = namearrays + "ddct" + namenorm + ".csv"
with open (name.csv,'w',newline = '') as csvfile:
    my_writer = csv.writer(csvfile, delimiter = ' ')
    my_writer.writerows(results_csv)
```
