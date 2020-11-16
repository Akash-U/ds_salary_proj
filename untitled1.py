# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 19:38:22 2020

@author: Akash
"""

import glassdoor_scaper as gs
import pandas as pd
path = "C:/Users/Akash/Documents/ds_salary_proj/chromedriver"

df = gs.get_jobs('data scientist',15, False, path, 15)