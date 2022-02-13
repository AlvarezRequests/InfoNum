import requests
from getpass import _raw_input



api = '510f8c00e437e5c107b8629d2fe5ca20'

print("""

         

           '       \
          |,.  ,-.  |
          |()L( ()| |
          |,'  `".| |
          |.___.',| `
         .j `--"' `  `.
        / '        '   \
       / /          `   `.
      / /            `    .
     / /              l   |
    . ,               |   |
    ,"`.             .|   |
 _.'   ``.          | `..-'l
|       `.`,        |      `.
|         `.    __.j         )
|__        |--""___|      ,-'
   `"--...,+
   
     """)
numero = int(_raw_input("Ingrese el numero de telefono porfavor >> "))

info = requests.get("http://apilayer.net/api/validate?access_key=%s&number=%s&country_code&format=1" % (api, numero))

for key, valor in info.json().items():
    print("\n%s: %s" % (key, valor))
