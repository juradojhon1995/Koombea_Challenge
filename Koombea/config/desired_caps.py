from appium import webdriver
from appium.options.android import UiAutomator2Options

def get_driver():
    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.device_name = "emulator-5554"  # Asegúrate de que este sea el nombre correcto del emulador
    options.app = "C:/Users/j-hon/AndroidStudioProjects/Koombea/PreciseUnitConversion.apk"
    options.automation_name = "UiAutomator2"

    return webdriver.Remote("http://127.0.0.1:4723", options=options)

