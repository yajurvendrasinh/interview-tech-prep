-- ---
-- Globals
-- ---

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";
SET FOREIGN_KEY_CHECKS=0;

-- ---
-- Table 'Message'
-- 
-- ---

DROP TABLE IF EXISTS message;
    
CREATE TABLE message (
  id INTEGER,
  user_id INTEGER,
  text VARCHAR(255),
  created_at TIMESTAMP,
  updated_at TIMESTAMP,
  PRIMARY KEY (`id`)
);

-- ---
-- Table 'User'
-- 
-- ---

DROP TABLE IF EXISTS user;
    
CREATE TABLE user (
  id INTEGER,
  room_id INTEGER,
  username VARCHAR(255),
  created_at TIMESTAMP,
  updated_at TIMESTAMP,
  PRIMARY KEY (`id`)
);

-- -- ---
-- -- Table 'Room'
-- -- 
-- -- ---

DROP TABLE IF EXISTS room;
    
CREATE TABLE room (
  id INTEGER,
  name VARCHAR(255),
  created_at TIMESTAMP,
  updated_at TIMESTAMP,
  PRIMARY KEY (`id`)
);

-- -- ---
-- -- Foreign Keys 
-- -- ---

ALTER TABLE `message` ADD FOREIGN KEY (user_id) REFERENCES `user` (`id`);
ALTER TABLE `user` ADD FOREIGN KEY (room_id) REFERENCES `room` (`id`);

-- ---
-- Table Properties
-- ---

ALTER TABLE `message` ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
ALTER TABLE `user` ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
ALTER TABLE `room` ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- ---
-- Seed data
-- ---

INSERT INTO message (`id`,`user_id`,`text`,`created_at`,`updated_at`) VALUES
('1','1','hello world','','');

INSERT INTO user (`id`,`room_id`,`username`,`created_at`,`updated_at`) VALUES
('1','1','polina','','');

INSERT INTO room (`id`,`name`,`created_at`,`updated_at`) VALUES
('1','lobby','','');

