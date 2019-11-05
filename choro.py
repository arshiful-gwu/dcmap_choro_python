#http://jsonviewer.stack.hu/

import pandas as pd
import folium
import os
import numpy as np
import json

with open('dc2.json') as f:
    clusters=json.load(f)

#clusters=os.path.join('dc2.json')
income=os.path.join('data.csv')
income_data=pd.read_csv(income)

dcmap=folium.Map(location=[39,-77], zoom_start=11)
folium.Choropleth(
    geo_data=clusters,
    name='Choropleth',
    data=income_data,
    columns=['Clusters','Income'],
    key_on='feature.properties.NAME',
    fill_color='YlGn',
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name='Income').add_to(dcmap)

folium.LayerControl().add_to(dcmap)

dcmap.save('dc-income.html')

#.save('dc-income.html')





