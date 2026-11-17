// serve_dash.mjs — book-signal-review dashboard sunucusu (gzip onbellekli)
// Kullanim: node tools/serve_dash.mjs  ->  http://localhost:8124/
import { createServer } from 'node:http';
import { readFile } from 'node:fs/promises';
import { gzipSync } from 'node:zlib';
import { fileURLToPath } from 'node:url';
import { dirname, extname, join, normalize, sep } from 'node:path';

const ROOT = join(dirname(fileURLToPath(import.meta.url)), '..', 'backtest', 'filter_layer');
const PORT = 8124;

const MIME = {
  '.html': 'text/html; charset=utf-8',
  '.js': 'application/javascript; charset=utf-8',
  '.json': 'application/json; charset=utf-8',
  '.css': 'text/css; charset=utf-8',
  '.woff2': 'font/woff2',
  '.woff': 'font/woff',
  '.png': 'image/png',
  '.svg': 'image/svg+xml',
  '.ico': 'image/x-icon',
  '.txt': 'text/plain; charset=utf-8',
};
const COMPRESSIBLE = new Set(['.html', '.js', '.json', '.css', '.svg', '.txt']);
const ROUTES = {
  '/': 'dashboard_pro.html',
  '/pro': 'dashboard_pro.html',
  '/eski': 'filter_dashboard.html',
  '/dashboard_data.json': 'dashboard_data.json',
};

const cache = new Map();
async function load(rel) {
  const file = normalize(join(ROOT, rel));
  if (!file.startsWith(ROOT + sep)) throw Object.assign(new Error('Yasak yol'), { status: 403 });
  if (!cache.has(file)) {
    const raw = await readFile(file);
    const ext = extname(file).toLowerCase();
    const gz = COMPRESSIBLE.has(ext) ? gzipSync(raw, { level: 6 }) : null;
    cache.set(file, { raw, gz, mime: MIME[ext] || 'application/octet-stream' });
  }
  return cache.get(file);
}

createServer(async (req, res) => {
  const url = (req.url || '/').split('?')[0];
  let rel = ROUTES[url];
  if (!rel && url.startsWith('/assets/')) rel = url.slice(1);
  if (!rel) {
    res.writeHead(404, { 'Content-Type': 'text/plain; charset=utf-8' });
    res.end('Bulunamadi: ' + url + '\nMevcut: ' + Object.keys(ROUTES).join(', ') + ', /assets/*');
    return;
  }
  try {
    const entry = await load(rel);
    const ae = req.headers['accept-encoding'] || '';
    if (entry.gz && ae.includes('gzip')) {
      res.writeHead(200, {
        'Content-Type': entry.mime,
        'Content-Encoding': 'gzip',
        'Content-Length': entry.gz.length,
        'Cache-Control': 'no-cache',
      });
      res.end(entry.gz);
    } else {
      res.writeHead(200, {
        'Content-Type': entry.mime,
        'Content-Length': entry.raw.length,
        'Cache-Control': 'no-cache',
      });
      res.end(entry.raw);
    }
  } catch (e) {
    res.writeHead(e.status || 500, { 'Content-Type': 'text/plain; charset=utf-8' });
    res.end('Hata: ' + e.message);
  }
}).listen(PORT, () => console.log('[serve] http://localhost:' + PORT + ' hazir · rotalar: ' + Object.keys(ROUTES).join(', ') + ', /assets/*'));
