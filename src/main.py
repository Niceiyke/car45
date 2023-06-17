import asyncio
import time 
from src.processor.processor import make_links,parse_link,extract_details
from processor.parser_html import parser


if __name__=="__main__":
    start_time=time.time()

    links=make_links()

    result=asyncio.run(extract_details(links=links))

    item=parse_link(html=result)

    items=asyncio.run(extract_details(links=item))

    parser(html=items)

    end_time=time.time()

    print(f'finished at:{end_time-start_time :0.4f} seconds')

    
  