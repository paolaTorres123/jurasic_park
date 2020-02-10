from behave import given, when, then
from selenium import webdriver
from unittest import TestCase

@given(u'que ingreso a la lista de dinosaurios existentes')
def step_impl(context):
    driver = webdriver.Firefox()
    driver.get('http://192.168.33.15:8000/periodo/dinos')
    context.driver = driver

@given(u'busco el dinosaurio por su nombre llamado "{nombre_dino}"')
def step_impl(context, nombre_dino):
    rows = context.driver.find_elements_by_tag_name('tr')
    dinosaurios = []
    for row in rows[1:]:
        td_dino = row.find_elements_by_tag_name('td')
        dinosaurios.append(td_dino[1].text)
    context.td_dino = td_dino
    test = TestCase()
    test.assertIn(nombre_dino, dinosaurios)

@when(u'presiono el botón editar')
def step_impl(context):
    buttons = context.td_dino[5].find_element_by_class_name('btn-success')
    buttons.click()

@when(u'modifico los datos de nombre a : "{nuevo_nombre_dino}"')
def step_impl(context, nuevo_nombre_dino):
    context.driver.find_element_by_id('id_nombre').clear()
    context.driver.find_element_by_id('id_nombre').send_keys(nuevo_nombre_dino)

@when(u'presiono el botón guardar')
def step_impl(context):
    context.driver.find_element_by_class_name('btn-primary').click()

@then(u'puedo ver la modificación que le hice al dinosaurio en su nombre por "{nuevo_nombre_dino}" en la lista de dinosaurios')
def step_impl(context, nuevo_nombre_dino):
    rows = context.driver.find_elements_by_tag_name('tr')
    dinos = [row.find_elements_by_tag_name('td')[1].text for row in rows[1:]]
    test = TestCase()
    test.assertIn(nuevo_nombre_dino,dinos)
        
