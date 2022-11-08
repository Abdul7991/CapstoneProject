--
-- Table structure for table `postcode`
--

DROP TABLE IF EXISTS `postcode`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `postcode` (
  `postcode` varchar(10) COLLATE utf8_bin NOT NULL,
  `constituency` varchar(100) COLLATE utf8_bin NOT NULL,
  `longitude` double DEFAULT NULL,
  `latitude` double DEFAULT NULL,
  PRIMARY KEY (`postcode`),
  UNIQUE KEY `postcode_UNIQUE` (`postcode`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
