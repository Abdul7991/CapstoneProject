--
-- Table structure for table `planning_permissions`
--

DROP TABLE IF EXISTS `planning_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `planning_permissions` (
  `planning_permissions` varchar(100) COLLATE utf8_bin NOT NULL,
  `uid` varchar(255) COLLATE utf8_bin DEFAULT NULL,
  `description` varchar(255) COLLATE utf8_bin DEFAULT NULL,
  `app_size` varchar(255) COLLATE utf8_bin DEFAULT NULL,
  `app_state` varchar(255) COLLATE utf8_bin DEFAULT NULL,
  `app_type` varchar(255) COLLATE utf8_bin DEFAULT NULL,
  `pid` varchar(10) COLLATE utf8_bin DEFAULT NULL,
  PRIMARY KEY (`planning_permissions`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
