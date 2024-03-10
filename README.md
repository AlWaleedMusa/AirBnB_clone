![Example Image](images/hbnb.png "HBNB Logo")

# HBNB Project (AirBnB clone - The console)

The HBNB project is a simple implementation of an **AirBnB** platform where users can manage, create, and book accommodations, Through a *console* It is developed as part of the ALX SE Program as a learning project, aiming to demonstrate proficiency in Python, object-oriented programming, database management, and web development.

# Execution
The console works both in interactive mode and non-interactive mode, much like a Unix shell. It prints a prompt (hbnb) and waits for the user for input.

- interactive mode

| Command                   | Description |
|---------------------------|-------------|
|```python console.py```    | *Run the console* |
|```(hbnb) help <command>```       | *Show help of the command*    |
|```(hbnb) quite```         | *Quit the console*|
|```(hbnb) create <class>```| *Create an Object and (print it ID)*|
|```(hbnb) show <class> <id>``` or ```(hbnb) <class>.show(<id>)```| *Show an Object*|
|```(hbnb) destroy <class> <id>``` or ```(hbnb) <class>.destroy(<id>)```| *Destroy an Object*|
|```(hbnb) all``` or ```(hbnb) all <class>```| *Show all objects, or all instances of a class*|

<hr>
<br>

- non-interactive mode

```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```
<br>

# Models
in the Folder **Model** You will find all these Classes used in this project

| Model                     | Description | Attr |
|---------------------------|-------------|------|
|[base_model.py](models/base_model.py)|Base class to all other models|ID, Created_at, Updated_at|
|[user.py](models/user.py)| User information |Email, Password, First_name, Last_name|
|[amenity.py](models/amenity.py)|Amenity information|Name|
|[city.py](models/city.py)|City information|State_id, Name|
|[state.py](models/state.py)|State information|Name|
|[place.py](models/place.py)|Place information|City_id, User_id, Name, Description, Number_rooms, Number_bathrooms, Max_guest, Price_by_night, Latitude, Longitude, Amenity_ids|
|[review.py](models/review.py)|User/Place Reviews information|Place_id, User_id, Text|
<br>

# Authors

[AlWaleed Musa](https://github.com/AlWaleedMusa) A mobile repair technician eager to transition my career to web development through the ALX program.
