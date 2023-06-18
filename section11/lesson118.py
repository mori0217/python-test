import configparser

config = configparser.ConfigParser()

# config["DEFAULT"] = {
#     "debug": "True"
# }
# config["web_server"] = {
#     "host": "127.0.0.1",
#     "port": "80"
# }
# config["db_server"] = {

#     "host": "127.0.0.2",
#     "port": "3306"
# }

# with open("section11/config.ini", "w") as f:
# config.write(f)

config.read("section11/config.ini")
print(config.sections())
print(config["web_server"])
print(config["web_server"]["host"])
print(config["web_server"]["port"])
