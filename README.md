# Fusionador de PDFs

Este script en Python permite **fusionar múltiples archivos PDF** en uno solo, siguiendo el orden proporcionado por el usuario. El archivo resultante se guarda automáticamente con el **nombre de la carpeta actual**.

## 📁 Ejemplo de uso

Supongamos que tienes los siguientes archivos PDF:
documento1.pdf documento2.pdf documento3.pdf

Y deseas fusionarlos en el orden dado. Solo ejecuta el script desde una terminal o consola:


```bash
python fusionpdf.py documento1.pdf documento2.pdf documento3.pdf
```
El resultado será un archivo llamado nombre_de_la_carpeta_actual.pdf generado en la misma carpeta.

## ⚙️ Requisitos

- Python 3.6 o superior
- Las dependencias necesarias están listadas en `requirements.txt`.

Instálalas fácilmente con:

```bash
pip install -r requirements.txt
```

Y también puedes agregar una línea en la parte superior del README para que el usuario sepa clonar tu proyecto:


## 📦 Instalación

Clona este repositorio y entra a la carpeta:

```bash
git clone https://github.com/tu_usuario/fusionpdf.git
cd fusionpdf
pip install -r requirements.txt
```

## ⚡️ Configuración rápida en PowerShell

Si quieres ejecutar el script desde cualquier carpeta escribiendo simplemente `fusionpdf`, puedes hacer esto:

1. Abre tu perfil de PowerShell con este comando:
    ```powershell
    notepad $PROFILE
    ```

2. Agrega la siguiente función:

    ```powershell
    function fusionpdf {
        python "C:\Users\alizarazo\Documents\github\fusionpdf\fusionpdf.py" $args
    }
    ```

3. Guarda el archivo y abre una nueva terminal de PowerShell.

¡Listo! Ahora puedes ejecutar `fusionpdf archivo1.pdf archivo2.pdf` desde cualquier carpeta.

## 🖼️ Ejemplos visuales

### 📂 Antes de ejecutar

![Antes de ejecutar](images/antes.png)

### ⚙️ Ejecutando el comando

```bash
fusionpdf documento1.pdf documento2.pdf documento3.pdf
