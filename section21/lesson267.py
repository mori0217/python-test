import tasks

result = tasks.build_servers_with_cleanup.delay()
# result = tasks.build_server()
print("doing...")
print(result)
