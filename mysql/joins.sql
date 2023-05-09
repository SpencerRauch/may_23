-- JOINS
-- SELECT * FROM table JOIN table_we_are_joining ON fk = pk;

-- one to one join
SELECT * FROM users JOIN licenses ON users.id = licenses.user_id;

-- one to many join
SELECT * FROM users JOIN pets ON users.id = pets.user_id;
SELECT * FROM pets JOIN users ON pets.user_id = users.id;

-- many to many join
SELECT * FROM users JOIN users_have_infractions 
ON users.id = users_have_infractions.user_id
JOIN infractions ON users_have_infractions.infraction_id = infractions.id; 


SELECT * FROM users;

-- left join
SELECT * FROM users LEFT JOIN pets ON users.id = user_id;

-- SELECT * FROM pets RIGHT JOIN users ON pets.user_id = users.id;

-- group by
SELECT *, COUNT(pets.id) AS pets_owned FROM users JOIN pets ON users.id = user_id GROUP BY users.id;