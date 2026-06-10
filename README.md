# El Baúl del Pelu

Aplicación web fullstack de e-commerce para una tienda de ropa, zapatillas y accesorios. Desarrollada con Django 4.2, cuenta con catálogo de productos, carrito de compras, gestión de pedidos, blog, formulario de contacto con envío de correo y panel de administración completo.

---

## Funcionalidades

- **Tienda** — Catálogo de productos con categorías, descripción, imágenes y precios
- **Carrito de compras** — Lógica de sesión para agregar, restar y eliminar productos
- **Pedidos** — Registro y gestión de órdenes de compra
- **Autenticación** — Registro e inicio de sesión con el sistema nativo de Django
- **Blog** — Posts con categorías y autor
- **Servicios** — Sección de servicios de la tienda
- **Contacto** — Formulario de contacto con envío de correo electrónico via SMTP
- **Panel de administración** — Gestión completa de productos, pedidos, blog y servicios

---

## Tecnologías utilizadas

| Tecnología | Uso |
|---|---|
| Python | Lenguaje principal |
| Django 4.2.7 | Framework web |
| MySQL | Base de datos (producción) |
| SQLite | Base de datos (desarrollo local) |
| Django Crispy Forms | Formularios con Bootstrap |
| Pillow | Manejo de imágenes |
| Bootstrap | Layout responsivo |
| PyMySQL | Conector Python-MySQL |

---

## Estructura del proyecto

```
EBDP/
├── EBDP/           # Configuración principal (settings, urls, wsgi)
├── EBDPApp/        # App principal (index)
├── autenticacion/  # Registro, login y logout
├── tienda/         # Productos y categorías
├── carro/          # Carrito de compras con sesiones
├── pedidos/        # Gestión de pedidos
├── blog/           # Posts y categorías del blog
├── servicios/      # Servicios de la tienda
├── contacto/       # Formulario de contacto
├── cont/           # Módulo de contacto alternativo con EmailMessage
├── media/          # Archivos subidos (imágenes)
└── manage.py
```

---

## Instalación y ejecución local

### Requisitos

- Python 3.10

### Pasos

1. Clona el repositorio:
   ```bash
   git clone https://github.com/alysph/EBDP.git
   cd EBDP
   ```

2. Instala las dependencias:
   ```bash
   pip install django==4.2.7 pillow django-crispy-forms crispy-bootstrap4 pymysql
   ```

3. Cambia la base de datos a SQLite en `EBDP/settings.py`:
   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.sqlite3',
           'NAME': BASE_DIR / 'db.sqlite3',
       }
   }
   ```

4. Aplica las migraciones:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. Crea un superusuario:
   ```bash
   python manage.py createsuperuser
   ```

6. Levanta el servidor:
   ```bash
   python manage.py runserver
   ```

7. Abre el navegador en **http://127.0.0.1:8000/**

---

## Autora

**Alison Urrea** — [GitHub](https://github.com/alysph)

---

## Licencia

Proyecto académico — Duoc UC, 2023.
