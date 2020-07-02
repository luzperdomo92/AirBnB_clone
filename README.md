<img align="left" width="100" height="90" src="https://images.squarespace-cdn.com/content/v1/52a11797e4b05f836261a40b/1520460989019-H2O2LTTNTO9B1UVP0UKC/ke17ZwdGBToddI8pDm48kOyctPanBqSdf7WQMpY1FsRZw-zPPgdn4jUwVcJE1ZvWQUxwkmyExglNqGp0IvTJZUJFbgE-7XRK3dMEBRBhUpzdDaU_bF7Ds5W9lU7yP8WpaBCM76uVnxdYD9Ka9eZj3NBMAuNC_ujA-eHPkEsGI2A/bello.gif?format=1500w">

# AirBnB clone - The console

This repository is  the first step of the simple copy of the AirBnB website. This project is about a command interpreter to manipulate data without a visual interface, like in a Shell (perfect for development and debugging) 

## The Console objective : 
-   Create your data model.
-   Manage (create, update, destroy, etc) objects via a console / command interpreter.
-   Store and persist objects to a file (JSON file).



## Getting started

1.  Clone all the repository in your terminal.
```
$ git@github.com:luzperdomo92/AirBnB_clone.git
```
3. Execute the program.
```
./console
```
You should see something like this:
```
(hbnb)
```


> **Note:** There are other way to run the program, in non-interactive mode by simply piping the commands into the shell executable.

```
$ echo "help" | ./console.py
```


## How used the console:

For run some command in the program, the syntax that you have to use is the same like a usual Shell. 

```
($) <command> <class name> <id> <attribute name> "<attribute value>"
```
**Example:**
```
(hbnb) create BaseModel
```
or
```
(hbnb) update BaseModel 49faff9a-6318-451f-87b6-910505c55907 first_name "Betty"
```


## Commands

This console  support  some commands:

- `create` - Creates a new instance.
- `show` - Prints the string representation of an instance.
- `destroy` - Deletes an instance.
- `all` - Prints all string representation of all instances.
- `update` - Updates an instance based.

Standard commands:

- `quit` - Exit the program
- `EOF` - Exit the program (ctrl + d) 
- `help` - Shows whats a command do

## Authors

- Adonis Tejeda.
- Luz A. Perdomo.
