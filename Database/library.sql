-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 17, 2022 at 10:15 PM
-- Server version: 10.4.22-MariaDB
-- PHP Version: 8.1.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `library`
--

-- --------------------------------------------------------

--
-- Table structure for table `book`
--

CREATE TABLE `book` (
  `BookNo` int(50) NOT NULL,
  `Title` varchar(150) DEFAULT NULL,
  `SubjectCode` varchar(60) DEFAULT NULL,
  `Author` varchar(40) DEFAULT NULL,
  `Publisher` varchar(50) DEFAULT NULL,
  `Price` double DEFAULT NULL,
  `Location` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `bookchapter`
--

CREATE TABLE `bookchapter` (
  `BookNo` int(50) NOT NULL,
  `ChapterNo` int(40) NOT NULL,
  `Title` varchar(250) DEFAULT NULL,
  `StartingNo` int(50) DEFAULT NULL,
  `EndingNo` int(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `subject`
--

CREATE TABLE `subject` (
  `SubjectCode` varchar(60) NOT NULL,
  `Name` varchar(70) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `subject`
--

INSERT INTO `subject` (`SubjectCode`, `Name`) VALUES
('ARTS', 'ART'),
('ENG', 'ENGLISH'),
('FAN', 'FANTASY'),
('HIS', 'HISTORY'),
('LIFE', 'LIFESTYLE');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `book`
--
ALTER TABLE `book`
  ADD PRIMARY KEY (`BookNo`);

--
-- Indexes for table `bookchapter`
--
ALTER TABLE `bookchapter`
  ADD PRIMARY KEY (`BookNo`,`ChapterNo`);

--
-- Indexes for table `subject`
--
ALTER TABLE `subject`
  ADD PRIMARY KEY (`SubjectCode`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `bookchapter`
--
ALTER TABLE `bookchapter`
  ADD CONSTRAINT `bookchapter_ibfk_1` FOREIGN KEY (`BookNo`) REFERENCES `book` (`BookNo`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
