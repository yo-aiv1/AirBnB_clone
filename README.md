![N|Solid](https://i.postimg.cc/rsmnnH50/65f4a1dd9c51265f49d0.png)

# 0x00. AirBnB clone - The console

# Description
This the first step to create a command interpreter to manage your AirBnB objects and it calls the console, it allows the users to manage the entities of the system using the commands explained in this manual.
The users like the administrator of the Airbnb clone has the posibility of the creating and updating and managing objects and data of the application, those objects are:
 
 * Users
 * Places
 * States
 * Cities
 * Amenities
 * Reviews

This abstraction will also allow you to change the type of storage easily without updating all of your codebase.
The console will be a tool to validate this storage engine.

![N|Solid](https://i.postimg.cc/65PSSBj9/815046647d23428a14ca.png)

# How to use the console:

To use the console:
* you can start by running the console.py file:
    ```bash
    ~/AirBnB_clone$ ./console.py
    (hbnb) 
    ```

* `(hbnb) help`: this is the help command or it can be used next to one of the command for further help:
    ```bash
    (hbnb) help
    
    Documented commands (type help <topic>):
    ========================================
    EOF  all  create  destroy  help  quit  show  update
    
    (hbnb)
    ```
* `(hbnb) create <Model's name>`: this command can be used to create a model, it returns model's id:
    ```bash
    (hbnb) create BaseModel
    3fc9cd65-b9cb-4895-bfe1-8b63877f0583
    (hbnb)
    ```
* `(hbnb) all <Model's name>`: this command can be used to display all the existent models:
    ```bash
    (hbnb) all BaseModel
    ["[BaseModel] (3fc9cd65-b9cb-4895-bfe1-8b63877f0583) {'id': '3fc9cd65-b9cb-4895-bfe1-8b63877f0583', 'created_at': datetime.datetime(2023, 12, 9, 22, 21, 32, 216883), 'updated_at': datetime.datetime(2023, 12, 9, 22, 21, 32, 216883)}"]
    (hbnb)
    ```
* `(hbnb) show <Model's name> <model's id> `: this command follow by the id of the model, display only the content of that specific model:
    ```bash
    (hbnb) show BaseModel 3fc9cd65-b9cb-4895-bfe1-8b63877f0583
    [BaseModel] (3fc9cd65-b9cb-4895-bfe1-8b63877f0583) {'id': '3fc9cd65-b9cb-4895-bfe1-8b63877f0583', 'created_at': datetime.datetime(2023, 12, 9, 22, 21, 32, 216883), 'updated_at': datetime.datetime(2023, 12, 9, 22, 21, 32, 216883)}
    (hbnb)
    ```
* `(hbnb) destroy <model's name> <instance's id>`: this command can delete a model using it's instance id.
    ```bash
    (hbnb) destroy User 3fc9cd65-b9cb-4895-bfe1-8b63877f0583
    (hbnb) 
    ```
* `(hbnb) update BaseModel <model's id> <attribute>: <the new value>`: this command can be used to update the value of an attribute using it's id.

* `(hbnb) quit`: this command can be used to exit the console.
    ```bash
    (hbnb) quit

    ~/AirBnB_clone$ 
    ```
## AUTHORS
 
* **Zak Haouzan** - [zakariasan](https://github.com/zakariasan)
* **Yahya Oulha** - [yo-aiv1](https://github.com/yo-aiv1)