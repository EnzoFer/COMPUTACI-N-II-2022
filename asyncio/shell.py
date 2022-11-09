import asyncio, argparse, subprocess

async def handle_echo(reader, writer):

    while True:

        content = await reader.read(100)
        content = (content.decode())
        addr = writer.get_extra_info('peername')

        if len(content) == 0 or content == 'exit':
            print(f"{addr} desconectado")  
            writer.close()
            await writer.wait_closed()
            return
        print(f"Mensaje de {addr}")
        command = subprocess.Popen([content], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        stdout, stderr = command.communicate()
        if command.returncode == 0:
            ans = b"OK \n "+stdout.encode()
        else:
            ans = b"ERROR \n "+stderr.encode()
        writer.write(ans)
        await writer.drain()

async def main():
    parser = argparse.ArgumentParser(description="Servidor asincrónico")
    parser.add_argument('-ht', type=str, help="Ingresar host")
    parser.add_argument('-p', type=int, help="Ingresar puerto")
    args = parser.parse_args()
    server = await asyncio.start_server(handle_echo, args.ht, args.p)
    print("Starting server...")
    await server.serve_forever()
    
asyncio.run(main())