# SQL

|---------|---------|
| Url | Descripción |
| [sqlbolt](https://sqlbolt.com/) | Curso SQL gratuito |
| [khanacademy](https://www.khanacademy.org/computer-programming/new/sql) | Trabajar con SQL online |

## Introducción SQL

Sentencias SQL comunmente usadas:

```
/* Crear una tabla en SQL */
CREATE TABLE Vehicles (
    Id INTEGER PRIMARY KEY,
    MakeModel TEXT,
    Wheels INTEGER,
    Doors INTEGER,
    Type text
);

/* Insertar un dato en una tabla */
INSERT INTO Vehicles (Id, MakeModel, Wheels, Doors, Type) VALUES 
(1, 'BMW', 4, 4, 'Hashback');

/* Consultar toda la información (columnas) de una tabla */
SELECT * FROM Vehicles;

/* Consultar las columnas especificas de la tabla */
SELECT Id, MakeModel, Type FROM Vehicles;

/* Consultar usando una condición */
SELECT * FROM Vehicles WHERE Id <= 5;
```

## Trabajando con consultas

Consultas:

```
CREATE TABLE Buildings (
    Building_name TEXT PRIMARY KEY,
    Capacity INTEGER
);

CREATE TABLE Employees (
    Role TEXT,
    Name TEXT,
    Building TEXT FOREIGN KEY Buildings,
    Years_employed INTEGER
);

SELECT * FROM movies INNER JOIN Boxoffice ON Id = Movie_id;

SELECT * FROM movies INNER JOIN Boxoffice ON Id = Movie_id WHERE International_sales > Domestic_sales;

SELECT * FROM movies INNER JOIN Boxoffice ON Id = Movie_id ORDER BY Rating DESC;


SELECT DISTINCT Buildings.Building_name FROM Employees LEFT JOIN Buildings ON Employees.Building = Buildings.Building_name;

SELECT Buildings.Building_name, Buildings.Capacity FROM Buildings;

SELECT DISTINCT Employees.Role, Buildings.Building_name FROM Buildings LEFT JOIN Employees ON Employees.Building = Buildings.Building_name;
```

## Modelo

Un Modelo es una estructura de datos ordenada compuesta por columnas y filas.

## Entidad

Un objeto que puede existir en la vida real o ficticio tiene caracteristicas de dicha entidad.