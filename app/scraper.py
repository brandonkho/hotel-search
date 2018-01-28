import requests
from multiprocessing import Pool
from heapq import heappush, heappop, heapify

SCRAPER_URL = 'http://localhost:9000/scrapers/'


'''
use multiprocessing to get sites in parallel
'''
def search():
    sites =['Expedia','Orbitz','Travelocity','Priceline','Hilton']
    pool = Pool(len(sites))
    results = pool.map(get_data, sites)
    pool.close()
    pool.join()
    
    return merge(results)
    

def get_data(site):
    url = SCRAPER_URL + site
    response = requests.get(url)
    response_json = response.json()
    search_results = response_json['results']

    return search_results



'''
use heap to merge the sorted list
on each iteration we pop off the "min" (which is really the max because we multiplied by -1)
then we add the next element of the same list
runtime complexity is O(n logk) where n is the number of elements and k is the number of providers

'''
def merge(results):
    sorted_results = []

    pq = [(-row[0]['ecstasy'], i, 0) for i, row in enumerate(results)]
    heapify(pq)

    while pq:
        val, i, j = heappop(pq)
        
        sorted_results.append(results[i][j])
        if j + 1 == len(results[i]):
            continue
        ecstasy = results[i][j+1]['ecstasy']
        heappush(pq, (-ecstasy, i, j+1))

    return sorted_results

