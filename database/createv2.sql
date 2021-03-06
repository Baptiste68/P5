

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';


SET UNIQUE_CHECKS = 0;
DROP SCHEMA IF EXISTS `foodexo` ;
SET UNIQUE_CHECKS = 1;


CREATE SCHEMA IF NOT EXISTS `foodexo` DEFAULT CHARACTER SET utf8 ;
USE `foodexo` ;


DROP TABLE IF EXISTS `foodexo`.`Food` ;

CREATE TABLE IF NOT EXISTS `foodexo`.`Food` (
  `id_food` SMALLINT NOT NULL AUTO_INCREMENT,
  `name_food` TEXT NOT NULL,
  `quantity_food` TEXT NULL,
  `dangers_food` TEXT NULL,
  `store_food` TEXT NULL,
  `nutri_score_food` CHAR(1) NOT NULL,
  `link_food` TEXT NULL,
  PRIMARY KEY (`id_food`))
ENGINE = InnoDB;


DROP TABLE IF EXISTS `foodexo`.`Categories` ;

CREATE TABLE IF NOT EXISTS `foodexo`.`Categories` (
  `id_categories` SMALLINT NOT NULL AUTO_INCREMENT,
  `name_categories` VARCHAR(45) NULL,
  PRIMARY KEY (`id_categories`))
ENGINE = InnoDB;


DROP TABLE IF EXISTS `foodexo`.`foodcate` ;

CREATE TABLE IF NOT EXISTS `foodexo`.`foodcate` (
  `Food_id_food` SMALLINT NOT NULL,
  `Categories_id_categories` SMALLINT NOT NULL,
  PRIMARY KEY (`Food_id_food`, `Categories_id_categories`),
  INDEX `fk_foodcate_Categories_idx` (`Categories_id_categories` ASC) VISIBLE,
  INDEX `fk_foodcate_Food_idx` (`Food_id_food` ASC) VISIBLE,
  CONSTRAINT `fk_foodcate_Food`
    FOREIGN KEY (`Food_id_food`)
    REFERENCES `foodexo`.`Food` (`id_food`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_foodcate_Categories`
    FOREIGN KEY (`Categories_id_categories`)
    REFERENCES `foodexo`.`Categories` (`id_categories`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


DROP TABLE IF EXISTS `foodexo`.`saved` ;

CREATE TABLE IF NOT EXISTS `foodexo`.`saved` (
  `Food_id_foodsub` SMALLINT NOT NULL,
  `Food_id_foodissub` SMALLINT NOT NULL,
  PRIMARY KEY (`Food_id_foodsub`, `Food_id_foodissub`),
  CONSTRAINT `fk_saved_Foodsub_idx`
    FOREIGN KEY (`Food_id_foodsub`)
    REFERENCES `foodexo`.`Food` (`id_food`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_saved_Foodissub`
    FOREIGN KEY (`Food_id_foodissub`)
    REFERENCES `foodexo`.`Food` (`id_food`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
