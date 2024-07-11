-- trigger that decreases quantity attribute for an item in table items whenever a new row with the item is inserted into table order
DELIMITER $$
CREATE TRIGGER update_quantity
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
    UPDATE items SET quantity = (quantity - NEW.number) WHERE name = NEW.item_name;
END
$$
