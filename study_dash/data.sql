INSERT INTO student (first_name, last_name, matrikel_nr, password)
VALUES
  ('Max', 'Mustermann', 'IU123456789', 'scrypt:32768:8:1$rUHVsMDDipqbfmnt$15a9db76a5f0707a2cf37929cb6515e79b99d7365dfd0b5870c47643639ea435ed181d40de7fe1579df03be50a27dd075e78cbd772a3081a38bfef416beaaa77');


INSERT INTO module (name)
VALUES
  ('Artificial Intelligence'),
  ('Einführung in die Programmierung mit Python'),
  ('Mathematik: Analysis'),
  ('Einführung in das wissenschaftliche Arbeiten für IT und Technik'),
  ('Projekt: Objektorientierte und funktionale Programmierung mit Python'),
  ('Mathematik: Lineare Algebra'),
  ('Statistik - Wahrscheinlichkeit und deskriptive Statistik'),
  ('Statistik - Induktive Statistik'),
  ('Cloud Computing'),
  ('Statistik - Wahrscheinlichkeit und deskriptive Statistik'),
  ('Maschinelles Lernen - Supervised Learning'),
  ('Maschinelles Lernen - Unsupervised Learning und Feature Engineering'),
  ('Neuronale Netze und Deep Learning'),
  ('Einführung in Computer Vision'),
  ('Projekt: Computer Vision'),
  ('Einführung in das Reinforcement Learning'),
  ('Einführung in Datenschutz und IT-Sicherheit'),
  ('Ethische und rechtliche Aspekte in der KI'),
  ('Einführung in NLP'),
  ('Projekt: NLP'),
  ('Projekt: Edge AI'),
  ('Seminar: Ethische Innovation'),
  ('Model Engineering');

INSERT INTO program (name)
VALUES
  ('Angewandte Künstliche Intelligenz'),
  ('Some other program');


  
INSERT INTO program_module (program_id, module_id, sort)
VALUES
  (1, 1, 0),
  (1, 2, 1),
  (1, 3, 2),
  (1, 4, 3),
  (1, 5, 4),
  (1, 6, 5),
  (1, 7, 6),
  (1, 8, 7),
  (1, 9, 8),
  (1, 10, 9),
  (1, 11, 10),
  (1, 12, 11),
  (1, 13, 12),
  (1, 14, 13),
  (1, 15, 14),
  (1, 16, 15),
  (1, 17, 16),
  (1, 18, 17),
  (1, 19, 18),
  (1, 20, 19),
  (1, 21, 20),
  (1, 22, 21),
  (1, 23, 22),
  (2, 1, 0),
  (2, 2, 1),
  (2, 3, 2),
  (2, 4, 3),
  (2, 5, 4),
  (2, 6, 5),
  (2, 7, 6),
  (2, 8, 7),
  (2, 9, 8),
  (2, 10, 9);

INSERT INTO enrollment (program_id, student_id, semesters, start_date, end_date, target_grade, target_end_date)
VALUES
  (1, 1, 6, '2026-05-01 00:00:00', '2030-04-01 00:00:00', 2.5, '2030-01-01 00:00:00'),
  (2, 1, 3, '2026-05-01 00:00:00', '2030-04-01 00:00:00', NULL, NULL);


INSERT INTO evaluation (module_id, type, max_score, max_attempt)
VALUES
  (1, "exam", 100, 3),
  (2, "exam", 100, 3),
  (3, "exam", 100, 3),
  (4, "exam", 100, 3),
  (5, "exam", 100, 3),
  (6, "exam", 100, 3),
  (7, "exam", 100, 3),
  (8, "exam", 100, 3),
  (9, "exam", 100, 3),
  (10, "exam", 100, 3),
  (11, "exam", 100, 3),
  (12, "exam", 100, 3),
  (13, "exam", 100, 3),
  (14, "exam", 100, 3),
  (15, "exam", 100, 3),
  (16, "exam", 100, 3),
  (17, "exam", 100, 3),
  (18, "exam", 100, 3),
  (19, "exam", 100, 3),
  (20, "exam", 100, 3),
  (21, "exam", 100, 3),
  (22, "exam", 100, 3),
  (23, "exam", 100, 3);

INSERT INTO attempt (enrollment_id, evaluation_id, date_of_attempt, score, grade)
VALUES
  (1, 1, '2026-05-02 00:00:00', 65, 3.7),
  (1, 2, '2026-05-03 00:00:00', 21, 5.0),
  (1, 2, '2026-05-04 00:00:00', 99, 1.0),
  (1, 4, '2026-05-06 00:00:00', 89, 1.0),
  (1, 3, '2026-05-05 00:00:00', 80, 2.7),
  (2, 1, '2026-05-02 00:00:00', 89, 1.7),
  (2, 2, '2026-05-03 00:00:00', 50, 4.0),
  (2, 3, '2026-05-04 00:00:00', 82, 2.0);