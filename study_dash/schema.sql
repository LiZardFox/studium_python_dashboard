DROP TABLE IF EXISTS attempt;
DROP TABLE IF EXISTS evaluation;
DROP TABLE IF EXISTS enrollment;
DROP TABLE IF EXISTS program_module;
DROP TABLE IF EXISTS program;
DROP TABLE IF EXISTS module;
DROP TABLE IF EXISTS student;

CREATE TABLE student (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  first_name VARCHAR NOT NULL,
  last_name VARCHAR NOT NULL,
  matrikel_nr VARCHAR UNIQUE NOT NULL,
  password TEXT NOT NULL
);

CREATE TABLE module (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name VARCHAR NOT NULL
);

CREATE TABLE program (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name VARCHAR NOT NULL
);


CREATE TABLE program_module (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  program_id INTEGER NOT NULL,
  module_id INTEGER NOT NULL,
  sort INTEGER NOT NULL DEFAULT 0,
  FOREIGN KEY (program_id) REFERENCES program (id),
  FOREIGN KEY (module_id) REFERENCES module (id)
);

CREATE TABLE enrollment (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  program_id INTEGER NOT NULL,
  student_id INTEGER NOT NULL,
  semesters INTEGER NOT NULL,
  start_date TIMESTAMP NOT NULL,
  end_date TIMESTAMP NOT NULL,
  target_grade FLOAT,
  target_end_date TIMESTAMP,
  FOREIGN KEY (program_id) REFERENCES program (id),
  FOREIGN KEY (student_id) REFERENCES student (id)
);

CREATE TABLE evaluation (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  module_id INTEGER NOT NULL,
  type VARCHAR NOT NULL,
  max_score INTEGER NOT NULL,
  max_attempt INTEGER NOT NULL,
  weight, FLOAT NOT NULL DEFAULT 1,
  FOREIGN KEY (module_id) REFERENCES module (id)
);


CREATE TABLE attempt (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  enrollment_id INTEGER NOT NULL,
  evaluation_id INTEGER NOT NULL,
  date_of_attempt TIMESTAMP,
  score INTEGER,
  grade INTEGER,
  FOREIGN KEY (enrollment_id) REFERENCES enrollment (id),
  FOREIGN KEY (evaluation_id) REFERENCES evaluation (id)
);

