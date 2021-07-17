

CREATE TABLE IF NOT EXISTS `TweetInformation` 
(
    `id` INT NOT NULL AUTO_INCREMENT,
    `created_at` TEXT NOT NULL,
    `source` VARCHAR(200) NOT NULL,
    `original_text` TEXT DEFAULT NULL,
    `polarity` FLOAT DEFAULT NULL,
    `subjectivity` FLOAT DEFAULT NULL,
    `lang` TEXT DEFAULT NULL,
    `favorite_count` INT DEFAULT NULL,
    `original_author` TEXT DEFAULT NULL,
    `followers_count` INT DEFAULT NULL,
    `friends_count` INT DEFAULT NULL,
    `possibly_sensitive` TEXT DEFAULT NULL,
    `hashtags` TEXT DEFAULT NULL,
    `user_mentions` TEXT DEFAULT NULL,
    `place` TEXT DEFAULT NULL,
    `clean_text` TEXT DEFAULT NULL,
    PRIMARY KEY (`id`)
)
ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE utf8mb4_unicode_ci;
