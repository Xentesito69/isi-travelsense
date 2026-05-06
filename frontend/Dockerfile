# ── Stage 1: no hay build steps (SPA puro en HTML/CSS/JS) ───────────────────
# Stage kept simple – si en el futuro se añade un bundler (Vite/Webpack)
# se añadiría aquí el npm run build.

# ── Stage 2: runtime con Nginx ───────────────────────────────────────────────
FROM nginx:1.25-alpine

# Eliminar la página de bienvenida de Nginx
RUN rm -rf /usr/share/nginx/html/*

# Copiar el frontend estático
COPY index.html  /usr/share/nginx/html/index.html
COPY coords.js   /usr/share/nginx/html/coords.js
COPY logo.png    /usr/share/nginx/html/logo.png
COPY logodark.png /usr/share/nginx/html/logodark.png

# Configuración de Nginx: sirve el frontend y redirige /api/* al backend
COPY nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80
