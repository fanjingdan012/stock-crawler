
drop database if exists stock;

create database stock;

use stock;

grant select, insert, update, delete on stock.* to 'www-data'@'localhost' identified by 'www-data';
CREATE TABLE `stock` (
	`id` INT(11) NOT NULL AUTO_INCREMENT,
	`compname` VARCHAR(255) NULL DEFAULT NULL,
	`engname` VARCHAR(255) NULL DEFAULT NULL,
	`comptype1` VARCHAR(255) NULL DEFAULT NULL,
	`comptype2` VARCHAR(255) NULL DEFAULT NULL,
	`founddate` VARCHAR(255) NULL DEFAULT NULL,
	`orgtype` VARCHAR(255) NULL DEFAULT NULL,
	`regcapital` DECIMAL(10,0) NULL DEFAULT NULL,
	`authcapsk` DECIMAL(10,0) NULL DEFAULT NULL,
	`chairman` VARCHAR(255) NULL DEFAULT NULL,
	`manager` VARCHAR(255) NULL DEFAULT NULL,
	`legrep` VARCHAR(255) NULL DEFAULT NULL,
	`bsecretary` VARCHAR(255) NULL DEFAULT NULL,
	`bsecretarytel` VARCHAR(255) NULL DEFAULT NULL,
	`bsecretaryfax` VARCHAR(255) NULL DEFAULT NULL,
	`seaffrepr` VARCHAR(255) NULL DEFAULT NULL,
	`seagttel` VARCHAR(255) NULL DEFAULT NULL,
	`seagtfax` VARCHAR(255) NULL DEFAULT NULL,
	`seagtemail` VARCHAR(255) NULL DEFAULT NULL,
	`authreprsbd` VARCHAR(255) NULL DEFAULT NULL,
	`leconstant` VARCHAR(255) NULL DEFAULT NULL,
	`accfirm` VARCHAR(255) NULL DEFAULT NULL,
	`regaddr` VARCHAR(255) NULL DEFAULT NULL,
	`officeaddr` VARCHAR(255) NULL DEFAULT NULL,
	`officezipcode` VARCHAR(255) NULL DEFAULT NULL,
	`comptel` VARCHAR(255) NULL DEFAULT NULL,
	`compfax` VARCHAR(255) NULL DEFAULT NULL,
	`compemail` VARCHAR(255) NULL DEFAULT NULL,
	`compurl` VARCHAR(255) NULL DEFAULT NULL,
	`servicetel` VARCHAR(255) NULL DEFAULT NULL,
	`servicefax` VARCHAR(255) NULL DEFAULT NULL,
	`compintro` TEXT NULL,
	`bizscope` TEXT NULL,
	`majorbiz` VARCHAR(255) NULL DEFAULT NULL,
	`bizscale` VARCHAR(255) NULL DEFAULT NULL,
	`compcode` VARCHAR(255) NULL DEFAULT NULL,
	`compsname` VARCHAR(255) NULL DEFAULT NULL,
	`region` VARCHAR(255) NULL DEFAULT NULL,
	`regptcode` VARCHAR(255) NULL DEFAULT NULL,
	`listdate` DATETIME NULL DEFAULT NULL,
	`issprice` DECIMAL(10,0) NULL DEFAULT NULL,
	`onlactissqty` BIGINT(20) NULL DEFAULT NULL,
	`actissqty` BIGINT(20) NULL DEFAULT NULL,
	`industryid` INT(11) NULL DEFAULT NULL,
	PRIMARY KEY (`id`)
)
COLLATE='utf8_general_ci'
ENGINE=InnoDB;

create table users (
    `id` varchar(50) not null,
    `email` varchar(50) not null,
    `passwd` varchar(50) not null,
    `admin` bool not null,
    `name` varchar(50) not null,
    `image` varchar(500) not null,
    `created_at` real not null,
    unique key `idx_email` (`email`),
    key `idx_created_at` (`created_at`),
    primary key (`id`)
) engine=innodb default charset=utf8;

create table blogs (
    `id` varchar(50) not null,
    `user_id` varchar(50) not null,
    `user_name` varchar(50) not null,
    `user_image` varchar(500) not null,
    `name` varchar(50) not null,
    `summary` varchar(200) not null,
    `content` mediumtext not null,
    `created_at` real not null,
    key `idx_created_at` (`created_at`),
    primary key (`id`)
) engine=innodb default charset=utf8;

create table comments (
    `id` varchar(50) not null,
    `blog_id` varchar(50) not null,
    `user_id` varchar(50) not null,
    `user_name` varchar(50) not null,
    `user_image` varchar(500) not null,
    `content` mediumtext not null,
    `created_at` real not null,
    key `idx_created_at` (`created_at`),
    primary key (`id`)
) engine=innodb default charset=utf8;