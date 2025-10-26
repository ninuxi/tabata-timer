const CACHE_NAME = 'tabata-timer-v2.0.1';
const urlsToCache = [
  '/',
  '/index.html',
  '/programma.html',
  '/programma_testo.html',
  '/diario.html',
  '/about.html',
  '/manifest.json'
];

// Install event - cache resources
self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then((cache) => {
        console.log('Cache aperta:', CACHE_NAME);
        return cache.addAll(urlsToCache);
      })
  );
  // Force the waiting service worker to become the active service worker
  self.skipWaiting();
});

// Fetch event: always try network for HTML (navigate), cache others network-first
self.addEventListener('fetch', (event) => {
  const req = event.request;
  if (req.method !== 'GET') return;
  const accept = req.headers.get('accept') || '';

  // For navigations/HTML: network first, no re-cache of HTML, fallback to cache
  if (accept.includes('text/html')) {
    event.respondWith(
      fetch(req).catch(() => caches.match(req))
    );
    return;
  }

  // For other GETs: network first, then cache the fresh response, fallback to cache
  event.respondWith(
    fetch(req)
      .then((response) => {
        if(!response || response.status !== 200 || response.type !== 'basic') {
          return response;
        }
        const responseToCache = response.clone();
        caches.open(CACHE_NAME).then((cache) => cache.put(req, responseToCache));
        return response;
      })
      .catch(() => caches.match(req))
  );
});

// Activate event - clean old caches
self.addEventListener('activate', (event) => {
  const cacheWhitelist = [CACHE_NAME];
  event.waitUntil(
    caches.keys().then((cacheNames) => {
      return Promise.all(
        cacheNames.map((cacheName) => {
          if (cacheWhitelist.indexOf(cacheName) === -1) {
            console.log('Eliminando cache vecchia:', cacheName);
            return caches.delete(cacheName);
          }
        })
      );
    })
  );
  // Take control of all clients immediately
  return self.clients.claim();
});
