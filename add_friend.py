import requests
import os


url       = "https://discord.com/api/v9/users/@me/relationships"


print("=========================")
print("\tAdd Friend")
print("=========================\n")
token         = input("Discord Token: ")
headers       = { 
    "authorization": token, 
    "content-type": "application/json" 
}

user      = input("Username#Discriminator: ")
username = user.split("#")[:-1][0]
discriminator = user.split("#")[-1]

print(username)
print(discriminator)

json_data     = {
    "discriminator": discriminator, 
    "username": username
}



r = requests.post(url, json=json_data, headers=headers)
print(r.content)
if (r.content == b''): print("Successfull!")
else: print("Failed!")
  
  
