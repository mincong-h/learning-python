--
-- Script for database creation for Clement GAUTIER
--
-- Author: mincong-h
-- Date: 2015.11.27
--
CREATE DATABASE IF NOT EXISTS `infostats`;

CREATE TABLE IF NOT EXISTS `infostats`.`trace` (
	`id` INT unsigned NOT NULL AUTO_INCREMENT COMMENT 'unique ID for each entry',
	`timestamp` INT(11) NOT NULL COMMENT 'unix timestamp in second',
	`total_distance` FLOAT NOT NULL COMMENT 'total distance of vehical (KM)',
    `volume` FLOAT NOT NULL COMMENT 'remaining volume in (L)',
	PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

INSERT INTO `infostats`.`trace` (`timestamp`, `total_distance`, `volume`) VALUES
(UNIX_TIMESTAMP(NOW()) - 1, 0.1, 50.0),
(UNIX_TIMESTAMP(NOW()), 0.2, 49.9)