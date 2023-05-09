-- INSERTS:
-- INSERT INTO table_name (column_name1, column_name2) 
-- VALUES('column1_value', 'column2_value');

INSERT INTO users (name, age, email)
VALUES ('ASpencer', 35, 'srauch@codingdojo.com');
-- ('Kaija', 25, 'kaija@dojo.com');

INSERT INTO infractions (rule, base_fine)
VALUES ('no seatbelt', 75), ('unsafe driving',80),('loose baby',200);

-- one to many insert
INSERT INTO pets (name, species, user_id)
VALUES ('Wiley', 'ChiPom', 1);

-- one to one YYYY-MM-DD
INSERT INTO licenses (state, expiration_date, user_id)
VALUES ('OR', '2023-07-04', 1);

-- many to many
INSERT INTO users_have_infractions (infraction_id, user_id, court_date)
VALUE (1, 1, '2023-07-04');

-- SELECT QUERIES

-- SELECT columns FROM table WHERE condition;

SELECT * FROM users;

SELECT name, age FROM users;

SELECT * FROM users
WHERE name like '%r';

SELECT * FROM users
ORDER BY name ASC;

-- UPDATE
-- UPDATE table_name
-- SET column1 = value1, column2 = value2, ...
-- WHERE condition; <--- the where condition is very important for an update!

UPDATE users SET age = 99, email = 'dont store my email' WHERE id > 0;
SET SQL_SAFE_UPDATES = 0;
UPDATE users SET age = 34 WHERE name = 'Spencer';


-- DELETE FROM table_name WHERE condition

DELETE FROM users WHERE id = 4;

-- SELECT FUNCTION(column) FROM table_name
SELECT *, MONTH(created_at) AS month_no FROM users;