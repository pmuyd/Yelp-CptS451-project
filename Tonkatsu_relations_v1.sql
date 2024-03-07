create table Business (
	business_id char(25) primary key,
	name varchar(255),
	city varchar(20),
	state varchar(50),
	address varchar(255),
	zipCode varchar(10),
	totalCheckins int,
	reviewCount int,
	rating float,
	stars float
);

CREATE TABLE Review (
    reviewID char(25) PRIMARY KEY,
    business_id char(25) NOT NULL,
    date varchar(25),
    text varchar(500),
    reviewStars INT,
    coolVote INT,
    funnyVote INT,
    usefulVote INT,
    FOREIGN KEY (business_id) REFERENCES Business(business_id)
);

create table user(
	userID char(25) primary key,
	name varchar(255)
);

create table friend(
	user_id_list varchar(25) primary key
);

create table Attributes(
	names varchar(255) primary key,
	value int -- ?? unsure because of true/false & numbers for this value
);

create table Categories(
	names varchar(255) primary key
);

CREATE TABLE Checkin (
    checkinID int PRIMARY KEY,
    business_id char(25) NOT NULL,
    time timestamp,
    day varchar(10),
    count int,
    FOREIGN KEY (business_id) REFERENCES Business(business_id)
);