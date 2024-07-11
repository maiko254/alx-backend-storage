-- Script creating a stored procedured that calculates and stores the average score for a student

DELIMITER //

CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN
	DECLARE total_score INT;
	DECLARE total_projects INT;
	DECLARE avg_score FLOAT;

	SELECT SUM(score) INTO total_score FROM corrections WHERE corrections.user_id = user_id;

	SELECT COUNT(*) INTO total_projects FROM corrections WHERE corrections.user_id = user_id;

	SET avg_score = total_score / total_projects;

	UPDATE users SET average_score = avg_score WHERE id = user_id;
END //

DELIMITER ;
