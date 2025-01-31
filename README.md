# 🏆 Koombea Challenge

Este repositorio contiene la solución a la prueba técnica de Koombea, la cual incluye:

## 📌 Descripción
Este proyecto abarca la automatización de pruebas para:
1. 📱 **Automatización móvil:** Pruebas con **Appium y Cucumber** para una aplicación de conversión de unidades.
2. 🌍 **Automatización de API:** Pruebas con **KarateDSL** para la API de Rick and Morty.

## 🔧 Requisitos y herramientas utilizadas
- **Lenguaje:** Python (para automatización móvil) y Java (para API)
- **Frameworks y librerías:**
  - **Móvil:** Appium, Cucumber
  - **API:** KarateDSL
- **Patrón de diseño:** Page Object Model (POM)
- **Gestión de dependencias:**
  - `pip` para Python
  - `Maven` para Java
- **Ejecutor de pruebas:** Behave (para pruebas móviles), JUnit (para pruebas de API)

📂 Evidencias
Los videos de ejecución de las pruebas se encuentran en el siguiente enlace: Videos de ejecución ([coloca el enlace aquí](https://www.transfernow.net/dl/20250131xOAbu5Dn)).

## 📁 Estructura del repositorio
```sh
Koombea_Challenge/
│── 📂 Koombea               # Proyecto de automatización móvil con Appium y Cucumber
│   │── 📂 features/         # Definición de escenarios en Gherkin
│   │── 📂 pages/            # Implementación del Page Object Model (POM)
│   │── 📂 tests/            # Casos de prueba con Behave
│   │── 📂 config/           # Configuración de Appium y WebDriver
│   │── 📄 requirements.txt  # Dependencias del proyecto móvil
│   │── 📄 README.md         # Explicación del módulo móvil
│
│── 📂 Koombea-api           # Proyecto de automatización de API con KarateDSL
│   │── 📂 src/test/java/com/koombea/tests/ # Pruebas de API en KarateDSL
│   │── 📄 karate-config.js  # Configuración global de Karate
│   │── 📄 pom.xml           # Gestión de dependencias con Maven
│   │── 📄 README.md         # Explicación del módulo API
│
│── 📄 .gitignore            # Archivos ignorados en el repositorio
│── 📄 README.md             # Documentación principal del proyecto

