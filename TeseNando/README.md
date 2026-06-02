Latex template for thesis of the Multimedia Masters (U.Porto)
=============================================================

This template is based on the MIEIC/MIEEC template provided by João Correia Lopes and João Canas Ferreira (v2012 / feupteses.sty v1.1).

Below you will find information regarding the structure of the template files/folders and the instructions for configuring and building the document

Files/Folders structure
-----------------------

The template is divided in folders, to separate the content of the thesis produced by the author from the supporting latex and auxiliary files.

Authors should focus on the following folders/files (in **bold** those that must be edited by the author):

+ **A_FrontMatter**
   - cover.tex: additional information for the cover (optional)
   - **abstract.tex**: the abstract
   - **acknowledgments.tex**:  the acknowledgments
   - quote.tex: initial quotation (optional)
   - **abbreviations.tex** the list of abbreviations used
   
+ **B_Chapters**
   - **_list.tex**: list of chapters (edit to include only the ones you need)
   - **chapter1.tex**, ..., **chapterN.tex**: your chapters
   
+ **C_Appendices**
   - **_list.tex**: list of appendices (edit to include only the ones you need)
   - **appendix1.tex**, ..., **appendixN.tex**: your appendices

+ **D_Figures**: 
   - here you should include your figures in *png* or *pdf* format; two sample figures are included)

+ **E_Bibliography**
   - *_list.tex*: list of bib files to include (edit if you need more than one; otherwise defaults to bibliography.bib)
   - **bibliography.bib**: your bibtex file containing the references


---
Instructions for configuring and building the document
------------------------------------------------------

+ The main file is "Thesis.tex"
+ Use "pdflatex", not "latex".
+ If building through the command line, use the common sequence

        pdflatex Thesis
        bibtex Thesis
        pdflatex Thesis
        pdflatex Thesis

+ For references in the format (author,date), the *plainnat.bst* file should be installed
+ To choose the character encoding used uncomment the correct *inputenc* package in the :

        \usepackage[latin1]{inputenc}   % latin
        \usepackage[utf8]{inputenc}     % utf8
        \usepackage[applemac]{inputenc} % Mac
