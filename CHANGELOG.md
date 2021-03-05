## 2021-02-12
### Added
- Build the project layout following Nick Janetakis tutorial: blueprints/, static/, templates/, tests/, app.py, extensions.py, DockerFile.  
- Used my personal whiteboard to design an initial database shema following business idea and deployed a firt model with 2 tables.


## 2021-02-14
### Added
- Split the questions tables into 2 tables: questions / answers


## 2021-02-27 
### Added
- Mostly worked on the User module. 
- Wrote hasher.py file to handle password encryption and decryption methods
- Wrote validators.py file to store validations methods such as check if a password is strong enough and if a user already exist 


## 2021-02-28
### Added
- Mostly worked on the User module. 
- Separation of concerns: a User class to represent the user object, UserService to make opertions to the User and a UserRepository to interact with the database following a code review https://codereview.stackexchange.com/questions/256512/python-oop-web-app-flask-user-registration-class



## 2021-03-04
### Added
- Created a Forms class to handle all user forms to handle
- Created a testing folder and added basic unit tests

### Removed
- Docker files. I do not really to use Docker right now and build the project locally to speed up development



## 2021-03-05
### Added
- Added a bin folder to add shell scripts such as running test with coverage ```py.test --cov-report html --cov ```
- Added 2 badges on the Github repo: build and coverage