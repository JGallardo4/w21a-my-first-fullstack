CREATE TABLE `Posts` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `User_Id` int(11) NOT NULL,
  `Content` varchar(800) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `Created_At` datetime DEFAULT NULL,
  PRIMARY KEY (`Id`),
  KEY `FK_Users__Posts` (`User_Id`),
  CONSTRAINT `FK_Users__Posts` FOREIGN KEY (`User_Id`) REFERENCES `Users` (`Id`) ON DELETE CASCADE
);

CREATE TABLE `User_Sessions` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `User_Id` int(11) NOT NULL,
  `Login_Token` varchar(110) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`Id`),
  UNIQUE KEY `User_Id` (`User_Id`),
  KEY `FK_Users__User_Sessions` (`User_Id`),
  CONSTRAINT `FK_Users__User_Sessions` FOREIGN KEY (`User_Id`) REFERENCES `Users` (`Id`) ON DELETE CASCADE
);

CREATE TABLE `Users` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `Username` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL,
  `Password` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`Id`),
  UNIQUE KEY `Username` (`Username`)
);