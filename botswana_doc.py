import docx2txt
import re
import pandas as pd

text = docx2txt.process('./assets/botswana_doc.docx')
text_list = text.splitlines() #splits read text into list with white spaces


cummulative_tests_count = 0
cummulative_death_count = 0

read_tests = False
read_deaths = False

attributes_container = []

for line in text_list:
    #Do not process if line is empty
    if not len(line.split()) > 0:
        continue

    #Get count
    if read_tests:
        compact_line = line.replace(" ", "").replace(",", "")
        number = re.findall('[0-9]+', compact_line)
        if len(number) > 0:
            cummulative_tests_count = number[0]
            continue

    #Set true to read next line as the count
    if 'Cummulative tests performed' in line:
        read_tests = True
    else:
        read_tests = False

    #Read line to get number of deaths
    if 'cumulative deaths' in line:
        compact_line = line.replace(" ", "").replace(",", "")
        number = re.findall('[0-9]+', compact_line)
        if len(number) > 0:
            cummulative_death_count = number[0]

attributes_container.append([cummulative_tests_count, cummulative_death_count])

df = pd.DataFrame(attributes_container, columns=["Cummulative Tests", "Cummulative Deaths"])

df.to_csv('downloads/botswana_word.csv', index=False)







