from selenium.common.exceptions import StaleElementReferenceException, TimeoutException, NoSuchElementException
from pages.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ConvertPage(BasePage):
    INPUT_FIELD = (AppiumBy.ID, "com.ba.universalconverter:id/source_value")
    OUTPUT_FIELD = (AppiumBy.ID, "com.ba.universalconverter:id/target_value")
    MENU_BUTTON = (AppiumBy.XPATH, "//android.widget.ImageButton[@content-desc='Open navigation drawer']")

    AREA_OPTION = (AppiumBy.XPATH, "//android.widget.TextView[@text='Area']")
    VOLUME_OPTION = (AppiumBy.XPATH, "//android.widget.TextView[@text='Volume']")
    SPEED_OPTION = (AppiumBy.XPATH, "//android.widget.TextView[@text='Speed']")
    ACCELERATION_OPTION = (AppiumBy.XPATH, "//android.widget.TextView[@text='Acceleration']")


    UNIT_SELECTOR = {
        "input": (AppiumBy.XPATH, "(//android.widget.Spinner)[1]"),
        "output": (AppiumBy.XPATH, "(//android.widget.Spinner)[2]")
    }

    UNIT_LIST = (AppiumBy.ID, "android:id/select_dialog_listview")

    def get_unit_locator(self, unit):
        """Retorna el localizador correcto de una unidad según el texto"""
        return (AppiumBy.ANDROID_UIAUTOMATOR,
                f'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().text("{unit}"))')

    def open_menu(self):
        """Asegura que el menú esté abierto antes de continuar"""
        for _ in range(2):
            try:
                WebDriverWait(self.driver, 3).until(
                    EC.presence_of_element_located(self.MENU_BUTTON)
                )
                self.click(self.MENU_BUTTON)
                break
            except:
                self.driver.press_keycode(4)  # Presiona BACK si el menú no aparece

    def select_area_section(self):
        """Hace scroll en el menú lateral y selecciona la opción 'Area'"""
        for _ in range(3):
            try:

                print("🔄 Intentando encontrar 'Volume' con scroll automático...")
                self.driver.find_element(
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().text("Area"))'
                )
                WebDriverWait(self.driver, 2).until(
                    EC.presence_of_element_located(self.AREA_OPTION)
                )
                self.click(self.AREA_OPTION)
                return  
            except (NoSuchElementException, TimeoutException):
                print("⚠ No se encontró con scroll automático, intentando swipe manual...")
                self.driver.swipe(100, 1200, 100, 400, 800)
                WebDriverWait(self.driver, 2).until(
                    EC.presence_of_element_located(self.AREA_OPTION)
                )

    def select_volume_section(self):
        """Hace scroll en el menú lateral y selecciona la opción 'Volume'"""
        for _ in range(3):  
            try:
                print("🔄 Intentando encontrar 'Volume' con scroll automático...")
                self.driver.find_element(
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().text("Volume"))'
                )
                WebDriverWait(self.driver, 2).until(
                    EC.presence_of_element_located(self.VOLUME_OPTION)
                )
                self.click(self.VOLUME_OPTION)
                return 
            except (NoSuchElementException, TimeoutException):
                print("⚠ No se encontró con scroll automático, intentando swipe manual...")
                self.driver.swipe(100, 1200, 100, 400, 800)
                WebDriverWait(self.driver, 2).until(
                    EC.presence_of_element_located(self.VOLUME_OPTION)
                )

    def select_speed_section(self):
        """Hace scroll en el menú lateral y selecciona la opción 'Speed'"""
        for _ in range(3): 
            try:
                print("🔄 Intentando encontrar 'Speed' con scroll automático...")
                self.driver.find_element(
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().text("Speed"))'
                )
                WebDriverWait(self.driver, 2).until(
                    EC.presence_of_element_located(self.SPEED_OPTION)
                )
                self.click(self.SPEED_OPTION)
                return  
            except (NoSuchElementException, TimeoutException):
                print("⚠ No se encontró con scroll automático, intentando swipe manual...")
                self.driver.swipe(100, 1200, 100, 400, 800)
                WebDriverWait(self.driver, 2).until(
                    EC.presence_of_element_located(self.SPEED_OPTION)
                )

        print("⚠ No se pudo encontrar 'Speed' después de hacer scroll.")
        raise TimeoutException("No se encontró la opción 'Speed' en el menú.")

    def select_acceleration_section(self):
        """Hace scroll en el menú lateral y selecciona la opción 'Acceleration'"""
        for _ in range(3):  
            try:
                print("🔄 Intentando encontrar 'Acceleration' con scroll automático...")
                self.driver.find_element(
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().text("Acceleration"))'
                )
                WebDriverWait(self.driver, 2).until(
                    EC.presence_of_element_located(self.ACCELERATION_OPTION)
                )
                self.click(self.ACCELERATION_OPTION)
                return 
            except (NoSuchElementException, TimeoutException):
                print("⚠ No se encontró con scroll automático, intentando swipe manual...")
                self.driver.swipe(100, 1200, 100, 400, 800)
                WebDriverWait(self.driver, 2).until(
                    EC.presence_of_element_located(self.ACCELERATION_OPTION)
                )


        print("⚠ No se pudo encontrar 'Acceleration' después de hacer scroll.")
        raise TimeoutException("No se encontró la opción 'Acceleration' en el menú.")


    def select_unit(self, field, unit):
        """Abre el selector y elige la unidad correspondiente"""
        for _ in range(3): 
            try:
                self.click(self.UNIT_SELECTOR[field])
                
                WebDriverWait(self.driver, 5).until(
                    EC.presence_of_element_located(self.UNIT_LIST)
                )

                unit_locator = self.get_unit_locator(unit)

                WebDriverWait(self.driver, 5).until(
                    EC.element_to_be_clickable(unit_locator)
                )
                self.click(unit_locator)

                WebDriverWait(self.driver, 5).until_not(
                    EC.presence_of_element_located(self.UNIT_LIST)
                )
                return 
            except StaleElementReferenceException:
                print(f"⚠ Elemento '{field}' perdió referencia en el DOM, reintentando...")

        raise TimeoutException(f"No se pudo seleccionar la unidad '{unit}' después de varios intentos.")

    def enter_number(self, number):
        """Ingresa un número usando la calculadora"""
        for digit in str(number):
            for _ in range(3):
                try:
                    button = WebDriverWait(self.driver, 2).until(
                        EC.presence_of_element_located((AppiumBy.XPATH, f"//android.widget.Button[@text='{digit}']"))
                    )
                    button.click()
                    break
                except (StaleElementReferenceException, TimeoutException):
                    continue

    def get_converted_value(self):
        """Obtiene el valor convertido"""
        return self.driver.find_element(*self.OUTPUT_FIELD).text

    def invert_units(self):
        """Hace clic en el botón que invierte las unidades de entrada y salida"""
        print("🔄 Invirtiendo unidades...")
        invert_button = (AppiumBy.XPATH, '(//android.widget.ImageButton[@content-desc="Swap units"])[2]')

        try:
            WebDriverWait(self.driver, 3).until(
                EC.element_to_be_clickable(invert_button)
            ).click()
            print("✅ Unidades invertidas correctamente.")
        except TimeoutException:
            print("❌ No se pudo hacer clic en el botón de invertir unidades.")
            raise
