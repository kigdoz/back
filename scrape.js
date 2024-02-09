const axios = require('axios');
const fs = require('fs');

const proxies = [];
const output_file = 'proxy.txt';

if (fs.existsSync(output_file)) {
  fs.unlinkSync(output_file);
  console.log(`'${output_file}' đã xóa bỏ.`);
}

const raw_proxy_sites = [
'https://proxyspace.pro/http.txt',
'https://api.proxyscrape.com/v3/free-proxy-list/get?request=displayproxies&country=VN&anonymity=all&timeout=15000&proxy_format=ipport&format=text',
'https://api.proxyscrape.com/v3/free-proxy-list/get?request=displayproxies',
'https://api.proxyscrape.com/v2/?request=displayproxies&protocol=all&timeout=10000&country=all&ssl=all&anonymity=all',
'https://spys.one/free-proxy-list/VN/',
'https://proxypremium.top/full-proxy-list',
'https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt',
];

async function fetchProxies() {
  for (const site of raw_proxy_sites) {
    try {
      const response = await axios.get(site);
      const lines = response.data.split('\n');
      for (const line of lines) {
        if (line.includes(':')) {
          const [ip, port] = line.split(':', 2);
          proxies.push(`${ip}:${port}`);
        }
      }
    } catch (error) {
      console.error(`Không thể truy xuất proxy từ ${site}: ${error.message}`);
    }
  }

  fs.writeFileSync(output_file, proxies.join('\n'));
  console.log(`Proxy đã được truy xuất và lưu trữ thành công trong ${output_file}`);
}

fetchProxies();
