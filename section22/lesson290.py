import asyncio
import asyncio.subprocess


async def run(cmd):
    proc = await asyncio.create_subprocess_shell(
        cmd, stdout=asyncio.subprocess.PIPE)
    stdout, stderr = await proc.communicate()
    print(stdout.decode())
    exitcode = await proc.wait()
    print(f'exitcode: {exitcode}')

loop = asyncio.get_event_loop()

loop.run_until_complete(asyncio.wait([run("ls -al"), run("pwd")]))
loop.close()
