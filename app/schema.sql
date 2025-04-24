DROP TABLE IF EXISTS calculations;

CREATE TABLE calculations (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  num1 INTEGER NOT NULL,
  num2 INTEGER NOT NULL,
  operand TEXT NOT NULL,
  solution INTEGER NOT NULL,
  UNIQUE (num1, num2, operand, solution)
);