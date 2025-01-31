from behave import given, when, then
from pages.convert_page import ConvertPage
from config.desired_caps import get_driver
from selenium.common.exceptions import NoSuchElementException

@given("the user opens the conversion app")
def step_open_app(context):
    """Abre la app en el emulador"""
    context.driver = get_driver()
    context.convert_page = ConvertPage(context.driver)

@given('navigates to "Area" section')
def step_navigate_area(context):
    """Abre el menú y selecciona la sección de Área"""
    context.convert_page.open_menu()
    context.convert_page.select_area_section()

@given('navigates to "Volume" section')
def step_navigate_volume(context):
    """Abre el menú y selecciona la sección de Volume"""
    context.convert_page.open_menu()
    context.convert_page.select_volume_section()

@given('navigates to "Speed" section')
def step_navigate_speed(context):
    """Abre el menú y selecciona la sección de Speed"""
    context.convert_page.open_menu()
    context.convert_page.select_speed_section()

@given('navigates to "Acceleration" section')
def step_navigate_acceleration(context):
    context.convert_page.open_menu()
    context.convert_page.select_acceleration_section()

@when('the user selects "{unit}" as the input unit')
def step_select_input_unit(context, unit):
    """Selecciona la unidad de entrada en el selector"""
    context.convert_page.select_unit("input", unit)

@when('the user selects "{unit}" as the output unit')
def step_select_output_unit(context, unit):
    """Selecciona la unidad de salida en el selector"""
    context.convert_page.select_unit("output", unit)

@when('the user enters "{number}"')
def step_enter_number(context, number):
    """Simula la entrada de un número en la calculadora de la app"""
    context.convert_page.enter_number(number)

@then('the converted value should be "{expected_value}"')
def step_check_converted_value(context, expected_value):
    """Verifica que el número en la pantalla es el esperado"""
    converted_value = context.convert_page.get_converted_value()
    assert converted_value == expected_value, f"Expected {expected_value} but got {converted_value}"

@when("the user opens the input unit selector")
def step_open_input_selector(context):
    """Abre el selector de unidades de entrada"""
    context.convert_page.open_unit_selector("input")


@when('the user clicks the invert units button')
def step_impl(context):
    # Llama a la función que hicimos para invertir las unidades
    context.convert_page.invert_units()


@when("the user opens the output unit selector")
def step_open_output_selector(context):
    """Abre el selector de unidades de salida"""
    context.convert_page.open_unit_selector("output")

@then('the unit "{unit}" should be available')
def step_verify_unit_availability(context, unit):
    """Verifica que una unidad específica está en la lista de selección"""
    try:
        assert context.convert_page.is_unit_available(unit), f"Unit '{unit}' not found in the selector"
    except NoSuchElementException:
        assert False, f"Unit '{unit}' is NOT available in the list"