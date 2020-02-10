from behave import given, when, then
from selenium import webdriver
from unittest import TestCase

@given(u'que ingreso a la lista de dinosaurios')
def step_impl(context):
    driver = webdriver.Firefox()
    driver.get('http://192.168.33.15:8000/periodo/dinos')
    context.driver = driver

@given(u'busco el dinosaurio por nombre llamado "{nombre_dino}"')
def step_impl(context, nombre_dino):
    rows = context.driver.find_elements_by_tag_name('tr')
    dinosaurios = []
    for row in rows[1:]:
        td_dino = row.find_elements_by_tag_name('td')
        dinosaurios.append(td_dino[1].text)
    context.td_dino = td_dino
    test = TestCase()
    test.assertIn(nombre_dino, dinosaurios)

@when(u'presiono el botón eliminar')
def step_impl(context):
    #context.driver.find_element_by_class_name('btn-primary').click()
    buttons = context.td_dino[5].find_element_by_class_name('btn-danger')
    print(buttons) 
    #boton_eliminar = []
    #for button in buttons:
    #    delete_button = button.find_elements_by_tag_name('a')
    #    boton_eliminar.append(delete_button[1]) 

    #boton_eliminar[1].click()
    buttons.click()

@when(u'confirmo presionando el botón eliminar')
def step_impl(context):
    context.driver.find_element_by_class_name('btn-danger').click()

@then(u'puedo ver que el dinosaurio "{nombre}" ya no se encuentra en la lista de dinosaurios')
def step_impl(context, nombre):
    rows = context.driver.find_elements_by_tag_name('tr')
    dinosaurios = []
    for row in rows[1:]:
        td_dino = row.find_elements_by_tag_name('td')
        dinosaurios.append(td_dino[1].text)
    
    test = TestCase()
    test.assertNotIn(nombre, dinosaurios)
    #test.assertIn(nombre, dinosaurios)

