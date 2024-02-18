# scary-webmd
Search ClinVar Like It's WebMD! A hypochondriac's nightmare!

WebMD is scary. You search for advice on a small red bump you found on your foot and it says you might have cancer or some super rare disease. Wouldn't it be better to scare yourself medically by using peer-reveiwed research?! With this, you can find clinically relevant publications associated with whatever vague symptoms you have. 

Requires: Python 3.X, [entrez direct](https://www.ncbi.nlm.nih.gov/books/NBK179288/), [BeautifulSoup](https://pypi.org/project/beautifulsoup4/)

Your query is searched on [ClinVar](https://www.ncbi.nlm.nih.gov/clinvar/intro), an NIH database holding genetic variants associated with some disease and/or drug response. Results are parsed for publications with some association of your symptoms.

The class calls all it's functions in a chain:
![scary-webmd-methods-flow](https://github.com/StephenWist/scary-webmd/assets/18633285/7a7e01c8-7243-4656-a414-8833fd891952)

## This code was made for myself and by myself only. This code is not designed to provide medical advice, nor was produced by or with a medically licensed professional and should not be used in lieu of seeking professional medical attention. 
