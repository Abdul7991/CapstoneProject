--
-- Table structure for table `nearest_postcode`
--

DROP TABLE IF EXISTS `nearest_postcode`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `nearest_postcode` (
  `nearest_postcode` varchar(10) CHARACTER SET latin1 NOT NULL,
  `pid` varchar(10) CHARACTER SET latin1 NOT NULL,
  PRIMARY KEY (`nearest_postcode`),
  UNIQUE KEY `idnearest_postcode_UNIQUE` (`nearest_postcode`),
  UNIQUE KEY `pid_UNIQUE` (`pid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
