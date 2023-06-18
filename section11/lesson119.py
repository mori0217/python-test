import yaml

with open('section11/config.yml', 'w') as f:
    yaml.safe_dump({
        "web_server": {
            'host': "127.0.0.1",
            "port": 80
        },
        "db_server": {
            "host": "127.0.0.2",
            "port": 3306
        }
    }, f, default_flow_style=False)


with open("section11/config.yml", "r") as f:
    data = yaml.safe_load(f)
    print(data)
    print(type(data))
    print(data["web_server"]["host"])
    print(data["web_server"]["port"])
    print(data["db_server"]["host"])
    print(data["db_server"]["port"])
