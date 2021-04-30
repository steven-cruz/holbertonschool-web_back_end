-- Buy buy buy
-- script that creates a trigger that decreases the quantity of
-- an item after adding a new order.
CREATE TRIGGER buy_trigger
AFTER INSERT ON orders
FOR EACH ROW
UPDATE items SET quantity = quantity - NEW.item_name;
