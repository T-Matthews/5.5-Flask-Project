import requests as r
# class PRegion:
#     def __init__(self,region_data):
#         self.name = region_data['name'].title()
#         self.locations = region_data['places']
#         self.first = region_data['first']
#         self.last = region_data['last']


# class Pokemon:
#     def __init__(self,pokedex):
#         self.name = 

def getRegions():
    data = r.get('https://pokeapi.co/api/v2/region/')
    if data.status_code == 200:
        data = data.json()['results']
    else:
        return 'broken api'
    regionlist = {}
    names = []
    urls = []
    for x in data:
        cities = []
        names.append(x['name'])
        urls.append(x['url'])
        rdata = r.get(x['url']).json()
        for i in rdata['locations']:
            if 'city' in i['name'] or 'town' in i['name'] or 'island' in i['name']:
                cities.append(i['name'].replace('-',' ').title())
        
        dexdata = r.get(rdata['pokedexes'][0]['url']).json()
        pmin = r.get(dexdata['pokemon_entries'][0]['pokemon_species']['url']).json()['id']
        pmax = r.get(dexdata['pokemon_entries'][-1]['pokemon_species']['url']).json()['id']
    
        regionlist[x['name']] = {
                                'name':x['name'].title(),
                                'places':cities,
                                'first':pmin,
                                 'last':pmax
        }

    # for i in regionlist:
#     #     newRegion = PRegion(i)
#     print('Here is the regionlist', regionlist)
    return regionlist
# getRegions()

