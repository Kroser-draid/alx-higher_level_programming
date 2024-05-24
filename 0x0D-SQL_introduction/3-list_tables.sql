-- script that shows all tables in the database
-- show all tables command
SELECT table_name 
FROM information_schema.tables 
WHERE table_schema = DATABASE();
