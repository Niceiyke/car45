import asyncio
import aiohttp
import pandas as pd
from bs4 import BeautifulSoup
import time 

urls='https://www.cars45.com/listing'
pages=range(1,134)

def make_links(url=urls,p=pages):
     links=[]
     for page in p:
         links.append(f'{url}?page={page}')    
     return links


async def get_deatil(session,link):
          async with session.get(link) as p:
            return await p.text()


async def get_all_details(session,links):
     tasks=[]
     for link in links:
          task=asyncio.create_task(get_deatil(session=session,link=link))
          tasks.append(task)
     results=await asyncio.gather(*tasks)
     return results


async def main(links):
       async with aiohttp.ClientSession() as session:
              data=await get_all_details(session=session, links=links)
              return data
       
async def main1(links):
       async with aiohttp.ClientSession() as session:
              data=await get_all_details(session=session, links=links)
              return data

def parse_link(html):
    car_links=[]
    for i in range(len(html)):
        soup=BeautifulSoup(html[i],'html.parser')
        cars=soup.find_all('a',class_="car-feature car-feature--wide-mobile")
        [car_links.append(f"https://www.cars45.com{car['href']}" )for car in cars]
    return car_links

def parser(html):
    items=[]
    for i in html:
        item=[]
        try:
            soup=BeautifulSoup(i,'html.parser')
            info=soup.find('div',class_='details-grid grid')
            state=info.find('p',class_='main-details__region').text.strip().split(',')[0]
            item.append(state)
            price=info.find('h5',class_='main-details__name__price').text.strip().replace('₦','').replace(',','').strip()
            item.append(price)
            name=info.find('h1',class_='main-details__name__title').text.strip()
            item.append(name)
            r=info.find_all('span',class_='tab-content__svg__title')
            if len(r)>2:
                r.pop(0)
                fuel_type=r[0].text.strip()
                transmission=r[1].text.strip()
            else:
                fuel_type=r[0].text.strip()
                transmission=r[1].text.strip()
            item.append(fuel_type)
            item.append(transmission)
            info=soup.find('div',class_='tab-content')
            r=info.find('div',class_='general-info grid')
            features=r.find_all('div')
            c=[feature.text.strip().split('\n') for feature in features][:-2]
            for a in c:
                
                if 'Make' in a[1] :
                    item.append(a[0])
                if 'Model' in a[1] :
                    item.append(a[0])
                if 'Condition' in a[1] :
                    item.append(a[0])

                if 'Year of manufacture' in a[1] :
                    item.append(a[0])
                if 'Mileage' in a[1] :
                    item.append(a[0])
                if 'Engine Size' in a[1] :
                    item.append(a[0])
            items.append(item)
        except Exception as e:
             print(e)
    return items
        

if __name__=="__main__":
    start_time=time.time()
    links=make_links()
    end_time=time.time()
    print(f'finished link scraping at:{end_time-start_time :0.4f} seconds')
    result=asyncio.run(main(links=links))
    print("*"*35)
    print(f'finished first detail scraping at:{end_time-start_time :0.4f} seconds')
    item=parse_link(html=result)
    items=asyncio.run(main(links=item))
    print("#"*35)
    end_time=time.time()
    print(f'finished detail scraping at:{end_time-start_time :0.4f} seconds')
    data=parser(html=items)
    columns=['state','price','name','fuel_type','transmmision','make','model','year','condition','millage','engine_size']
    df=pd.DataFrame(data,columns=columns)
    df.to_csv('car.csv',index=False)
    end_time=time.time()
    print(f'finished at:{end_time-start_time :0.4f} seconds')

    
  