# -- FILE: features/environment.py
# CONTAINS: driver fixture setup and teardown
from behave import fixture, use_fixture
from selenium.webdriver import Firefox

@fixture
def driver_firefox(context):
    # -- BEHAVE-FIXTURE: Similar to @contextlib.contextmanager
    context.driver = Firefox()
    yield context.driver
    # -- CLEANUP-FIXTURE PART:
    context.driver.quit() # Cierra la instancia de Firefox auto.
    # Aquí se podría poner el login si requerimos que todas las pruebas tienes que estar logueado.

def before_all(context):
    use_fixture(driver_firefox, context)
    # -- NOTE: CLEANUP-FIXTURE is called after after_all() hook.