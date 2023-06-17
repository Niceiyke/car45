from bs4 import BeautifulSoup
from src.processor.database import save_to_db
import pandas as pd

def parser(html):
    items=[]
    for i in html:
        try:
            soup=BeautifulSoup(i,'html.parser')
            info=soup.find('div',class_='details-grid grid')
            state=info.find('p',class_='main-details__region').text.strip().split(',')[0]
            price=float(info.find('h5',class_='main-details__name__price').text.strip().replace('₦','').replace(',','').strip())
            name=info.find('h1',class_='main-details__name__title').text.strip()
            r=info.find_all('span',class_='tab-content__svg__title')
            if len(r)>2:
                r.pop(0)
                fuel_type=r[0].text.strip()
                transmission=r[1].text.strip()
            else:
                fuel_type=r[0].text.strip()
                transmission=r[1].text.strip()
            info=soup.find('div',class_='tab-content')
            r=info.find('div',class_='general-info grid')
            features=r.find_all('div')
            c=[feature.text.strip().split('\n') for feature in features][:-2]
            for a in c:
                
                if 'Make' in a[1] :
                    make=(a[0])
                if 'Model' in a[1] :
                    model=a[0]
                if 'Condition' in a[1] :
                    condition=a[0]
                if 'Year of manufacture' in a[1] :
                    year=int(a[0])
                if 'Mileage' in a[1] :
                    mileage=float(a[0])
                if 'Engine Size' in a[1] :
                    engine_size=int(a[0])
            item=(state,price,name,fuel_type,transmission,make,model,year,condition,mileage,engine_size)
            items.append(item)
        except Exception as e:
             print(f'error{e}')

    save_to_db(item=items)

    columns=['state','price','name','fuel_type','transmission','make','model','year','condition','mileage','engine_size']
    df=pd.DataFrame(items,columns=columns)
    df.to_csv('./car45.csv')
    return
        

