#credit to Dataloden for this source code.
#credit to Velocity for the metadata link
import requests
import json
import os
import time

token = str(input("please enter authorization code for your account:"))
#print(f"successfully imputted {token} into variable token")
try:
    url = ' https://account-public-service-prod.ol.epicgames.com/account/api/oauth/token'
    myobj = {'grant_type': 'authorization_code', 'code': token}
    x = requests.post(url, data = myobj, auth=('ec684b8c687f479fadea3cb2ad83f5c6', 'e1f31c211f28413186262d37a13fc84d'))
    #auth="Basic ZWM2ODRiOGM2ODdmNDc5ZmFkZWEzY2IyYWQ4M2Y1YzY6ZTFmMzFjMjExZjI4NDEzMTg2MjYyZDM3YTEzZmM4NGQ="
    #print the response text (the content of the requested file):
    resp = x.text
    dicty = json.loads(resp)
    bond = dicty['access_token']
    accid = dicty['account_id']
    revi = 1
    #print(bond)
    def get_party_id():
        securl = f"https://party-service-prod.ol.epicgames.com/party/api/v1/Fortnite/user/{accid}"
        obj = {}
        auth = {"Authorization": f"Bearer {bond}"}
        print("getting party id....")
        y = requests.get(securl, data=obj, headers=auth).json()
        ppl = dict(y).get("current")
        strin = str(ppl)
        lis = list(strin)
        combolist = lis[9] + lis[10] + lis[11] + lis[12] + lis[13] + lis[14] + lis[15] + lis[16] + lis[17] + lis[18] + lis[19] + lis[20] + lis[21] + lis[22] + lis[23] + lis[24] + lis[25] + lis[26] + lis[27] + lis[28] + lis[29] + lis[30] + lis[31] + lis[32] + lis[33] + lis[34] + lis[35] + lis[36] + lis[37] + lis[38] + lis[39] + lis[40]
        return combolist
        '''yu = y.text
        yup = json.loads(yu)
        yuppi = str(yup).replace("'", '"')
        koko = json.loads(yuppi)
        yuppl = koko["current"]
        ditto = dict(yuppi)
        #newstr = str(yuppl).replace("'", '"')
        #par = json.loads(list(newstr))
        #print(newstr)
        pid = ditto["id"]
        return pid
        #print(f"url is {securl}")'''
    def change_skin():
        third_url = f"https://party-service-prod.ol.epicgames.com/party/api/v1/Fortnite/parties/{get_party_id()}/members/{accid}/meta"
        with open("skin.json", "r+") as f:
            objct = json.load(f) 
        authy = {"Authorization": f"Bearer {bond}"}
        z = requests.patch(third_url, json=objct, headers=authy).json()
        print(z)
        estr = str(z)
        lista = list(estr)
        if lista[8] == "o":
            rev = z.get("messageVars")
            objct["revision"] = rev[1]
            with open("skin.json", "w+") as fp:
                json.dump(objct, fp, sort_keys=False, indent=4)
            #change_skin()
            #add this to json to also false ready: "Default:GameReadiness_s": "Ready",
            requests.patch(third_url, json=objct, headers=authy)
            print("successfully changed skin")
            
    def goback():
        comm = str(input("enter a command:"))
        if comm == "banana":
            change_skin()
            goback()
        elif comm == "spam":
            for i in range(300):
                if i == 300:
                    print("done spamming.")
                    goback()
                else:
                    change_skin()
                    time.sleep(1)
    goback()

#except IndexError:
#            await message.reply("authorization code not supplied. be sure to log into epic games website, visit https://www.epicgames.com/id/api/redirect?clientId=ec684b8c687f479fadea3cb2ad83f5c6&responseType=code, and put in the code you see inside the redirect url")
except KeyError:
    print(f"{dicty['errorMessage']}")
