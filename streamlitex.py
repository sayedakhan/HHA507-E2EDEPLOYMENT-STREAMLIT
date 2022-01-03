#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  3 17:59:38 2022

@author: sayedakhan
"""

import streamlit as st
import pandas as pd
import numpy as np

st.title('CMS - Hospital Data')

df = pd.read_csv('https://raw.githubusercontent.com/hantswilliams/AHI_DataSci_507/main/Deployment_Streamlit/outpatient_2015.csv')


st.dataframe(df)

