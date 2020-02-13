# One-Minute-Pitch App

## Description

Pitch social is a web app developed using Python Flask, Postgressql and SQLAlchemy The app allows a user to create pitches for three categories Interview, Product and Promotion. The user can view comments made about a specific pitch and can also write comments for a specific pitch The user also has a profile page that display his/her pitches as well as upload a profile picture The application incorporates concepts of authentication system, ORM using SQLAlchemy, password hashing, migrations, unit testing and the Flask framework.

## Author

Samuel Aronda


## CodeBeats Badge

[![codebeat badge](https://codebeat.co/badges/14a53603-d0b5-4c04-9c28-14ccaa55f6aa)](https://codebeat.co/projects/github-com-arondasamuel123-pitchapp-master)



# Installation

## Clone
    Place your secret key, mail_username, mail_password in the start.sh
```bash
    git clone https://github.com/arondasamuel123/PitchApp.git
    
```
##  Create virtual environment
```bash
    python3.6 -m venv --without-pip
    
```
Activate virtual and install requirements.txt
```bash
   $ source virtual/bin/activate
   $ pip install - requirements.txt
    
```

## Run app
```bash
   $ ./start.sh
    
```

## Test class

```bash
    $ python3.6 serve.py test
```
## Known Bugs
I haven't implemented upvotes and downvotes functionality for pitches 

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## Technologies Used
    Python Shell
    Python 3.6
    Flask 
    Bootstrap
    HTML
    CSS
    PostgreSQL



## License
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)



