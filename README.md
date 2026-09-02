Markdown
# SauceDemo Automation Framework

Estructura de automatización de pruebas End-to-End (E2E) construida sobre la aplicación [SauceDemo](https://www.saucedemo.com/) aplicando el patrón de diseño Page Object Model (POM), ejecución asíncrona de Playwright y gestión de estado mediante Pytest.

## 🛠️ Tecnologías y Herramientas

* **Lenguaje:** Python 3.10+
* **Framework de Automatización:** Playwright (Python Sync API)
* **Test Runner:** Pytest
* **Manejo de Entorno:** Python-dotenv
* **Reporteo:** Allure Framework (Integración en Módulo 04)

## 📁 Arquitectura del Proyecto

```text
.
├── config.py              # Carga y validación estricta de variables de entorno
├── conftest.py            # Fixtures globales de Pytest e inyección de contexto
├── pages/                 # Abstracción de UI (Page Object Model)
│   ├── base_page.py       # Encapsulamiento del objeto Page y esperas explícitas
│   └── auth_page.py       # Localizadores semánticos y flujos de autenticación
├── tests/                 # Suites de prueba E2E
│   └── test_auth.py       # Casos positivos y parametrizados de login
├── .env.example           # Plantilla de variables de entorno requeridas
├── .gitignore             # Exclusión de credenciales y artefactos de ejecución
├── pytest.ini             # Configuración global del ejecutor de pruebas
└── requirements.txt       # Dependencias del proyecto
⚙️ Configuración del Entorno
1. Requisitos Previos
Python 3.10 o superior instalado.

Git configurado localmente.

2. Instalación
Clona el repositorio e instala las dependencias del proyecto:

Bash
# Crear entorno virtual
python -m venv .venv

# Activar entorno virtual (Linux/Mac)
source .venv/bin/activate
# Activar entorno virtual (Windows PowerShell)
.venv\Scripts\Activate.ps1

# Iniciar e instalar dependencias
pip install -r requirements.txt
playwright install chromium
3. Variables de Entorno
Crea un archivo .env en la raíz del proyecto basándote en la plantilla .env.example:

Fragmento de código
BASE_URL=[https://www.saucedemo.com](https://www.saucedemo.com)
QA_USER=standard_user
QA_PASSWORD=secret_sauce
🚀 Ejecución de Pruebas
Bash
# Ejecución completa de la suite
pytest

# Ejecución en modo visible (Headed)
pytest --headed

# Ejecución con generación de reporte Allure
pytest --alluredir=allure-results