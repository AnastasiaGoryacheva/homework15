from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False


@app.route("/<int:itemid>/")
def search_animals_id(itemid):
    with sqlite3.connect("animal.db") as content:
        cursor = content.cursor()
        info = f"""
            SELECT animals_new.id, animals_new.name_animal, animals_new.animal_id,
            type_animals.type_animal, breeds.breed_animal,
            main_colors.color_animal AS 'main_color',
            additional_colors.color_animal AS 'additional_color',
            animals_new.date_of_birth, outcome_animals.subtype,
            outcome_animals.age_upon_outcome, outcome_animals.month_outcome,
            outcome_animals.year_outcome, outcome_animals.type_outcome
            FROM animals_new
            LEFT JOIN type_animals ON type_animals.id = animals_new.type_id
            LEFT JOIN breeds ON breeds.id = animals_new.breed_id
            LEFT JOIN main_colors ON main_colors.id = animals_new.main_color_id
            LEFT JOIN additional_colors ON additional_colors.id = animals_new.additional_color_id
            LEFT JOIN outcome_animals ON outcome_animals.id = animals_new.outcome_id
            WHERE animals_new.id = {itemid}
        """
        cursor.execute(info)
        result = cursor.fetchall()
        result_json = {
            "name_animal": result[0][1],
            "animal_id": result[0][2],
            "type_animal": result[0][3],
            "breed_animal": result[0][4],
            "main_color": result[0][5],
            "additional_color": result[0][6],
            "date_of_birth": result[0][7],
            "subtype": result[0][8],
            "age_upon_outcome": result[0][9],
            "year_outcome": result[0][10],
            "month_outcome": result[0][11],
            "type_outcome": result[0][12],
        }
        return jsonify(result_json)


app.run()
