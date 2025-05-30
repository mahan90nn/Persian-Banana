from plugins.common import *
import requests

def connect(username, server):
    try:
        if checkserver(server) == False: error('Please input a real domain or server'); return
        elif ':' in server: gzeht = str(server).split(':'); server = gzeht[0]; port = int(gzeht[1])
        response = requests.post('http://localhost:6969/connect', json={
            "host": server, "port": 25565 if not ':' in server else port, "username": username
        })

        if response.status_code != 200 and response.status_code != 400:
            return error(f'Failed to connect [{response.status_code}]')

        while not requests.get('http://localhost:6969/status').json()[server + ':' +'25565' if not ':' in server else port][username]:
            info('Waiting for connection...')
            time.sleep(1)
        
        info(f'Type "exit" to exit. [beta] this is still very shit but it works for sending messages')
        while True: 
            msg = input('> ').strip()
            if msg.lower() == "exit":
                if requests.get('http://localhost:6969/status').json()[server + ':' +'25565' if not ':' in server else port][username]:
                    requests.post('http://localhost:6969/disconnect', json={"host": server, "port": 25565 if not ':' in server else str(port), "username": username})
                    info(f'Bot disconnected.')
                else:
                    info(f'Bot already disconnected.')
                return
            if requests.post('http://localhost:6969/send', json={"host": server, "port": 25565 if not ':' in server else port, "username": username, "message": msg}).status_code != 200:
                error(f'Failed to send message. (BOT LIKELY NOT CONNECTED)')

    except KeyboardInterrupt: requests.post('http://localhost:6969/disconnect', json={"host": server, "port": 25565 if not ':' in server else port, "username": username}); return
    except Exception as e: 
        error(e)