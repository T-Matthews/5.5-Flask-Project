from app import app
from flask import render_template
from .services import getRegions #allows us to pass info over to the 
import requests as r

@app.route('/')
def home():
    text = 'Hello World'
    return render_template('index.html',text = text)

@app.route('/regions')
def regions():
    context = getRegions()
    regionlist = []
    locations_list=[]
    for k,v in context.items():
        regionlist.append(k.title())
        locations_list.append(v['places'])


    return render_template('regions.html',regionlist = regionlist,locations_list = locations_list)

