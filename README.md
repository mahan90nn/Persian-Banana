<h1 align="center">
  <img src="https://r2.e-z.host/049cab41-5ed3-4a5c-a42f-5b83b721f333/re5pq23l.png" alt="Header Image" style="width:30%; max-width:600px;"/>
</h1>


# Banana
This is a free and better alternative to MCPTool

# Installation
## Requirements 
- Python 3.10+
- winget package manager (Windows)

## Get a local copy up and running
```
Open Terminal and run: 
git clone https://github.com/Renovsk/Banana.git && cd Banana
pip3 install -r requirements.txt
python3 main.py

Install the command line developer tools if prompted
```

# Features
## Commands

| Command   | Arguments         | Description                                                         |
|-----------|-------------------|---------------------------------------------------------------------|
| `server`  | `<address>`        | Shows information about the server                                  |
| `uuid`    | `<ign>`            | Shows player's UUID                                                 |
| `ipinfo`  | `<ip>`             | Shows information about the given IP                                |
| `monitor` | `<ip>`             | Monitors who leaves and joins on a specified server (if queries are enabled) |
| `dns`     | `<domain>`         | Shows all DNS records of the domain                                 |
| `proxy`   | `<ip> <mode>`      | Starts a local Velocity proxy server that redirects to the specified server |
| `check`   | `<file>`           | Check the status of Minecraft servers listed in a specified text file |
| `scan`    | `<ip> <range> <threads>` | Check the status of Minecraft servers listed in a specified text file. Example: `scan 0.0.0.0 1-65535 10` |
| `clear`   | N/A               | Clears the screen                                                    |
| `update`  | N/A               | Re-initializes Banana                                                |
| `kick`    | `<username> <server>` | Kicks a player from the server (if cracked)                          |
| `shell`   | `<port>`           | Uses netcat to listen to a port                                      |
| `connect` | `<username> <server>` | Joins with a bot and allows you to send messages                     |
| `rcon`    | `<server> <password>` | Connects to a server's RCON                                         |
| `brutrcon`| `<server> <file>`  | Tries the passwords of the file given to try to connect to RCON     |
| `fuzz`    | `<website> <file> <threads>` | Example: `example.com/FUZZ` or `FUZZ.example.com`                   |
| `sendcmd` | `<username> <server> <file>` | Sends a bot that will execute a list of commands from a file        |


MORE SOON!

## Credits
- Made by @x5ten on discord
- Translated By @mahan90nn on discord

## Persian

# موز

این یک جایگزین رایگان و بهتر برای MCPTool است.

# نصب
## الزامات

پایتون ۳.۱۰+
مدیر بسته winget (ویندوز)

یک نسخه محلی از آن را دریافت و اجرا کنید

ترمینال را باز کنید و اجرا کنید:

git clone https://github.com/Renovsk/Banana.git && cd Banana
pip3 install -r requirements.txt
python3 main.py

در صورت درخواست، ابزارهای توسعه‌دهنده خط فرمان را نصب کنید.

# ویژگی‌ها
## دستورات
آرگومان‌های دستور توضیحات
server <address> اطلاعات مربوط به سرور را نشان می‌دهد.

uuid <ign> UUID بازیکن را نشان می‌دهد.

ipinfo <ip> اطلاعات مربوط به IP داده شده را نشان می‌دهد.

monitor <ip> نظارت می‌کند که چه کسی در یک سرور مشخص شده خارج می‌شود و به آن می‌پیوندد (در صورت فعال بودن پرس‌وجوها)

dns <domain> تمام رکوردهای DNS دامنه را نشان می‌دهد.

proxy <ip> <mode> یک سرور پروکسی محلی Velocity را شروع می‌کند که به سرور مشخص شده هدایت می‌شود.

check <file> وضعیت سرورهای Minecraftرا بررسی می‌کند. فهرست شده در یک فایل متنی مشخص شده

scan <ip> <range> <threads> وضعیت سرورهای ماینکرفت فهرست شده در یک فایل متنی مشخص شده را بررسی کنید. مثال: اسکن 0.0.0.0 1-65535 10

Clear صفحه را پاک می‌کند

Update موز را دوباره مقداردهی اولیه می‌کند

kick <name> <server> یک بازیکن را از سرور بیرون می‌کشد (در صورت کرک بودن سرور)

shell <port> از netcat برای گوش دادن به پورت استفاده می‌کند

connect <username> <server> به یک ربات متصل می‌شود و به شما امکان ارسال پیام می‌دهد

rcon <سرور> <رمز عبور> به RCON یک سرور متصل می‌شود

brutrcon <سرور> <فایل> رمزهای عبور فایل داده شده را برای اتصال به RCON امتحان می‌کند

fuzz <وب‌سایت> <فایل> <موضوعات> مثال: example.com/FUZZ یا FUZZ.example.com

sendcmd <نام کاربری> <سرور> <فایل> یک ربات ارسال می‌کند که لیستی از دستورات را از یک فایل اجرا می‌کند

به زودی بیشتر!

ساخته شده توسط @x5ten در دیسکورد
ترجمه شده توسط @mahan90nn در دیسکورد
