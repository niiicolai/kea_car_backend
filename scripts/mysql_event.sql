--
-- Dumping events for database 'kea_cars_dev'
--
DROP EVENT IF EXISTS delete_old_none_purchased_cars;
DELIMITER //
CREATE EVENT delete_old_none_purchased_cars
ON SCHEDULE EVERY 1 DAY
DO
BEGIN
	DELETE car
	FROM cars car
	INNER JOIN car_purchase_view cpv ON car.id = cpv.car_id
	WHERE cpv.is_past_deadline = TRUE;
END //
DELIMITER ;
