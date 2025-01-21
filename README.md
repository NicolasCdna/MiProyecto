Autor: Nicolas Caudana
---

## **Proyecto: Gestión de Vehículos, Versiones y Proxies**

Este proyecto es una aplicación web desarrollada en **Django** que permite gestionar **vehículos**, **versiones** y **proxies** de manera eficiente, integrando relaciones y validaciones entre los modelos, además de formularios dinámicos.

---

### **Funciones Principales**

1. **Gestión de Vehículos**:
   - Creación y listado de vehículos.
   - Cada vehículo está asociado a una versión específica.
   - Validaciones en el formulario para asegurar que los datos sean consistentes.

2. **Gestión de Versiones**:
   - Creación y listado de versiones.
   - Validación de relaciones biunívocas entre `version_extend` y `version_codif` para evitar duplicados.
   - Asociación directa con vehículos y proxies.

3. **Gestión de Proxies**:
   - Creación de proxies con los siguientes campos:
     - Selección de una **central** (ECU) a través de un desplegable.
     - Asociación con una versión existente en la base de datos.
     - Configuración personalizada (64 bits) para cada proxy.
     - Inclusión de la versión de software asociada a la central.
   - Validación en tiempo de ejecución para asegurar que los datos cumplan con las restricciones.

4. **Página de Inicio**:
   - Navegación centralizada con enlaces hacia las distintas secciones:
     - **Vehículos**: Creación y listado.
     - **Versiones**: Creación y listado.
     - **Proxies**: Creación y listado.

---

### **Estructura Lógica y Validaciones**

#### **1. Relación Biunívoca en Version**
- El modelo `Version` asegura que los campos `version_extend` y `version_codif` sean únicos entre sí mediante la opción `unique_together` en `Meta`.
- Esto garantiza que no existan combinaciones duplicadas de estos campos en la base de datos.

#### **2. Asociación entre Modelos**
- **Vehículos**:
  - Cada vehículo se asocia a una versión existente mediante una clave foránea (`ForeignKey`).
- **Proxies**:
  - Cada proxy se asocia a una versión mediante una clave foránea (`ForeignKey`).
  - La central se selecciona de un conjunto predefinido de opciones, asegurando integridad en los datos.

#### **3. Formularios Dinámicos**
- Todos los formularios se basan en los modelos correspondientes (`ModelForm`), lo que asegura:
  - Validaciones automáticas definidas en el modelo.
  - Representación clara y simplificada de los datos en la interfaz.
- Ejemplo:
  - En el formulario de **Proxy**, solo se muestran versiones existentes cargadas previamente en la clase `Version`.

#### **4. Verificación de Longitudes**
- Campos como `version_extend` y `configuracion` tienen restricciones de longitud (`max_length`) para evitar datos corruptos o inconsistentes.
- El campo de configuración en el proxy está limitado a 64 caracteres alfanuméricos.

---

### **Ejecución del Proyecto**

#### **Requisitos Previos**
- Python 3.8+.
- Django 5.1.5.
- Un entorno virtual configurado.

#### **Pasos para Ejecutar**
1. Clona el repositorio:
   ```bash
   git clone <URL_DEL_REPOSITORIO>
   cd <CARPETA_DEL_PROYECTO>
   ```
2. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```
3. Realiza las migraciones:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
4. Ejecuta el servidor de desarrollo:
   ```bash
   python manage.py runserver
   ```
5. Accede a la aplicación en tu navegador en `http://127.0.0.1:8000/`.

---

### **Estructura de Navegación**

1. **Inicio** (`/`):
   - Página principal con enlaces hacia las secciones clave:
     - Vehículos.
     - Versiones.
     - Proxies.

2. **Vehículos**:
   - **Crear Vehículo** (`/crear/`).
   - **Lista de Vehículos** (`/vehiculos/`).

3. **Versiones**:
   - **Agregar Versión** (`/agregar_version/`).
   - **Lista de Versiones** (`/lista_versiones/`).

4. **Proxies**:
   - **Crear Proxy** (`/crear-proxy/`).
   - **Lista de Proxies** (`/lista-proxies/`).

---

### **Características Técnicas**

- **Patrón MTV**: Separación clara entre Modelos, Vistas y Plantillas.
- **Herencia de Plantillas**: Uso de un archivo `base.html` para mantener consistencia en todas las páginas.
- **Validaciones Automatizadas**:
  - Uso de `ModelForm` para manejar restricciones directamente desde los modelos.
  - Relación biunívoca y validaciones de unicidad entre campos.

---

### **Futuras Mejoras**
- Implementar un sistema de autenticación para manejar permisos de usuario.
- Agregar filtros avanzados en las listas (por ejemplo, por versión o central).
- Mejorar el diseño de la interfaz utilizando un framework como Bootstrap.

---
