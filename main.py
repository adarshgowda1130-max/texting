import requests
pixela_endpoint="https://pixe.la/v1/users"
request_to_pixela={
  "token":"Password@1208",
  "username":"adhiiii",
  "agreeTermsOfService":"yes",
  "notMinor":"yes"
}
# post=requests.post(url=pixela_endpoint,json=request_to_pixela)
# print(post.text)
graph_endpoint=f"{pixela_endpoint}/adhiiii/graphs"
graph_params={
    "timezone":"Asia/Kolkata",
    "color":"sora",
    "unit":"minutes",
    "type":"int",
    "name":"first_graph",
    "id":"adarsh12"
}
graph_header={
    "X-USER-TOKEN":"Password@1208"
}
graph_post=requests.post(url=graph_endpoint,json=graph_params,headers=graph_header)
print(graph_post.text)