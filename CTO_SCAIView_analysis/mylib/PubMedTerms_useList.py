#!/usr/bin/env python
# coding: utf-8

# In[1]:


'''
this code is for retrieve all the desired PubMed Format elements: PMID, PT, OT, MH from a list of PMIDs by 
using the webpage https://pubmed.ncbi.nlm.nih.gov/32790733/?format=pubmed 
The input list is a result from SCAIView output back end file
 '''

import pandas as pd
import requests
from bs4 import BeautifulSoup


# In[2]:


#1. obtain a unique list of PMIDs, because one PMID may link to multiple Clinical Trial IDs.
def PMID_input(file):
    """
    Get the input NCTID as a list
    :param file
    :return the list
    """
    PMID_list = []
    filepath = "input\\"+file
    df = pd.read_csv(filepath, sep = '\t', header = 0)
    print("The "+file+" contains "+str(df.shape[0])+" rows in total.")
    PMID_list = df['PMID'].dropna().tolist()
    print("There are "+str(len(PMID_list))+" rows with PMID.")
    PMID_list_uni= list(set(PMID_list))
    print("There are "+str(len(PMID_list_uni))+" unique PMIDs.")
    return PMID_list_uni


# In[3]:


SCAIviewfile = input('Please give the file name contains PMID list:' )
PMID_list_uni = PMID_input(SCAIviewfile)


# In[8]:


#2. for each PMID in list, find the PMID, PT, OT and MH info from web and save to a dataframe

def page_content_body(URL):
    '''give an URL, will return the text of the body tag'''
    response = requests.get(URL)
    page = response.text
    soup = BeautifulSoup(page)
    content = soup.body.find('div', attrs={'class':'article-page'}).text
    return content

def create_new_row(content):
    '''give the content of page body. Creat a new row for the dataframe
       a new row includes PMID, PT, OT, MH, GR,SI, TI data extracted from the page'''
    content_list = content.splitlines()
    PT_list = []
    OT_list = []
    MH_list = []
    GR_list = []
    SI_list = []
    for line in content_list:
        if line.startswith('PMID'):
            PMID = line.replace(r'PMID','').replace('-','').lstrip()
        if line.startswith('TI'):
            TI = line.replace(r'TI  - ','')
        if line.startswith('PT'):
            PT = line.replace(r'PT','').replace('-','').lstrip()
            PT_list.append(PT)
        if line.startswith('OT'):
            OT = line.replace(r'OT','').replace('-','').lstrip()
            OT_list.append(OT)
        if line.startswith('MH'):
            MH = line.replace(r'MH','').replace('-','').lstrip()
            MH_list.append(MH)
        if line.startswith('GR'):
            GR = line.replace(r'GR','').replace('-','').lstrip()
            GR_list.append(GR)
        if line.startswith('SI'):
            SI = line.replace(r'SI','').replace('-','').lstrip()
            SI_list.append(SI)

    PT_list_str = ';'.join(PT_list)
    OT_list_str = ';'.join(OT_list)
    MH_list_str = ';'.join(MH_list)
    GR_list_str = ';'.join(GR_list)
    SI_list_str = ';'.join(SI_list)

    new_row = {'PMID':PMID, 'PT':PT_list_str, 'OT':OT_list_str, 'MH':MH_list_str, 'SI':SI_list_str, 'TI':TI,'GR':GR_list_str}
    return new_row
    
Base_URL = "https://pubmed.ncbi.nlm.nih.gov/"
PM_terms_df = pd.DataFrame(columns = ['PMID', 'PT', 'OT','MH','SI','TI','GR'])

for x in range(len(PMID_list_uni)):
    PMID = str(PMID_list_uni[x].replace('PMID:',''))
    pagelink = Base_URL+PMID+"//?format=pubmed"
    print("processing "+pagelink+"...")
    content = page_content_body(pagelink)
    new_row = create_new_row(content)
    print(new_row)
    PM_terms_df = PM_terms_df.append(new_row, ignore_index=True)
    n=x+1
    print(str(n)+" row added!")






