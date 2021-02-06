-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema play_my_beat
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema play_my_beat
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `play_my_beat` DEFAULT CHARACTER SET utf8 ;
USE `play_my_beat` ;

-- -----------------------------------------------------
-- Table `play_my_beat`.`runs`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `play_my_beat`.`runs` (
  `run_id` INT NOT NULL AUTO_INCREMENT,
  `start_date` DATETIME NOT NULL,
  `start_date_nano` BIGINT NOT NULL,
  `end_date` DATETIME NOT NULL,
  `end_date_nano` BIGINT NOT NULL,
  PRIMARY KEY (`run_id`),
  UNIQUE INDEX `run_id_UNIQUE` (`run_id` ASC) VISIBLE,
  UNIQUE INDEX `start_date_UNIQUE` (`start_date` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `play_my_beat`.`heart_rate`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `play_my_beat`.`heart_rate` (
  `run_id` INT NOT NULL,
  `reg_id` INT NOT NULL AUTO_INCREMENT,
  `run_min` TIME NOT NULL,
  `bpm` INT NOT NULL,
  INDEX `fk_heart_rate_runs_idx` (`run_id` ASC) VISIBLE,
  PRIMARY KEY (`reg_id`),
  CONSTRAINT `fk_heart_rate_runs`
    FOREIGN KEY (`run_id`)
    REFERENCES `play_my_beat`.`runs` (`run_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `play_my_beat`.`other_data`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `play_my_beat`.`other_data` (
  `run_id` INT NOT NULL,
  `reg_id` INT NOT NULL AUTO_INCREMENT,
  `distance` VARCHAR(45) NOT NULL,
  `steps` VARCHAR(45) NOT NULL,
  `calories` VARCHAR(45) NOT NULL,
  INDEX `fk_other_data_runs1_idx` (`run_id` ASC) VISIBLE,
  PRIMARY KEY (`reg_id`),
  CONSTRAINT `fk_other_data_runs1`
    FOREIGN KEY (`run_id`)
    REFERENCES `play_my_beat`.`runs` (`run_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `play_my_beat`.`last_prediction`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `play_my_beat`.`last_prediction` (
	pred_date DATETIME NOT NULL, 
  pred_min INT NOT NULL,
  pred_bpm INT NOT NULL);
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `play_my_beat`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `play_my_beat`.`users` (
  user_id INT NOT NULL AUTO_INCREMENT,
  user_name VARCHAR NOT NULL,
  user_pass VARCHAR NOT NULL,
  PRIMARY KEY (user_id));
ENGINE = InnoDB;

SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
