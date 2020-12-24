import  json

data = '{"var1":"harry" , "var2" : 45}'

parsed = json.loads(data)

print(parsed['var1'])

data2 = {    "channel_name" : "no channel" ,
             'cars' : ['mercedes' , 'rols royals'] ,
             "fridge" : ("roti" , "540")
}

data2_for_java = json.dumps(data2)
print(data2_for_java)

json.du