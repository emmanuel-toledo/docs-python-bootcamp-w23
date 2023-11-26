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

## Modelo

Un Modelo es una estructura de datos ordenada compuesta por columnas y filas.

## Entidad

Un objeto que puede existir en la vida real o ficticio tiene caracteristicas de dicha entidad.

## Trabajando con SQLBolt básico

### Lesson 1

```
SELECT Title FROM movies;
SELECT Director FROM movies;
SELECT Title, Director FROM movies;
SELECT Title, Year FROM movies;
SELECT * FROM movies;
```

### Lesson 2

```
SELECT * FROM movies WHERE Id = 6;
SELECT * FROM movies WHERE Year BETWEEN 2000 AND 2010;
SELECT * FROM movies WHERE Year NOT BETWEEN 2000 AND 2010;
SELECT * FROM movies WHERE Id <= 5;
```

### Lesson 3

```
SELECT * FROM movies WHERE Title LIKE '%Toy Story%';
SELECT * FROM movies WHERE Director = 'John Lasseter';
SELECT * FROM movies WHERE Director != 'John Lasseter';
SELECT * FROM movies WHERE Title LIKE 'WALL-%';
```

### Lesson 4

```
SELECT DISTINCT Director FROM Movies ORDER BY Director ASC;
SELECT * FROM movies ORDER BY Year DESC LIMIT 4 OFFSET 0;
SELECT * FROM Movies ORDER BY Title ASC LIMIT 5 OFFSET 0;
SELECT * FROM Movies ORDER BY Title ASC LIMIT 5 OFFSET 5;
```

### Lesson 5

```
SELECT * FROM north_american_cities WHERE Country = 'Canada';
SELECT * FROM north_american_cities WHERE Country = 'United States' ORDER BY Latitude DESC;
SELECT * FROM north_american_cities WHERE Longitude < -87.629798 ORDER BY Longitude ASC;
SELECT * FROM north_american_cities WHERE Country = 'Mexico' ORDER BY Population DESC LIMIT 2 OFFSET 0;
SELECT * FROM north_american_cities WHERE Country = 'United States' ORDER BY Population DESC LIMIT 2 OFFSET 2;
```

### Lesson 6

```
SELECT * FROM movies INNER JOIN Boxoffice ON Id = Movie_id;
SELECT * FROM movies INNER JOIN Boxoffice ON Id = Movie_id WHERE International_sales > Domestic_sales;
SELECT * FROM movies INNER JOIN Boxoffice ON Id = Movie_id ORDER BY Rating DESC;
```

### Lesson 7

```
SELECT DISTINCT Buildings.Building_name FROM Employees LEFT JOIN Buildings ON Employees.Building = Buildings.Building_name;
SELECT Buildings.Building_name, Buildings.Capacity FROM Buildings;
SELECT DISTINCT Employees.Role, Buildings.Building_name FROM Buildings LEFT JOIN Employees ON Employees.Building = Buildings.Building_name;
```

### Lesson 8

```
SELECT * FROM employees WHERE Building IS NULL
SELECT DISTINCT Buildings.Building_name FROM Buildings LEFT JOIN Employees ON Employees.Building = Buildings.Building_name WHERE Employees.Building IS NULL;
```

### Lesson 9

```
SELECT M.Title, (B.Domestic_sales + B.International_sales) / 100000 as sales FROM Movies AS M INNER JOIN Boxoffice AS B ON M.Id = B.Movie_id;
SELECT M.Title, (B.Rating * 10) as percent FROM Movies AS M INNER JOIN Boxoffice AS B ON M.Id = B.Movie_id;
SELECT M.Title FROM Movies AS M WHERE M.Year % 2 = 0;
```

### Lesson 10

```
SELECT Name, MAX(Years_employed) FROM Employees;
SELECT DISTINCT Role, AVG(Years_employed) FROM Employees GROUP BY Role;
SELECT DISTINCT Building, SUM(Years_employed) FROM Employees GROUP BY Building;
```

### Lesson 11

```
SELECT COUNT(*) FROM employees WHERE Role = 'Artist';
SELECT Role, COUNT(*) as total FROM Employees GROUP BY Role HAVING Role = Role;
SELECT SUM(Years_employed) sum_years FROM Employees GROUP BY Role HAVING Role = 'Engineer';
```

### Lesson 12

```
SELECT DISTINCT M.Director, COUNT(M.Id) FROM Movies AS M GROUP BY M.Director;
SELECT DISTINCT M.Director, (SUM(B.Domestic_sales) + SUM(B.International_sales)) AS Total_sales FROM Movies AS M INNER JOIN Boxoffice AS B ON M.Id = B.Movie_id GROUP BY M.Director;
```

### Lesson 13

Insertando registros a una tabla.

```
INSERT INTO Movies (Id, Title, Director, Year, Length_minutes) VALUES (15, 'Toy Story 4', 'John Lasseter', '2022', '90');
INSERT INTO Boxoffice (Movie_Id, Rating, Domestic_sales, International_sales) VALUES (15, 8.7, 340000000, 270000000);
```

### Lesson 14

Actualizando datos de un registro de una tabla.

```
UPDATE Movies 
SET Director = 'John Lasseter'
WHERE Title = "A Bug's Life";

UPDATE Movies 
SET Year = 1999
WHERE Title = "Toy Story 2";

UPDATE Movies 
SET Title = "Toy Story 3", 
Director = 'Lee Unkrich'
WHERE Id = 11;
```

### Lesson 15

Eliminando registros de una tabla con base a una condicionante.

```
DELETE FROM Movies WHERE Year < 2005;

DELETE FROM Movies WHERE Director = 'Andrew Stanton';
```

### Lesson 16

Crear una tabla.

```
CREATE TABLE Database
( 
    Name TEXT,
    Version INTEGER,
    Download_count INTEGER
);
```

### Lesson 17

Modificar el esquema de una tabla agregando nuevas columnas.

```
ALTER TABLE Movies ADD COLUMN Aspect_ratio FLOAT;
ALTER TABLE Movies ADD COLUMN Language TEXT DEFAULT 'English';
```

### Lesson 18

Eliminar una tabla si es que existe.

```
DROP TABLE IF EXISTS Movies;
DROP TABLE IF EXISTS BoxOffice;
```

### Lesson X

```
```