DROP TABLE IF EXISTS Employees;
DROP TABLE IF EXISTS Departments;

CREATE TABLE Departments (
  departmentId INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(128) DEFAULT NULL,
  city VARCHAR(64) DEFAULT NULL,
  UNIQUE (name, city)
);

CREATE TABLE Employees (
  employeeId INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  departmentId INT DEFAULT NULL,
  bossId INT DEFAULT NULL,
  firstName VARCHAR(256) NOT NULL,
  lastName VARCHAR(256) NOT NULL,
  salary DOUBLE DEFAULT 2000,
  contractStart DATE DEFAULT NULL,
  contractEnd DATE DEFAULT NULL,
  fee DOUBLE DEFAULT NULL,
  FOREIGN KEY (departmentId) REFERENCES Departments (departmentId) ON DELETE SET NULL,
  FOREIGN KEY (bossId) REFERENCES Employees (employeeId),
  CONSTRAINT validFee CHECK (fee >= 0 and fee <= 1),
  CONSTRAINT validContractDates CHECK (contractStart < contractEnd)
);