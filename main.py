import sqlite3

with sqlite3.connect("animal.db") as content:
    cursor = content.cursor()
    info = """
    CREATE TABLE IF NOT EXISTS animals_test (
    id integer PRIMARY KEY AUTOINCREMENT,
    name_animal varchar(20),
    animal_id varchar(7),
    type_id integer,
    breed_id integer,
    main_color_id integer,
    additional_color_id integer,
    date_of_birth date,
    outcome_id integer,
    FOREIGN KEY (outcome_id) REFERENCES outcome_animals(id)
    )
           """
    cursor.execute(info)
    cursor.fetchall()


with sqlite3.connect("animal.db") as content:
    cursor = content.cursor()
    info = """
    CREATE TABLE IF NOT EXISTS type_animals (
    id integer PRIMARY KEY AUTOINCREMENT,
    type_animal varchar(20),
    FOREIGN KEY (id) REFERENCES animals_test(type_id)
    )
           """
    cursor.execute(info)
    cursor.fetchall()


with sqlite3.connect("animal.db") as content:
    cursor = content.cursor()
    info = """
    CREATE TABLE IF NOT EXISTS breeds (
    id integer PRIMARY KEY AUTOINCREMENT,
    breed_animal varchar(50),
    FOREIGN KEY (id) REFERENCES animals_test(breed_id)
    )
           """
    cursor.execute(info)
    cursor.fetchall()


with sqlite3.connect("animal.db") as content:
    cursor = content.cursor()
    info = """
    CREATE TABLE IF NOT EXISTS main_colors (
    id integer PRIMARY KEY AUTOINCREMENT,
    color_animal varchar(50),
    FOREIGN KEY (id) REFERENCES animals_test(color_id)
    )
           """
    cursor.execute(info)
    cursor.fetchall()


with sqlite3.connect("animal.db") as content:
    cursor = content.cursor()
    info = """
    CREATE TABLE IF NOT EXISTS additional_colors (
    id integer PRIMARY KEY AUTOINCREMENT,
    color_animal varchar(50),
    FOREIGN KEY (id) REFERENCES animals_test(color_id)
    )
           """
    cursor.execute(info)
    cursor.fetchall()


with sqlite3.connect("animal.db") as content:
    cursor = content.cursor()
    info = """
    CREATE TABLE IF NOT EXISTS outcome_animals (
    id integer PRIMARY KEY AUTOINCREMENT,
    subtype varchar(50), 
    age_upon_outcome varchar(50),
    month_outcome integer,
    year_outcome integer,
    type_outcome varchar(50)
    )
           """
    cursor.execute(info)
    cursor.fetchall()


with sqlite3.connect("animal.db") as content:
    cursor = content.cursor()
    info = """
    INSERT INTO animals_test (name_animal, animal_id, type_id, breed_id,
    main_color_id, additional_color_id, date_of_birth)
    SELECT animals.name, animals.animal_id, type_animals.id, breeds.id,
    main_colors.id, additional_colors.id, animals.date_of_birth
    FROM animals
    LEFT JOIN type_animals
    ON type_animals.type_animal = animals.animal_type
    LEFT JOIN breeds
    ON breeds.breed_animal = animals.breed
    LEFT JOIN main_colors
    ON main_colors.color_animal = animals.color1
    LEFT JOIN additional_colors
    ON additional_colors.color_animal = animals.color2
           """
    cursor.execute(info)
    cursor.fetchall()


with sqlite3.connect("animal.db") as content:
    cursor = content.cursor()
    info = """
    INSERT INTO animals_test (color_id)
    SELECT colors.id
    FROM colors
    LEFT JOIN animals
    ON animals.color1 = colors.color_animal
    AND animals.color2 = colors.color_animal
           """
    cursor.execute(info)
    cursor.fetchall()


with sqlite3.connect("animal.db") as content:
    cursor = content.cursor()
    info = """
    INSERT INTO outcome_animals (subtype, age_upon_outcome, month_outcome, year_outcome, type_outcome)
    SELECT outcome_subtype, age_upon_outcome, outcome_month, outcome_year, outcome_type
    FROM animals
           """
    cursor.execute(info)
    cursor.fetchall()


with sqlite3.connect("animal.db") as content:
    cursor = content.cursor()
    info = """
    UPDATE animals
    SET color1 = TRIM(color1),
        color2 = TRIM(color2)
           """
    cursor.execute(info)
    cursor.fetchall()


with sqlite3.connect("animal.db") as content:
    cursor = content.cursor()
    info = """
    INSERT INTO main_colors (color_animal)
    SELECT DISTINCT color1
    FROM animals
           """
    cursor.execute(info)
    cursor.fetchall()


with sqlite3.connect("animal.db") as content:
    cursor = content.cursor()
    info = """
    INSERT INTO additional_colors (color_animal)
    SELECT DISTINCT color2
    FROM animals
           """
    cursor.execute(info)
    cursor.fetchall()


with sqlite3.connect("animal.db") as content:
    cursor = content.cursor()
    info = """
    INSERT INTO type_animals (type_animal)
    SELECT DISTINCT animal_type
    FROM animals
           """
    cursor.execute(info)
    cursor.fetchall()


with sqlite3.connect("animal.db") as content:
    cursor = content.cursor()
    info = """
    INSERT INTO breeds (breed_animal)
    SELECT DISTINCT breed
    FROM animals
           """
    cursor.execute(info)
    cursor.fetchall()


with sqlite3.connect("animal.db") as content:
    cursor = content.cursor()
    info = """
    CREATE TABLE IF NOT EXISTS animals_new (
    id integer PRIMARY KEY AUTOINCREMENT,
    name_animal varchar(20),
    animal_id varchar(7),
    type_id integer,
    breed_id integer,
    main_color_id integer,
    additional_color_id integer,
    date_of_birth date,
    outcome_id integer,
    FOREIGN KEY (outcome_id) REFERENCES outcome_animals(id)
    )
           """
    cursor.execute(info)
    cursor.fetchall()


with sqlite3.connect("animal.db") as content:
    cursor = content.cursor()
    info = """
    INSERT INTO animals_new (name_animal, animal_id, type_id, breed_id,
     main_color_id, additional_color_id, date_of_birth, outcome_id)
    SELECT animals_test.name_animal, animals_test.animal_id, animals_test.type_id, animals_test.breed_id, 
    animals_test.main_color_id, animals_test.additional_color_id, animals_test.date_of_birth, outcome_animals.id
    FROM animals_test
    LEFT JOIN outcome_animals
    ON animals_test.id = outcome_animals.id
           """
    cursor.execute(info)
    cursor.fetchall()
