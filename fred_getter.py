import requests
import time
import warnings
import pandas as pd
from urllib3.exceptions import InsecureRequestWarning
from config import user_agent, myAPIkey, response_method

import ssl
ssl._create_default_https_context = ssl._create_unverified_context

warnings.filterwarnings("ignore", category=InsecureRequestWarning, module="urllib3")

def getSeriesInfo(series_id):
    url=f'https://api.stlouisfed.org/fred/series?series_id={series_id}&api_key={myAPIkey}&file_type={response_method}'
    headers = {'User-Agent': user_agent}
    response = requests.get(url, headers=headers, verify=False)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        return None

def getObservations(series_id):
    url = f'https://api.stlouisfed.org/fred/series/observations?series_id={series_id}&api_key={myAPIkey}&file_type={response_method}'
    headers = {'User-Agent': user_agent}
    response = requests.get(url, headers=headers, verify=False)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        return None

def getCategoryBySeriesId(series_id):
    url = f'https://api.stlouisfed.org/fred/series/categories?series_id={series_id}&api_key={myAPIkey}&file_type={response_method}'
    headers = {'User-Agent': user_agent}
    response = requests.get(url, headers=headers, verify=False)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        return None

def getSereisIds(category_id):
    url = f'https://api.stlouisfed.org/fred/category/series?category_id={category_id}&api_key={myAPIkey}&file_type={response_method}'
    headers = {'User-Agent': user_agent}
    response = requests.get(url, headers=headers, verify=False)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        return None

def getCategoryByCategoryId(category_id):
    url = f'https://api.stlouisfed.org/fred/category?category_id={category_id}&api_key={myAPIkey}&file_type={response_method}'
    headers = {'User-Agent': user_agent}
    response = requests.get(url, headers=headers, verify=False)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        return None

def getRelatedCategoriesByCategoryId(category_id):
    url=f'https://api.stlouisfed.org/fred/category/related?category_id={category_id}&api_key={myAPIkey}&file_type={response_method}'
    headers = {'User-Agent': user_agent}
    response = requests.get(url, headers=headers, verify=False)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        return None


