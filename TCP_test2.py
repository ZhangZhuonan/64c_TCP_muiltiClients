from anyio import create_tcp_listener, run
Is_liscen = False

#tcp服务端代码，
async def handle(client):
    async with client:
        print("客户端",client)
        while Is_liscen:
            name = await client.receive(1024)
            await client.send(b'Hello, %s n' % name)

async def main():
    listener = await create_tcp_listener(local_host='192.168.0.132',local_port=9999)
    await listener.serve(handle)

run(main)
