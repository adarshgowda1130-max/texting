import requests
from datetime import date
today=date.today().strftime("%Y%m%d")
USERNAME="adhi17"
TOKEN="Password@1208"
GRAPH_ID="graph12"
pixela_endpoint="https://pixe.la/v1/users"
request_to_pixela={
  "token":TOKEN,
  "username":USERNAME,
  "agreeTermsOfService":"yes",
  "notMinor":"yes"
}
# acc_post=requests.post(url=pixela_endpoint,json=request_to_pixela)
# print(acc_post.text)
graph_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs"
graph_parms={
    "timezone":"Asia/Kolkata",
    "color":"sora",
    "unit":"minutes",
    "type":"int",
    "name":"first_graph",
    "id":GRAPH_ID
}
headers={
    "X-USER-TOKEN":TOKEN
}
graph=requests.post(url=graph_endpoint,json=graph_parms,headers=headers)
# print(graph.text)
add_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today}"
add_params={
    "date":today,
    "quantity":"45",
}
added=requests.post(url=add_endpoint,json=add_params,headers=headers)
#print(added.text)
update_endpoint=f"{graph_endpoint}/{GRAPH_ID}"
update_parmas={
    "unit":"12"
}
update=requests.put(url=update_endpoint,json=update_parmas,headers=headers)
print(update.text)