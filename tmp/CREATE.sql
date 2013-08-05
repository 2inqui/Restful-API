CREATE DATABASE messages;

USE  messages;

CREATE TABLE `User` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `date_created` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `date_modified` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `name` text NOT NULL,
  `email` text NOT NULL,
  `phone` text NOT NULL,
  `thumbnail_url` text,
  `reg_id` text,
  PRIMARY KEY (`id`)
);