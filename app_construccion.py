import mysql.connector
from flask import Flask,render_template,request,url_for,redirect,send_file
import sys
import csv
import pandas as pd

from db import db, rellenar_datos, cerrar_conexion
from io import BytesIO  # Importa BytesIO
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
df = pd.read_csv( 'informacion_ob.csv', encoding= 'unicode_escape')


# df = df.drop(columns=["Cap"])


df = df.drop_duplicates(keep=False, inplace=False)

df= df

precio_detalle1 = 308
precio_detalle2 = 170
precio_detalle3 = 212
precio_detalle4 = 68
precio_detalle5 = 65
precio_detalle6 = 240 

#   detalles 1
def precio_cal(detalle, cantidad):
     presio = 0
     if detalle == 1:
         presio=  precio_detalle1 *cantidad
     if detalle == 2:
         presio = precio_detalle2 * cantidad
     if  detalle ==3:
         presio = precio_detalle3 * cantidad
     if detalle == 4:
         presio = precio_detalle4 * cantidad
     if detalle == 5:
         presio =  precio_detalle5 * cantidad
     if detalle == 6:
         presio =  precio_detalle6  * cantidad    
     return presio

# Inicio  de página 
app = Flask(__name__)

@app.route("/")
def formulario():
    return render_template("index.html")

@app.route("/contacto",methods=['GET'])
# pagina contactos 
def contacto():
    return render_template("contacto.html")

@app.route("/contacto",methods=['POST'])  
def recibirDatosCliente():
    if request.method == 'POST':
        respuesta = request.form
      
        nom =respuesta['nom']
        exampleInputEmail1=respuesta['exampleInputEmail1']
        ident =respuesta['ident']
        area =respuesta['area']
        resultado=  rellenar_datos(nom,exampleInputEmail1, ident,area)
        cerrar_conexion() 
        return redirect(url_for("ex_pagina_exit"))
    else:
        return render_template("contacto.html")     

# pagina exito 
@app.route("/pagina_exit")
def ex_pagina_exit():
    return render_template("pagina_exit.html")    



# informaciones  inmobilario 
@app.route("/inmobilari")
def inmobilarios():
    data =  df
    return render_template("inmobilari.html",tables = [data.to_html()],titles=[''] )

    
# detalles1  inputNumber_mater1
@app.route("/presupuesto",methods=['POST','GET'])
def presupuesto():
    if request.method == 'POST':
        # detalle 1 
        detalle1 = request.form.get('detalles1')
        cantidad1 = request.form.get('inputNumber_mater1')
        respuest1 = precio_cal(int(detalle1),int(cantidad1))
        # detalle2 
        detalle2 = request.form.get('detalles2')
        cantidad2 = request.form.get('inputNumber_mater2')
        respuest2 = precio_cal(int(detalle2),int(cantidad2))
        # detalle 3
        detalle3 = request.form.get('detalles3')
        cantidad3 = request.form.get('inputNumber_mater3')
        respuest3 = precio_cal(int(detalle3),int(cantidad3))
        # detalle 4
        detalle4 = request.form.get('detalles4')
        cantidad4 = request.form.get('inputNumber_mater4')
        respuest4 = precio_cal(int(detalle4),int(cantidad4))
        # detalle 5
        detalle5 = request.form.get('detalles5')
        cantidad5 = request.form.get('inputNumber_mater5')
        respuest5 = precio_cal(int(detalle5),int(cantidad5))
        # detalle 6
        detalle6 = request.form.get('detalles6')
        cantidad6 = request.form.get('inputNumber_mater6')
        respuest6 = precio_cal(int(detalle6),int(cantidad6))

        total = respuest1+respuest2+respuest3+respuest4+respuest5+respuest6
        return redirect(url_for("result_presupuesto",respuest1=respuest1 ,respuest2=respuest2,respuest3=respuest3,respuest4=respuest4,respuest5=respuest5,respuest6=respuest6 ,total= total))
    else:
        return render_template("presupuesto.html")  


@app.route("/resultat_presupuesto",methods=['GET'])
def result_presupuesto():
    respuest1 = request.args.get('respuest1')
    respuest2 = request.args.get('respuest2')
    respuest3 = request.args.get('respuest3')
    respuest4 = request.args.get('respuest4')
    respuest5 = request.args.get('respuest5')
    respuest6 = request.args.get('respuest6')
    total = request.args.get('total')
    return render_template("resultado_presupuesto.html", respuest1=respuest1,respuest2=respuest2,respuest3=respuest3,respuest4=respuest4,respuest5=respuest5,respuest6=respuest6,total=total)     


@app.route("/servisio")
def servisio():
    return render_template("servisio.html") 

@app.route("/fotos")
def fotos():
    return render_template("fotos.html") 
@app.route("/videos")
def videos():
    return render_template("videos.html") 
    
    
    
@app.route('/descargar_presupuesto',methods=['GET', 'POST'])
def descargar_presupuesto():
    # Crear el archivo PDF
    response = generate_pdf()
    
    return response

def generate_pdf():
    respuest1 = request.form.get('respuest1')
    respuest2 = request.form.get('respuest2')
    respuest3 = request.form.get('respuest3')
    respuest4 = request.form.get('respuest4')
    respuest5 = request.form.get('respuest5')
    respuest6 = request.form.get('respuest6')
    total = request.form.get('total')
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter)
    styles = getSampleStyleSheet()

    elements = []

    elements.append(Paragraph("Presupuesto de consulta", styles['Title']))

    details = [
        ["Detalle", "Precio"],
        ["Lavabo con mueble, espejo y aplique incluido", "€" + (respuest1 or "N/A")],
        ["Inodoro", "€" + (respuest2 or "N/A")],
        ["Plato de ducha", "€" + (respuest3 or "N/A")],
        ["Grifería lavabo", "€" + (respuest4 or "N/A")],
        ["Mampara Ducha panel fijo", "€" + (respuest5 or "N/A")],
        ["Instalación de sanitarios y griferia", "€" + (respuest6 or "N/A")],
        ["TOTAL", "€" + (total or "N/A")]
    ]

    table = Table(details, colWidths=[300, 100])
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]))
    elements.append(table)

    doc.build(elements)
    buffer.seek(0)
    
    # Devolver el PDF generado
    return send_file(buffer, as_attachment=True, download_name='presupuesto.pdf', mimetype='application/pdf')
    
if __name__ == "__main__":
    app.run(host='localhost',port=5000,debug=True)