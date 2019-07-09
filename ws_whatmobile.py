import csv
import pandas as pd
import requests
from bs4 import BeautifulSoup

mobile_list = ["Oppo_Reno-10X-Zoom", "Samsung_Galaxy-A70", "Realme_3-Pro", "Huawei_Y9-Prime-2019", "Vivo_Y15",
               "Honor_8S",
               "Oppo_Reno", "Samsung_Galaxy-S10-Plus-512GB", "Vivo_V15-Pro", "Oppo_F11-Pro", "Samsung_Galaxy-A50",
               "Huawei_P30-Pro",
               "Oppo_F11-Pro-64GB", "Vivo_V15", "Realme_2-Pro", "Samsung_Galaxy-A30", "Nokia_7.1",
               "Realme_3-Pro-6GB", "Vivo_Y17", "Honor_7X-4GB", "Huawei_P30-Lite", "Oppo_F11", "Samsung_Galaxy-A20",
               "Nokia_3.2-32GB", "Infinix_S4", "Oppo_A5s-4GB", "Realme_C2", "Realme_3-4GB", "Tecno_Camon-i4-4GB",
               "Infinix_Smart-3", "Nokia_2.2", "Infinix_Hot-6-Pro-3GB", "Tecno_Camon-iSky-3", "Infinix_Smart-3-Plus",
               "Huawei_Y5-2019",
               "Qmobile_QSmart-LT200", "Tecno_Pop-2", "Qmobile_i8i-2019", "Qmobile_i5i-2019", "Qmobile_QSmart-LT950",
               "Qmobile_QSmart-LT900"]

th_done = False
for mobile in mobile_list:
    url = "https://www.whatmobile.com.pk/{}".format(mobile)
    response = requests.get(url)
    html = response.content
    soup = BeautifulSoup(html, 'html.parser')
    table = soup.find('table', class_='specs')

    # Extracting Table Headings
    if th_done == False:

        th_list = ['Mobile_Name']
        for row in table.findAll('tr'):

            for cell in row.findAll('th', class_='hdngArial specs-subHeading RowBG1 bottom-border'):
                th_text = cell.text.replace('&nbsp', '')
                th_text = cell.text.replace('\n', '')
                th_text = cell.text.strip()
                th_list.append(th_text)

            for last_th in row.findAll('th', class_='hdngArial specs-subHeading RowBG1 bottom-border-section'):
                th_text1 = last_th.text.replace('&nbsp', '')
                th_text1 = last_th.text.replace('\n', '')
                th_text1 = last_th.text.strip()
                th_list.append(th_text1)

        with open("mobile-detail.csv", "a") as f:
            table_heading = ""
            for heading in th_list:
                if heading != th_list[len(th_list) - 2]:
                    table_heading += heading + " , "
                else:
                    table_heading += heading
            print(table_heading)
            f.write(table_heading + '\n')

        th_done = True

    specs_list = []
    mobile_name_container = soup.find('h1', class_='hdng3')
    mob_name = mobile_name_container.text
    specs_list.append(mob_name)

    for row in table.find_all('tr'):
        #     specs_list =[]
        #         new_list =[]
        for cell in row.find_all('td', class_='fasla RowBG1 specs-value bottom-border'):
            text = cell.text.replace('&nbsp', '')
            text = cell.text.replace('\n', '')
            text = cell.text.replace(',', '|')
            trim_text = '|'.join(text.split(','))
            trim_text = trim_text.strip()

            specs_list.append(trim_text)

        #         specs_list.append(text)
        #         print(specs_list)

        for sub_head in row.findAll('td', class_='fasla specs-value bottom-border'):
            text1 = sub_head.text.replace('&nbsp', '')
            text1 = sub_head.text.replace('\n', '')
            text1 = sub_head.text.replace(',', '|')

            trim_text1 = '|'.join(text1.split(','))

            trim_text1 = trim_text1.strip()
            #         print(trim_text1)

            specs_list.append(trim_text1)

        #         specs_list.append(text1)

        for border_head in row.findAll('td', class_='fasla specs-value bottom-border-section'):
            text2 = border_head.text.replace('&nbsp', '')
            text2 = border_head.text.replace('\n', '')
            text2 = border_head.text.replace(',', '|')
            trim_text2 = '|'.join(text2.split(','))
            trim_text2 = trim_text2.strip()
            #             print(trim_text2)
            specs_list.append(trim_text2)

    with open("mobile-detail.csv", "a") as f:

        #         table_heading = ""
        #         for heading in th_list:
        #             if heading != th_list[len(th_list)-2]:
        #                 table_heading += heading +" , "
        #             else:
        #                 table_heading += heading

        #         print(table_heading)
        #         f.write(table_heading)

        table_specs = ""

        for spec_details in specs_list:
            if spec_details != specs_list[len(specs_list) - 1]:
                table_specs += spec_details + " , "
            else:
                table_specs += spec_details

        print(table_specs)
        #         f.write("\n")
        f.write(table_specs + '\n')
