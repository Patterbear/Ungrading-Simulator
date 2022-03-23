#This code is using MySQL, and cannot be used for SQLlite3. Replicate this database into SQLlite3 to use it.
CREATE TABLE Characters(
id INT NOT NULL,
name VARCHAR(30) NOT NULL,
gender VARCHAR(30) NOT NULL,
photolink VARCHAR(200),
daynumber INT NOT NULL,
skilllevel INT NOT NULL,
experiencepoints INT NOT NULL,
intelligence FLOAT NOT NULL,
awareness INT NOT NULL,
PRIMARY KEY (id));

CREATE TABLE Topic(
id INT NOT NULL,
name VARCHAR(30) NOT NULL,
PRIMARY KEY(id));

CREATE TABLE Feedback(
id INT NOT NULL,
message VARCHAR(200) NOT NULL,
PRIMARY KEY(id));

CREATE TABLE Activity(
id INT NOT NULL,
name VARCHAR(30) NOT NULL,
type CHAR(30) NOT NULL,
characterid INT NOT NULL,
completed BOOLEAN NOT NULL,
grade FLOAT,
feedbackid INT,
topiccode INT NOT NULL,
FOREIGN KEY (characterid) REFERENCES Characters(id),
FOREIGN KEY (feedbackid) REFERENCES Feedback(id),
FOREIGN KEY (topiccode) REFERENCES Topic(id),
PRIMARY KEY (id));