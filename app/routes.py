from app import app
from flask import render_template
import json
import os
from flask import request


@app.route('/about')
def about():
    return render_template('about.html.jinja')

@app.route('/base')
def home():
    return render_template('base.html.jinja')

@app.route('/extract', methods=['GET', 'POST'])
def extract():
    # Pobierz wartość przycisku z formularza
    selected_product = request.form.get('product')

    # Sprawdź czy produkt został wybrany
    if selected_product is None:
        return render_template('extract.html.jinja')

    # Wybierz odpowiednią ścieżkę do pliku JSON w zależności od produktu
    if selected_product == 'product1':
        file_path = "C:\\Users\\Adrian\\Pan_Tadeusz_1\\ceeno\\34953634_opinions.json"
    elif selected_product == 'product2':
        file_path = "C:\\Users\\Adrian\\Pan_Tadeusz_1\\ceeno\\163090065_opinions.json"
    elif selected_product == 'product3':
        file_path = "C:\\Users\\Adrian\\Pan_Tadeusz_1\\ceeno\\138265678_opinions.json"
    elif selected_product == 'product4':
        file_path = "C:\\Users\\Adrian\\Pan_Tadeusz_1\\ceeno\\164649380_opinions.json"
    else:
        return "Niepoprawny produkt"

    # Obsługa braku pliku JSON
    if os.path.exists(file_path):
        # Odczytaj opinie z pliku JSON
        with open(file_path, "r", encoding="utf-8") as json_file:
            product = json.load(json_file)
        return render_template('extract.html.jinja', product=product)
    else:
        return "Brak pliku JSON"



@app.route('/list')
def list():
    return render_template('list.html.jinja')
