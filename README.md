# The console

[AUTHORS] (https://github.com/mwangiii/AirBnB_clone)

AirBnB clone This project is the first part of the AirBnB clone (HBnB) project for ALX SE students. The main objective of this project is to be an enrichment exercise to improve and apply concepts of higher-level programing done before and consists of implementing a specific command line interpreter to manage all of the functions and features of the project.

Requirements of the project To do this project we had to 
learn:

How to create a Python package How to create a command interpreter in Python using the cmd module What is Unit testing and how to implement it in a large project How to serialize and deserialize a Class How to write and read a JSON file How to manage datetime What is an UUID What is *args and how to use it What is **kwargs and how to use it How to handle named arguments in a function How to do a unittest The console This command line interpreter can:
Manage objects: create, update, destroy, etc... Retrieve an object from a file, a database etc... Do some operations on objects (count, compute stats, etc...) Update attributes of an object Getting started At first, you have to clone this repository in your machine using this command:

[git clone] (https://github.com/mwangiii/AirBnB_clone.git)

 Then, go inside it:

$ cd AirBnB_clone Finally, you can use the console this way:

$ ./console.py Usage Interactive mode

$ ./console.py

(hbnb) help
Documented commands (type help ):

EOF all count create destroy help quit show update

(hbnb) (hbnb) quit $ Non interactive mode

$ echo "help" | ./console.py
(hbnb) Documented commands (type help ):

EOF all count create destroy help quit show update

(hbnb) 
