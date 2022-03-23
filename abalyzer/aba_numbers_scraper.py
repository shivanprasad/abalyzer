# Import libraries
import pandas as pd
import cloudscraper
from bs4 import BeautifulSoup
import time
import re

websites_list = [
"https://bank-code.net/routing-numbers/bank/first-national-bank",
"https://bank-code.net/routing-numbers/bank/first-national-bank/100",
"https://bank-code.net/routing-numbers/bank/bank-of-america%2c-n.a.",
"https://bank-code.net/routing-numbers/bank/bank-of-america%2C-n.a./100",
"https://bank-code.net/routing-numbers/bank/first-state-bank",
"https://bank-code.net/routing-numbers/bank/wells-fargo-bank",
"https://bank-code.net/routing-numbers/bank/prosperity-bank",
"https://bank-code.net/routing-numbers/bank/fifth-third-bank",
"https://bank-code.net/routing-numbers/bank/capital-one%2c-n.a.",
"https://bank-code.net/routing-numbers/bank/bmo-harris-bank%2cn.a.",
"https://bank-code.net/routing-numbers/bank/pnc-bank%2c-na",
"https://bank-code.net/routing-numbers/bank/first-financial-bank",
"https://bank-code.net/routing-numbers/bank/jpmorgan-chase",
"https://bank-code.net/routing-numbers/bank/centennial-bank",
"https://bank-code.net/routing-numbers/bank/renasant-bank",
"https://bank-code.net/routing-numbers/bank/synovus-bank",
"https://bank-code.net/routing-numbers/bank/first-national-bank-of-pennsylvania",
"https://bank-code.net/routing-numbers/bank/iberiabank",
"https://bank-code.net/routing-numbers/bank/bank-ozk",
"https://bank-code.net/routing-numbers/bank/united-bank",
"https://bank-code.net/routing-numbers/bank/us-bank-na",
"https://bank-code.net/routing-numbers/bank/farmers-state-bank",
"https://bank-code.net/routing-numbers/bank/citizens-state-bank",
"https://bank-code.net/routing-numbers/bank/regions-bank",
"https://bank-code.net/routing-numbers/bank/valley-national-bank",
"https://bank-code.net/routing-numbers/bank/bmo-harris-bank-na",
"https://bank-code.net/routing-numbers/bank/compass-bank",
"https://bank-code.net/routing-numbers/bank/branch-banking-%26-trust-company",
"https://bank-code.net/routing-numbers/bank/citizens-bank",
"https://bank-code.net/routing-numbers/bank/firstbank",
"https://bank-code.net/routing-numbers/bank/banner-bank",
"https://bank-code.net/routing-numbers/bank/peoples-bank",
"https://bank-code.net/routing-numbers/bank/pinnacle-bank",
"https://bank-code.net/routing-numbers/bank/south-state-bank",
"https://bank-code.net/routing-numbers/bank/ameris-bank",
"https://bank-code.net/routing-numbers/bank/bmo-harris-bank%2c-n.a",
"https://bank-code.net/routing-numbers/bank/first-bank",
"https://bank-code.net/routing-numbers/bank/m-%26-t-bank",
"https://bank-code.net/routing-numbers/bank/umpqua-bank",
"https://bank-code.net/routing-numbers/bank/bank-of-america-n.a.",
"https://bank-code.net/routing-numbers/bank/first-tennessee-bank-natl-assn",
"https://bank-code.net/routing-numbers/bank/key-bank",
"https://bank-code.net/routing-numbers/bank/pacific-premier-bank",
"https://bank-code.net/routing-numbers/bank/people%27s-united-bank%2c-n.a.",
"https://bank-code.net/routing-numbers/bank/columbia-state-bank",
"https://bank-code.net/routing-numbers/bank/union-bank-%26-trust",
"https://bank-code.net/routing-numbers/bank/mufg-union-bank%2c-n.a.",
"https://bank-code.net/routing-numbers/bank/security-state-bank",
"https://bank-code.net/routing-numbers/bank/nbh-bank",
"https://bank-code.net/routing-numbers/bank/pacific-western-bank",
"https://bank-code.net/routing-numbers/bank/pnc-bank%2c-national-association",
"https://bank-code.net/routing-numbers/bank/heritage-bank",
"https://bank-code.net/routing-numbers/bank/citizens-business-bank",
"https://bank-code.net/routing-numbers/bank/citizens-national-bank",
"https://bank-code.net/routing-numbers/bank/east-west-bank",
"https://bank-code.net/routing-numbers/bank/huntington-national-bank",
"https://bank-code.net/routing-numbers/bank/td-bank-na",
"https://bank-code.net/routing-numbers/bank/farmers-%26-merchants-bank",
"https://bank-code.net/routing-numbers/bank/independent-bank",
"https://bank-code.net/routing-numbers/bank/new-york-community-bank",
"https://bank-code.net/routing-numbers/bank/trustmark-national-bank",
"https://bank-code.net/routing-numbers/bank/united-community-bank",
"https://bank-code.net/routing-numbers/bank/bank-of-america",
"https://bank-code.net/routing-numbers/bank/bank-of-new-york-mellon",
"https://bank-code.net/routing-numbers/bank/hancock-whitney-bank",
"https://bank-code.net/routing-numbers/bank/santander-bank",
"https://bank-code.net/routing-numbers/bank/wells-fargo-bank-na",
"https://bank-code.net/routing-numbers/bank/cornerstone-bank",
"https://bank-code.net/routing-numbers/bank/eastern-bank",
"https://bank-code.net/routing-numbers/bank/first-community-bank",
"https://bank-code.net/routing-numbers/bank/international-bank-of-commerce",
"https://bank-code.net/routing-numbers/bank/peoples-state-bank",
"https://bank-code.net/routing-numbers/bank/pnc-bank-inc.-_-baltimore",
"https://bank-code.net/routing-numbers/bank/bank-of-the-west",
"https://bank-code.net/routing-numbers/bank/community-bank",
"https://bank-code.net/routing-numbers/bank/first-citizens-bank-%26-trust-company",
"https://bank-code.net/routing-numbers/bank/interbank",
"https://bank-code.net/routing-numbers/bank/umb%2c-na",
"https://bank-code.net/routing-numbers/bank/bank-of-hope",
"https://bank-code.net/routing-numbers/bank/arvest-bank",
"https://bank-code.net/routing-numbers/bank/busey-bank",
"https://bank-code.net/routing-numbers/bank/chemical-bank",
"https://bank-code.net/routing-numbers/bank/first-tennessee-bank",
"https://bank-code.net/routing-numbers/bank/glacier-bank",
"https://bank-code.net/routing-numbers/bank/keybank-national-association",
"https://bank-code.net/routing-numbers/bank/union-state-bank",
"https://bank-code.net/routing-numbers/bank/capital-city-bank",
"https://bank-code.net/routing-numbers/bank/first-national-bank-of-omaha",
"https://bank-code.net/routing-numbers/bank/park-national-bank",
"https://bank-code.net/routing-numbers/bank/simmons-first-natl-bk",
"https://bank-code.net/routing-numbers/bank/td-bank%2c-na",
"https://bank-code.net/routing-numbers/bank/united-community-bank%2c-inc",
"https://bank-code.net/routing-numbers/bank/bancorp-south",
"https://bank-code.net/routing-numbers/bank/bancorpsouth-bank",
"https://bank-code.net/routing-numbers/bank/byline-bank",
"https://bank-code.net/routing-numbers/bank/commerce-bank",
"https://bank-code.net/routing-numbers/bank/community-first-bank",
"https://bank-code.net/routing-numbers/bank/community-state-bank",
"https://bank-code.net/routing-numbers/bank/equity-bank",
"https://bank-code.net/routing-numbers/bank/federal-reserve-bank",
"https://bank-code.net/routing-numbers/bank/financial-partners-credit-union",
"https://bank-code.net/routing-numbers/bank/first-bank-%26-trust",
"https://bank-code.net/routing-numbers/bank/first-merchants-bank",
"https://bank-code.net/routing-numbers/bank/simmons-bank",
"https://bank-code.net/routing-numbers/bank/usalliance-federal-credit-union",
"https://bank-code.net/routing-numbers/bank/webster-bank",
"https://bank-code.net/routing-numbers/bank/berkshire-bank",
"https://bank-code.net/routing-numbers/bank/centerstate-bank%2c-national-associati",
"https://bank-code.net/routing-numbers/bank/citizens-bank-na",
"https://bank-code.net/routing-numbers/bank/city-national-bank",
"https://bank-code.net/routing-numbers/bank/commercial-bank",
"https://bank-code.net/routing-numbers/bank/great-southern-bank",
"https://bank-code.net/routing-numbers/bank/national-bank-of-commerce",
"https://bank-code.net/routing-numbers/bank/seacoast-national-bank",
"https://bank-code.net/routing-numbers/bank/cathay-bank",
"https://bank-code.net/routing-numbers/bank/citibank-na",
"https://bank-code.net/routing-numbers/bank/citibank-west",
"https://bank-code.net/routing-numbers/bank/community-first-credit-union",
"https://bank-code.net/routing-numbers/bank/credit-union-of-southern-california",
"https://bank-code.net/routing-numbers/bank/first-midwest-bank",
"https://bank-code.net/routing-numbers/bank/german-american-bank",
"https://bank-code.net/routing-numbers/bank/great-lakes-credit-union",
"https://bank-code.net/routing-numbers/bank/hsbc-bank%2c-usa",
"https://bank-code.net/routing-numbers/bank/m-b-financial-bank",
"https://bank-code.net/routing-numbers/bank/s-%26-t-bank",
"https://bank-code.net/routing-numbers/bank/simmons-first-national-bank",
"https://bank-code.net/routing-numbers/bank/sterling-national-bank",
"https://bank-code.net/routing-numbers/bank/unify-financial-federal-credit-union",
"https://bank-code.net/routing-numbers/bank/axos-bank",
"https://bank-code.net/routing-numbers/bank/bank-of-commerce",
"https://bank-code.net/routing-numbers/bank/cadence-bank%2c-n.a.",
"https://bank-code.net/routing-numbers/bank/camden-national-bank",
"https://bank-code.net/routing-numbers/bank/comerica-bank",
"https://bank-code.net/routing-numbers/bank/community-national-bank",
"https://bank-code.net/routing-numbers/bank/horizon-bk%2c-an-indiana-bank",
"https://bank-code.net/routing-numbers/bank/horizon-credit-union",
"https://bank-code.net/routing-numbers/bank/midland-states-bank",
"https://bank-code.net/routing-numbers/bank/tbk-bank%2c-ssb",
"https://bank-code.net/routing-numbers/bank/wesbanco-bank-inc",
"https://bank-code.net/routing-numbers/bank/banco-popular",
"https://bank-code.net/routing-numbers/bank/bancorpsouth",
"https://bank-code.net/routing-numbers/bank/bankplus",
"https://bank-code.net/routing-numbers/bank/central-bank",
"https://bank-code.net/routing-numbers/bank/cibc-bank-usa",
"https://bank-code.net/routing-numbers/bank/community-bank-of-ms",
"https://bank-code.net/routing-numbers/bank/farmers-bank",
"https://bank-code.net/routing-numbers/bank/fidelity-bank",
"https://bank-code.net/routing-numbers/bank/first-fidelity-bank",
"https://bank-code.net/routing-numbers/bank/first-financial-bank%2c-n.a.",
"https://bank-code.net/routing-numbers/bank/first-savings-bank",
"https://bank-code.net/routing-numbers/bank/old-national-bank",
"https://bank-code.net/routing-numbers/bank/pioneer-bank%2c-ssb",
]
aba_lookup_table = {'aba_number': [],
                    'address': [],
                    'city': [],
                    'state': [],
                    'bank_name': []
                    }

for website in websites_list[:1]:
    scraper = cloudscraper.create_scraper()  # returns a CloudScraper instance
    tries = 0
    url = website
    page = scraper.get(url)
    time.sleep(0.5)

    while tries < 15:
        scraper = cloudscraper.create_scraper()         # returns a CloudScraper instance
        page = scraper.get(url)

        if page.status_code != 200:
            tries = tries + 1
            print(f"*** The response for {url} is {page.status_code}")
            time.sleep(1)
        else:
            table = pd.read_html(page.text, index_col=0)         # aba table parsed from bank-code.net
            # del table[0]
            # print(table)
            table_df = pd.DataFrame(table[0])
            print(table_df.to_string())

            parsed_page = BeautifulSoup(page.text, features='lxml')
            bank_name = parsed_page.body.find('h1', attrs={'class': 'text-center'}).text
            bank_name = bank_name[:-18]         # bank name parsed from bank-code.net
            # print(table_df)

            # table = table.append(table_df.iloc[][])

            for row in range(len(table_df)):
                if len(str(table_df.iloc[row, 0])) != 99:
                    print(str(table_df.iloc[row, 0]))
                    aba_lookup_table['aba_number'].append(str(table_df.iloc[row, 0]))
                    aba_lookup_table['address'].append(str(table_df.iloc[row, 1]))
                    aba_lookup_table['city'].append(str(table_df.iloc[row, 2]))
                    aba_lookup_table['state'].append(str(table_df.iloc[row, 3]))
                    aba_lookup_table['bank_name'].append(bank_name)

            tries = 15
    if tries == 15 and len(aba_lookup_table) == 0:
        print("15 CONNECTIONS ATTEMPTED, POSSIBLE IP BAN, VISIT bank-code.net IN BROWSER, IF NOT BANNED RESTART SCRIPT")


# aba_lookup_table = pd.DataFrame(aba_lookup_table)
print(aba_lookup_table)
