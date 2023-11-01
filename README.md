# Project-python-course

A python code for calculating ddCT from raw CT files.

Install required packages first using the pcrpy.yml file.


This code will take qPCR CTs stored in .xls files and normalized them to get the ddCT values (normalized fold change) and store it in a new .csv file


CTs values are obtain from the qPCR machine directly. It's the number of cycle the PCR reaction did to obtain a fluorescence superior to the background level.

dCTs are obtain by doing the normalisation between your treated CT and the control CT.

ddCTs are obtain by doing the normalisation between the dCT of your sample and the dCT of your housekeeping gene.


You should be able to run this code using the different examples datas, and always using 18S as the housekeeping gene.



## **How to start:**

Dowload the PPPcr.py file and pcrpy.yml environment

First you need to set up your files pathways

```
assay_files = [r"C:\Users\your_file_assay"]
normaliser_files = [r"C:\Users\your_file_normaliser"]
```


If you run using 12S as assay and 18S as normaliser you should have this figure
![image](https://github.com/Lousip/Project-python-course-LL/assets/144322022/6b532969-8cad-4ca9-bfe2-86678293ce06)

And when you export to a csv file
Enter the names of your assay and normaliser in the input
You end upwith a csv file named after your assay and normaliser
