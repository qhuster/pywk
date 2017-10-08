from src import urls
import json
from src import api
import requests
import pymysql


def get_hero_small_img(heroname):
    return urls.BASE_HERO_IMAGES_URL + heroname.replace('npc_dota_hero_', '') + '_sb.png'


def get_hero_large_img(heroname):
    return urls.BASE_HERO_IMAGES_URL + heroname.replace('npc_dota_hero_', '') + '_lg.png'


def get_hero_full_img(heroname):
    return urls.BASE_HERO_IMAGES_URL + heroname.replace('npc_dota_hero_', '') + '_full.png'


def get_hero_vert_img(heroname):
    return urls.BASE_HERO_IMAGES_URL + heroname.replace('npc_dota_hero_', '') + '_vert.jpg'


def get_item_img(itemname):
    return urls.BASE_ITEMS_IMAGES_URL + itemname.replace('item_', '') + '_lg.png'


def download_heros_img():
    with open('..\\ref\\heroes.json', 'w') as fp:
        do = api.dota2py()
        do.init_key('39059503CFC8B0D8ADF685871CA0C00D')
        heros = do.get_heroes()
        for hero in heros:
            heroname = hero['name']
            hero['url_small_portrait'] = get_hero_small_img(heroname)
            with open('..\\imgs\\heroes\\small\\' + heroname + '_sb.png', 'wb') as f:
                f.write(requests.get(hero['url_small_portrait']).content)
            hero['url_large_portrait'] = get_hero_large_img(heroname)
            with open('..\\imgs\\heroes\\large\\' + heroname + '_lg.png', 'wb') as f:
                f.write(requests.get(hero['url_large_portrait']).content)
            hero['url_full_portrait'] = get_hero_full_img(heroname)
            with open('..\\imgs\\heroes\\full\\' + heroname + '_full.png', 'wb') as f:
                f.write(requests.get(hero['url_full_portrait']).content)
            hero['url_vertical_portrait'] = get_hero_vert_img(heroname)
            with open('..\\imgs\\heroes\\vertical\\' + heroname + '_vert.jpg', 'wb') as f:
                f.write(requests.get(hero['url_vertical_portrait']).content)
        json.dump(heros, fp, sort_keys=lambda h:h['id'], indent=4)


def save_heroes():
    with open('..\\ref\\heroes.json', 'w') as fp:
        do = api.dota2py()
        do.init_key('39059503CFC8B0D8ADF685871CA0C00D')
        heros = do.get_heroes()
        for hero in heros:
            heroname = hero['name']
            hero['url_large_portrait'] = get_hero_small_img(heroname)
            hero['url_large_portrait'] = get_hero_large_img(heroname)
            hero['url_full_portrait'] = get_hero_full_img(heroname)
            hero['url_vertical_portrait'] = get_hero_vert_img(heroname)
        json.dump(heros, fp, sort_keys=lambda h:h['id'], indent=4)


def save_items():
    with open('..\\ref\\items.json', 'w') as fp:
        do = api.dota2py()
        do.init_key('39059503CFC8B0D8ADF685871CA0C00D')
        items = do.get_items()
        for item in items:
            itemname = item['name']
            item['url_img'] = get_item_img(itemname)

        json.dump(items, fp, sort_keys=lambda i:i['id'], indent=4)


def download_items_img():
    with open('..\\ref\\items.json', 'w') as fp:
        do = api.dota2py()
        do.init_key('39059503CFC8B0D8ADF685871CA0C00D')
        items = do.get_items()
        for item in items:
            itemname = item['name']
            item['url_img'] = get_item_img(itemname)
            with open('..\\imgs\\items\\large\\' + itemname + '_lg.png', 'wb') as f:
                f.write(requests.get(item['url_img']).content)

        json.dump(items, fp, sort_keys=lambda i:i['id'], indent=4)


download_heros_img()
download_items_img()
