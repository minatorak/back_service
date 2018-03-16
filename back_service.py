from flask import Flask, render_template, request, jsonify

from common.database import Database
from models.crawlerDisease import Crawlerdisease
from models.medicine import Medicine

app = Flask(__name__)

@app.before_first_request
def initialize_database():
    Database.initialize()
    Database.dropCollection('disease')
    Crawlerdisease.get_data()


@app.route('/')
def home_add():
    return render_template('add_data.html')

@app.route('/confirm', methods=['POST'])
def db_show():
    name = request.form['name']
    type = request.form.get('type')
    medicine_for = request.form['medicine_for']
    medicine_facts = request.form['medicine_facts']
    medicine_use = request.form['medicine_use']
    medicine_risk = request.form['medicine_risk']
    medicine_store = request.form['medicine_store']
    Medicine.new_medicine(name=name,
                          type_medicine=type,
                          medicine_facts=medicine_facts,
                          medicine_for=medicine_for,
                          medicine_risk=medicine_risk,
                          medicine_use=medicine_use,
                          medicine_store=medicine_store)
    medicines = Medicine.from_mongo()
    return render_template('show_all.html', medicines=medicines)

@app.route('/all/medicine/',methods=['GET'])
def get_all_medicine():
    medicines = Medicine.from_mongo()
    listmedicines = []
    for medicine in medicines:
        med = Medicine.re_data(medicine)
        listmedicines.append(med)
    return jsonify({'medicine':listmedicines})


@app.route('/all/disease/',methods=['GET'])
def get_all_disease():
    disease = Crawlerdisease.from_mongo()
    listdisease = []
    for data in disease:
        med = Crawlerdisease.re_data(data)
        listdisease.append(med)
    return jsonify({'disease':listdisease})

if __name__ == '__main__':
    app.run()


