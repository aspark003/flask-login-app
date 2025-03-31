from flask import Flask, render_template, request
import csv
app2 = Flask(__name__)


file_path = "c:/Users/anton/school/family.csv"



def read_csv():
    with open(file_path, mode='r') as file:
        reader = csv.DictReader(file)
        data = []
        for row in reader:
            data.append(row)
        return data

@app2.route('/', methods=['GET'])

def search():
    family_data = read_csv()
    search_first = request.args.get('search_name')
    search_second = request.args.get('search_lastname')
    if search_first and search_second:
        family_data = [person for person in family_data if person['first_name'] == search_first and person['last_name'] == search_second]

    return render_template('new_page.html', family_data = family_data)

if __name__ == '__main__':
    app2.run(debug=True, port=5001)










