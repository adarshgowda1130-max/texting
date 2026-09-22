import requests
request_to_pixela={
  "token":"Password@1208",
  "username":"adhiiii",
  "agreeTermsOfService":"yes",
  "notMinor":"yes"
}
post=requests.post(url="https://pixe.la/v1/users",json=request_to_pixela)
print(post.text)