-- phpMyAdmin SQL Dump
-- version 5.0.3
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 30, 2021 at 12:50 PM
-- Server version: 10.4.14-MariaDB
-- PHP Version: 7.4.11

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `plant_disease_detection`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `PK_ID` int(11) NOT NULL,
  `FULL_NAME` varchar(50) NOT NULL,
  `EMAIL` varchar(50) NOT NULL,
  `USERNAME` varchar(50) NOT NULL,
  `PASSWORD` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`PK_ID`, `FULL_NAME`, `EMAIL`, `USERNAME`, `PASSWORD`) VALUES
(1, 'Admin', 'admin@gmail.com', 'admin', '3qew4w43');

-- --------------------------------------------------------

--
-- Table structure for table `expertadvisor`
--

CREATE TABLE `expertadvisor` (
  `PK_ID` int(11) NOT NULL,
  `FK_ID_ADMIN` int(11) NOT NULL,
  `FULL_NAME` varchar(50) NOT NULL,
  `EMAIL` varchar(50) NOT NULL,
  `USERNAME` varchar(50) NOT NULL,
  `PASSWORD` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `farmer`
--

CREATE TABLE `farmer` (
  `PK_ID` int(11) NOT NULL,
  `FULL_NAME` varchar(50) NOT NULL,
  `EMAIL` varchar(50) NOT NULL,
  `USERNAME` varchar(50) NOT NULL,
  `PASSWORD` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `farmer`
--

INSERT INTO `farmer` (`PK_ID`, `FULL_NAME`, `EMAIL`, `USERNAME`, `PASSWORD`) VALUES
(1, 'danialadli', 'adlidanial1@gmail.com', 'danialadli', '3qew4w43'),
(13, 'Adli Danial', 'adlidanial3@gmail.com', 'adlidanial12', '3qew4w43'),
(14, 'Muhammad Adli Danial', 'adlidanial1999@gmail.com', 'Adlidanial', '3qew4w43');

-- --------------------------------------------------------

--
-- Table structure for table `livechat`
--

CREATE TABLE `livechat` (
  `PK_ID` int(11) NOT NULL,
  `FK_ID_FARMER` int(11) NOT NULL,
  `FK_ID_EXPERT_ADVISOR` int(11) NOT NULL,
  `DESCRIPTION` longtext NOT NULL,
  `DATE_CREATED` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `STATUS` char(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `loghistory`
--

CREATE TABLE `loghistory` (
  `PK_ID` int(11) NOT NULL,
  `FK_ID_FARMER` int(11) NOT NULL,
  `FK_ID_DISEASE` int(11) NOT NULL,
  `URL_IMAGE` longtext NOT NULL,
  `DATE_CREATED` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `plantdisease`
--

CREATE TABLE `plantdisease` (
  `PK_ID` int(11) NOT NULL,
  `PLANT_DISEASE` longtext NOT NULL,
  `SYMPTOM_DISEASE` longtext NOT NULL,
  `PREVENT_DISEASE` longtext NOT NULL,
  `DATE_CREATED` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admin`
--
ALTER TABLE `admin`
  ADD PRIMARY KEY (`PK_ID`);

--
-- Indexes for table `expertadvisor`
--
ALTER TABLE `expertadvisor`
  ADD PRIMARY KEY (`PK_ID`),
  ADD KEY `FK_ID_ADMIN` (`FK_ID_ADMIN`);

--
-- Indexes for table `farmer`
--
ALTER TABLE `farmer`
  ADD PRIMARY KEY (`PK_ID`);

--
-- Indexes for table `livechat`
--
ALTER TABLE `livechat`
  ADD PRIMARY KEY (`PK_ID`),
  ADD KEY `FK_ID_FARMER_CHAT` (`FK_ID_FARMER`),
  ADD KEY `FK_ID_EXPERT_ADVISOR_CHAT` (`FK_ID_EXPERT_ADVISOR`);

--
-- Indexes for table `loghistory`
--
ALTER TABLE `loghistory`
  ADD PRIMARY KEY (`PK_ID`),
  ADD KEY `FK_ID_FARMER` (`FK_ID_FARMER`),
  ADD KEY `FK_ID_DISEASE` (`FK_ID_DISEASE`);

--
-- Indexes for table `plantdisease`
--
ALTER TABLE `plantdisease`
  ADD PRIMARY KEY (`PK_ID`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `admin`
--
ALTER TABLE `admin`
  MODIFY `PK_ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `expertadvisor`
--
ALTER TABLE `expertadvisor`
  MODIFY `PK_ID` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `farmer`
--
ALTER TABLE `farmer`
  MODIFY `PK_ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- AUTO_INCREMENT for table `livechat`
--
ALTER TABLE `livechat`
  MODIFY `PK_ID` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `loghistory`
--
ALTER TABLE `loghistory`
  MODIFY `PK_ID` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `plantdisease`
--
ALTER TABLE `plantdisease`
  MODIFY `PK_ID` int(11) NOT NULL AUTO_INCREMENT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
