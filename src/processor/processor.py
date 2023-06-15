import asyncio
import aiohttp
from bs4 import BeautifulSoup

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


async def extract_details(links):
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
