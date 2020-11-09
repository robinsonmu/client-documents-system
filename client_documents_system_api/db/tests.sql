# User-Employee
INSERT INTO user (email, hashed_password, is_active, is_employee)
	VALUES ("robinsonmu@unisabana.edu.co", "$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQoeG6Lruj3vjPGga31lW", 1, 1 );

# User-Client

INSERT INTO user (email, hashed_password, is_active, is_employee)
	VALUES ("juanpereira305@gmail.com", "$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQoeG6Lruj3vjPGga31lW", 1, 0 );

INSERT INTO client (address, occupation, user_id)
	VALUES ("Zipa", "Ingeniero informatico", 2);