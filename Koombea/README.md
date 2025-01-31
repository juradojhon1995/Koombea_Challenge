🏆 Koombea Challenge
Este repositorio contiene la solución a la prueba técnica de Koombea, la cual incluye:

📱 Automatización de pruebas móviles con Appium y Cucumber para una aplicación de conversión de unidades.
🌐 Automatización de pruebas de API usando KarateDSL para la API de Rick and Morty.
📌 Requisitos
🔧 Herramientas utilizadas:
Lenguaje: Python para la automatización móvil, Java para la automatización de APIs.
Automatización Móvil: Appium, Cucumber, Selenium.
Automatización de API: KarateDSL.
Patrones de Diseño: Page Object Model (POM).
Gestión de dependencias: pip para Python y Maven para Java.
Ejecutor de pruebas: Behave para pruebas móviles, JUnit para pruebas de API.
📂 Estructura del repositorio
bash
Copiar
Editar
📂 Koombea_Challenge
 ├── 📂 Koombea             # Proyecto de automatización móvil con Appium y Cucumber
 │   ├── features/         # Definición de escenarios de pruebas con Cucumber (Gherkin)
 │   ├── pages/            # Implementación de Page Object Model (POM)
 │   ├── tests/            # Casos de prueba y ejecución con Behave
 │   ├── config/           # Configuración de Appium y WebDriver
 │   ├── requirements.txt  # Dependencias del proyecto
 │   ├── README.md         # Explicación del módulo móvil
 │
 ├── 📂 Koombea-api         # Proyecto de automatización de API con KarateDSL
 │   ├── src/test/java/com/koombea/tests/  # Pruebas de API en KarateDSL
 │   ├── karate-config.js  # Configuración global de Karate
 │   ├── pom.xml           # Gestión de dependencias con Maven
 │   ├── README.md         # Explicación del módulo API
 │
 ├── .gitignore            # Archivos ignorados en el repositorio
 ├── README.md             # Documentación principal del proyecto
🚀 Cómo ejecutar las pruebas
📱 Automatización Móvil (Appium + Cucumber)
1️⃣ Instalación de dependencias
bash
Copiar
Editar
cd Koombea
pip install -r requirements.txt
2️⃣ Iniciar Appium Server
bash
Copiar
Editar
appium
3️⃣ Ejecutar las pruebas
bash
Copiar
Editar
behave features/
🌐 Automatización de APIs (KarateDSL)
1️⃣ Instalación de dependencias
bash
Copiar
Editar
cd Koombea-api
mvn clean install
2️⃣ Ejecutar las pruebas
bash
Copiar
Editar
mvn test
📸 Evidencias
Puedes encontrar los videos de ejecución de las pruebas en el siguiente enlace:
📌 Videos de ejecución

