import requests
from datetime import datetime

key="Make your's randomly"
username="your username"
pixela_endpoint="https://pixe.la/v1/users"
params={
    "token":key,
    "username":username,
    "agreeTermsOfService":"yes",
    "notMinor":"yes"
}

# response=requests.post(url=pixela_endpoint,json=params)
# print(response.text)

graph_endpoint=f"{pixela_endpoint}/{username}/graphs"
graph_config={
    "id":"graph2",
    "name":"Cycling Graph",
    "unit":"Km",
    "type":"float",
    "color":"sora"
}

headers={
    "X-USER-TOKEN":key
}

# response=requests.post(url=graph_endpoint,json=graph_config,headers=headers)
# print(response.text)

#------------------------ADDING A PIXEL-------------------------------------------------------#
today=datetime.now()

pixel_endpoint=f"{pixela_endpoint}/{username}/graphs/graph2"
pixel_config={
    "date":today.strftime("%Y%m%d"),
    "quantity":str(input("How much did you cycle today? : "))
}
pixel_header={
    "X-USER-TOKEN":key
}

response=requests.post(url=pixel_endpoint,json=pixel_config,headers=pixel_header)
print(response.text)

#--------------------------UPDATING A PIXEL----------------------------------------------------#

update_pixel_endpoint=f"{pixela_endpoint}/{username}/graphs/graph2/20251001"
update_pixel_config={
    "quantity":"15"
}
# response=requests.put(url=update_pixel_endpoint,json=update_pixel_config,headers=headers)
# print(response)

#-------------------------DELETING A PIXEL-----------------------------------------------------#

delete_pixel_endpoint=f"{pixela_endpoint}/{username}/graphs/graph2/20251001"
# response=requests.delete(url=delete_pixel_endpoint,headers=headers)
# print(response)