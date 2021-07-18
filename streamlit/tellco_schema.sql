

CREATE TABLE IF NOT EXISTS `TweetInformation` 
(
    `Bearer Id` INT NOT NULL AUTO_INCREMENT,
    `DL TP < 50 Kbps (%)` FLOAT DEFAULT NULL,
    `DL TP > 1 Mbps (%)` FLOAT DEFAULT NULL,
     `Avg RTT DL (ms)` FLOAT DEFAULT NULL, 
     `Avg RTT UL (ms)` FLOAT DEFAULT NULL,
     `MSISDN/Number` FLOAT DEFAULT NULL,
     `Nb of sec with Vol UL < 1250B` FLOAT DEFAULT NULL,
     `10 Kbps < UL TP < 50 Kbps (%)` FLOAT DEFAULT NULL,
     `UL TP > 300 Kbps (%)` FLOAT DEFAULT NULL,
     `50 Kbps < UL TP < 300 Kbps (%)` FLOAT DEFAULT NULL,
     `UL TP < 10 Kbps (%)` FLOAT DEFAULT NULL,
     `Nb of sec with Vol DL < 6250B` FLOAT DEFAULT NULL,
     `250 Kbps < DL TP < 1 Mbps (%)` FLOAT DEFAULT NULL,
     `50 Kbps < DL TP < 250 Kbps (%)` FLOAT DEFAULT NULL,
     `IMEI` FLOAT DEFAULT NULL,
     `Dur. (ms)` FLOAT DEFAULT NULL,
     `Last Location Name` VARCHAR(200) NOT NULL,
     `Handset Type` VARCHAR(200) NOT NULL,
     `Handset Manufacturer` VARCHAR(200) NOT NULL,
     `Social Media UL (Bytes)` FLOAT DEFAULT NULL,
     `Google DL (Bytes)` FLOAT DEFAULT NULL,
     `Google UL (Bytes)` FLOAT DEFAULT NULL,
     `Email DL (Bytes)` FLOAT DEFAULT NULL,
     `Email UL (Bytes)` FLOAT DEFAULT NULL,
     `Youtube DL (Bytes)` FLOAT DEFAULT NULL,
     `Youtube UL (Bytes)` FLOAT DEFAULT NULL,
     `Netflix DL (Bytes)` FLOAT DEFAULT NULL,
     `Netflix UL (Bytes)` FLOAT DEFAULT NULL,
     `Gaming DL (Bytes)` FLOAT DEFAULT NULL,
     `Gaming UL (Bytes)` FLOAT DEFAULT NULL,
     `Other DL (Bytes)` FLOAT DEFAULT NULL,
     `Other UL (Bytes)` FLOAT DEFAULT NULL,
     `Total UL (Bytes)` FLOAT DEFAULT NULL,
     `Total DL (Bytes)` FLOAT DEFAULT NULL,
     
    PRIMARY KEY (`Bearer Id`)
)
ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE utf8mb4_unicode_ci;
