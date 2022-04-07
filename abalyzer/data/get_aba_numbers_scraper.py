# Generates list of ABA numbers from bank-code.net website
# https://python.plainenglish.io/send-http-requests-as-fast-as-possible-in-python-304134d46604
# https://usbanksdirectory.com/routing-numbers/

# Import libraries
import csv
import pandas as pd
import time
import re
import asyncio
import aiohttp
from aiohttp.client import ClientSession

open('temp/unchecked_aba_lookup_table.csv', 'w')

headerList = ['aba_number', 'address', 'state', 'phone_number', 'bank']   # adding header

# open CSV file and assign header
with open("temp/unchecked_aba_lookup_table.csv", 'w') as file:
    dw = csv.DictWriter(file, delimiter=',',
                        fieldnames=headerList)
    dw.writeheader()

async def parse_website(url:str, start:float, session:ClientSession):
    async with session.get(url) as response:

        time_since_start = time.time() - start

        page = await response.text()

        table = pd.read_html(page, index_col=0)  # aba table parsed from
        table_df = pd.DataFrame(table[0])

        bank_name = table_df.iat[0,0]
        bank_name = re.search('(([A-Z][A-Z]*)\s)*', bank_name)
        bank_name = bank_name.group(0)
        table_df = table_df[2:]
        table_df.insert(3, '', bank_name)


        table_df.to_csv('temp/unchecked_aba_lookup_table.csv', mode='a', index=True, header=False)

        print(f"T+{'%.2f'%time_since_start} {url}")


async def parse_all_websites(urls:str, start:float):
    my_conn = aiohttp.TCPConnector(limit=10)
    async with aiohttp.ClientSession(connector=my_conn) as session:
        tasks = []
        for url in urls:
            task = asyncio.ensure_future(parse_website(url=url, start=start, session=session))
            tasks.append(task)
        await asyncio.gather(*tasks,return_exceptions=True)   # the await must be nest inside of the session

websites_list = pd.read_csv (r'temp/websites_list.csv')
websites_list = websites_list.iloc[:,1]
# final_list = pandas.DataFrame()

start = time.time()
asyncio.run(parse_all_websites(websites_list, start))
end = time.time()
print(f'Logged {len(websites_list)} website tables in {end - start} seconds')