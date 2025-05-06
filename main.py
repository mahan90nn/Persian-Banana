import importlib.util
from plugins.initialize import *
from plugins.common import *
from plugins.logging import *
from plugins.commands.server import server
from plugins.commands.uuid import puuid
from plugins.commands.rcon import rcon
from plugins.commands.rconbrut import rconbrut
from plugins.commands.fuzz import fuzz
from plugins.commands.ipinfo import ipinfo
from plugins.commands.dns import lookup
from plugins.commands.checker import check
from plugins.commands.scan import scan
from plugins.commands.monitor import monitor
from plugins.commands.proxy import proxy
from plugins.commands.connect import connect
from plugins.commands.kick import kick
from plugins.commands.sendcmd import sendcmd
from plugins.commands.shell import shell
from plugins.commands.ogmur import ogmur
from plugins.commands.target import target

scripts = {}

commands = {
    'server': (server, 1, "Usage: server <address>\ninfo server ra neson mydahad"),
    'uuid': (puuid, 1, "Usage: uuid <ign>\nuuid player ra neson mydahad"),
    'ipinfo': (ipinfo, 1, "Usage: ipinfo <ip>\netlahat ye ip ro neson mydahad"),
    'monitor': (monitor, 1, "Usage: monitor <ip>\nmybyny ky left va join dar ye server myde! (age queries enable sode base)"),
    'dns': (lookup, 1, "Usage: dns <domain>\nhame dns hay domain ro neson myde "),
    'target': (target, 1, "Usage: target <domain>\nhame subdomain haro neson myde w/ their resolved ips"),
    'proxy': (proxy, 2, "Usage: proxy <ip> <mode>\nye proxy velocity run mykone ke be server connect myde"),
    'check': (check, 1, "Usage: check <file>\nserver hayy ke toy ye file hastan ro check mykone"),
    'scan': (scan, 3, "Usage: scan <ip> <range> <threads>\nstatus server minecraft ro check mykone dar ye file \nExample: scan 0.0.0.0 1-65535 10"),
    'clear': (clear, 0, "Clears the screen"),
    'ogmur': (ogmur, 3, "Usage: ogmur <users_file> <server> <commands_file>\nye bot myfrestea az ye file myfreste ke az ye file command ejra mykone"),
    'update': (upd, 0, "Re-Initializes banana"),
    'kick': (kick, 2, "Usage: kick <username> <server>\nye player ra ba join dadan kick myde (age server cracked base)"),
    'shell': (shell, 1, "Usage: shell <port>\naz netcat estefade mykone ye port ro listen kone"),
    'connect': (connect, 2, "Usage: connect <username> <server>\nba ye bot join myde va mytony control koni),
    'rcon': (rcon, 2, "Usage: rcon <server> <password>\nbe rcon server connnect myde"),
    'brutrcon': (rconbrut, 2, "Usage: brutrcon <server> <file>\npassword hay ye file ro check mykone ke be rcon servre connect bede),
    'fuzz': (fuzz, 3, "Usage: fuzz <website> <file> <threads>\nExample: example.com/FUZZ or FUZZ.example.com"),
    'sendcmd': (sendcmd, 3, "Usage: sendcmd <username> <server> <commands_file>\nye bot myfreste ke az ye file command ejra mykone"),
    'exit': (exit, 0, "exit")
}

def chelp(command=None):
    if command is None:
        print(f"{yellow}[{white}Available Commands{yellow}]")
        for cmd, (func, args, msg) in commands.items(): print(f"{yellow}[{white}{cmd}{yellow}] {white}- {msg.splitlines()[0]}")
        for name, script in scripts.items(): print(f"{yellow}[{white}{name}{yellow}] {white}- {script['usage'].splitlines()[0]}")
    elif command in commands:
        _, _, msg = commands[command]
        print(msg)
    elif command in scripts:
        print(scripts[command]['usage'])
    else: print(f'Command estebah ast')


def loadscripts(folder='scripts'):
    if not os.path.exists(folder): return
    for filename in os.listdir(folder):
        if filename.endswith('.py'):
            path = os.path.join(folder, filename)
            spec = importlib.util.spec_from_file_location(filename[:-3], path)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            name = filename[:-3]
            scripts[name] = {
                "module": module,
                "arguments": getattr(module, 'arguments', []),
                "usage": getattr(module, 'usage', ''),
            }

def api():
    gg = os.path.join(os.getcwd(), "api", "server.js")
    subprocess.Popen(
        ["node", gg],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        stdin=subprocess.DEVNULL,
        shell=False
    )

def execmd(cmd):
    try:
        part = cmd.split()
        if len(part) == 0:
            return

        command = part[0]
        args = part[1:]

        if command == "help":
            if len(args) == 0: chelp()
            elif len(args) == 1: chelp(args[0])

        elif command in commands:
            func, required_args, msg = commands[command]
            if len(args) == required_args:
                func(*args)
            else: print(msg)

        elif command in scripts:
            script = scripts[command]
            if len(args) == len(script["arguments"]):
                script["module"].run(dict(zip(script["arguments"], args)))
            else:
                print(script["usage"])

        else: print('Command estebah ast')

    except Exception as e: error(e)

if __name__ == '__main__':  
    initialize() 
    loadscripts()
    api()
    while True:
        try:
            cmd = input(f'{white}{os.getlogin()}@{yellow}moz:~{white}$ ')
            execmd(cmd)
        except KeyboardInterrupt: pass
