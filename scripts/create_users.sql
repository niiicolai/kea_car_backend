-- Drop the user if it exists
DROP USER IF EXISTS 'application_user'@'%';

-- Create the user
CREATE USER 'application_user'@'%' IDENTIFIED BY 'password';

-- Drop the user if it exists
DROP USER IF EXISTS 'readonly_user'@'%';

-- Create the user
CREATE USER 'readonly_user'@'%' IDENTIFIED BY 'password';

-- Drop the user if it exists
DROP USER IF EXISTS 'limited_reader'@'%';

-- Create the user
CREATE USER 'limited_reader'@'%' IDENTIFIED BY 'password';