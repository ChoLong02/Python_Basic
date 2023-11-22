# 다음 영화 리뷰 Table
CREATE TABLE `tbl_review` (
	`no` INT(10) NOT NULL AUTO_INCREMENT,
	`title` VARCHAR(100) NOT NULL,
	`review` VARCHAR(100),
	`score` INT(10) NOT NULL DEFAULT '0',
	`writer` VARCHAR(50) NULL,
	`reg_date` VARCHAR(50) NOT NULL,
	PRIMARY KEY (`no`) USING BTREE
)
COMMENT='다음 영화 리뷰'
AUTO_INCREMENT=1
;