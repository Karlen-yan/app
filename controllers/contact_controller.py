# app/controllers/contact_controller.py
from flask import render_template, redirect, url_for, request
from app.models.contact_model import Contact

def formulario():
    return render_template("index.html")

def recibir_datos_cliente():
    if request.method == 'POST':
        respuesta = request.form
        nom = respuesta['nom']
        email = respuesta['exampleInputEmail1']
        ident = respuesta['ident']
        area = respuesta['area']
        
        contact = Contact(nom, email, ident, area)
        contact.save()
        
        return redirect(url_for("ex_pagina_exit"))
    else:
        return render_template("contacto.html")
