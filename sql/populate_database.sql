INSERT INTO Departments (departmentId, name, city)
    VALUES
	(1, 'Arte', 'Cádiz'),
	(2, 'Historia', NULL),
	(3, 'Informática', 'Sevilla');

INSERT INTO Employees (employeeId, departmentId, bossId, firstName, lastName, salary, contractStart, contractEnd, fee)
    VALUES
	(1, 1, NULL, 'Pedro', 'Periáñez', 2300, '2017-09-15', NULL, 0.2),
	(2, 1, 1, 'José', 'Jiménez', 2500, '2018-08-15', NULL, 0.5),
	(3, 2, 2, 'Lola', 'Lacalle', 2300, '2018-08-15', NULL, 0.3),
	(4, 1, 2, 'Luis', 'Linares', 1300, '2018-08-15', '2018-11-15', 0),
	(5, 1, 3, 'Ana', 'Álvarez', 1300, '2018-08-15', '2018-11-15', 0);