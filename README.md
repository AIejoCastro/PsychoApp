### PsychoApp

# Cómo iniciar el programa

## 1. Crear un Entorno Virtual (venv)

### Paso 1: Navegar a tu Directorio de Proyecto

Abre tu terminal y navega al directorio donde quieres crear tu entorno virtual.
(Abran el proyecto en el IDE e ingresan a la terminal desde ahí y ponen el siguiente comando)

```bash
cd ..
```

### Paso 2: Crear el Entorno Virtual

Usa el siguiente comando para crear un entorno virtual llamado `venv`.

```bash
python -m venv venv
```

### Paso 3: Activar el Entorno Virtual

- **Activar**:
```bash
venv\Scripts\activate
```

Una vez que el entorno esté activado, deberías ver el nombre del entorno virtual al inicio de la línea de tu terminal, indicando que está activo.

## 2. Instalar Dependencias desde `requirements.txt`

### Paso 1: Ir desde que activas el entorno virtual a la carpeta del repositorio

```bash
cd .\PsychoApp\
```

### Paso 2: Instalar las Dependencias

Ejecuta el siguiente comando para instalar todas las dependencias listadas en `requirements.txt`.

```bash
pip install -r requirements.txt
```

## 3. Confirmar Instalación

Para confirmar que Django y otras dependencias se instalaron correctamente, ejecuta:

```bash
python -m django --version
```
Esto debería mostrar la versión de Django instalada.

## 4. Desactivar el Entorno Virtual

Cuando hayas terminado de trabajar, puedes desactivar el entorno virtual con el comando:

```bash
deactivate
```