--
-- Table structure for table `crime_data`
--

DROP TABLE IF EXISTS `crime_data`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `crime_data` (
  `crime_data` varchar(255) COLLATE utf8_bin NOT NULL,
  `category` varchar(45) COLLATE utf8_bin DEFAULT NULL,
  `area` varchar(45) COLLATE utf8_bin DEFAULT NULL,
  `outcome_status` varchar(45) COLLATE utf8_bin DEFAULT NULL,
  `pid` varchar(10) COLLATE utf8_bin DEFAULT NULL,
  `date_time` int(11) DEFAULT NULL,
  PRIMARY KEY (`crime_data`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
