import requests
import datetime as dt

pixela_endpoint = 'https://pixe.la/v1/users'


TOKEN = 'hadfqr(q3324)'
USER_NAME = 'hunter-pro'
parameters = {
    'token':TOKEN,
    'username':USER_NAME,
    'agreeTermsOfService':'yes',
    'notMinor':'yes'
}

# response = requests.post(url=pixela_endpoint,json=parameters)

# print(response.text)

graph_endpoint = f'{pixela_endpoint}/{USER_NAME}/graphs'

GRAPH_ID = 'graph1'
graph_config = {
    'id':GRAPH_ID,
    'name':'Book Reading',
    'unit':'Hour',
    'type':'float',
    'color':'sora',
    'timezone':'Asia/Kolkata'
}

headers = {
    'X-USER-TOKEN':TOKEN
}

# response = requests.post(url=graph_endpoint,json=graph_config,headers=headers)
# print(response.text)

foramtted_date =  dt.date.today().strftime('%Y%m%d')

add_pixel_endpoint = f'{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}'

pixel_config = {
    'date': foramtted_date,
    'quantity': input('how many hours of Book Reading have to done today?:(float)')

}

response = requests.post(url=add_pixel_endpoint,json=pixel_config,headers=headers)

print(response.text)

update_pixel_endpoint = f'{add_pixel_endpoint}/{foramtted_date}'

update_config = {
    'quantity':'2'
}

# response = requests.put(url=update_pixel_endpoint,json=update_config,headers=headers)

# print(response.text)

delete_pixel_endpoint = f'{update_pixel_endpoint}'

# response = requests.delete(url=delete_pixel_endpoint,headers=headers)

# print(response.text)