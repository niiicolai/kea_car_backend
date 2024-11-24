USE kea_cars_dev;

-- Drop the application user if the user exists
DROP USER IF EXISTS 'application_user'@'%';

-- Create the application user
CREATE USER 'application_user'@'%' IDENTIFIED BY 'password';

-- Grant the required privileges for the application user


GRANT SELECT, INSERT, UPDATE, DELETE, EXECUTE ON * TO 'application_user'@'%';
-- Apply the changes
FLUSH PRIVILEGES;


-- Drop the readonly user if the user exists
DROP USER IF EXISTS 'readonly_user'@'%';

-- Create the readonly user
CREATE USER 'readonly_user'@'%' IDENTIFIED BY 'password';

-- Grant SELECT privileges on all tables in all databases to the readonly user
GRANT SELECT ON * TO 'readonly_user'@'%';

-- Grant EXECUTE privilege specifically for the "get_all_cars" stored procedure to the readonly user
GRANT EXECUTE ON PROCEDURE get_all_cars TO 'readonly_user'@'%';

-- Apply the changes
FLUSH PRIVILEGES;



-- Drop the user if it exists
DROP USER IF EXISTS 'limited_reader'@'%';

-- Create the user
CREATE USER 'limited_reader'@'%' IDENTIFIED BY 'password';

-- Grant SELECT privileges on specific tables to the limited_reader user
GRANT SELECT ON accessories TO 'limited_reader'@'%';
GRANT SELECT ON insurances TO 'limited_reader'@'%';
GRANT SELECT ON brands TO 'limited_reader'@'%';
GRANT SELECT ON colors TO 'limited_reader'@'%';
GRANT SELECT ON models TO 'limited_reader'@'%';

-- Apply the changes
FLUSH PRIVILEGES;
