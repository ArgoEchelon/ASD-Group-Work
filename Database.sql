PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE staff
        (staffId INT(4) PRIMARY KEY NOT NULL,
        password INT(4) NOT NULL,
        firstname VARCHAR(20) NOT NULL,
        lastname VARCHAR(20) NOT NULL,
        staffType VARCHAR(10) CHECK(staffType IN ('Staff', 'Manager', 'Admin')) NOT NULL,
        restaurantId INT(4) NOT NULL,
        FOREIGN KEY (restaurantId) REFERENCES restaurant (restaurantId)
        );
INSERT INTO staff VALUES(1234,1234,'Phoenix','Burke','Admin',1);
INSERT INTO staff VALUES(2345,2345,'Zak','Kannemeyer','Manager',1);
INSERT INTO staff VALUES(3456,3456,'Jack','Wemyss','Staff',1);
CREATE TABLE restaurant
        (restaurantId INT(4) PRIMARY KEY NOT NULL,
        restaurantName VARCHAR(50) NOT NULL
        );
INSERT INTO restaurant VALUES(1,'Bristol');
INSERT INTO restaurant VALUES(2,'Edinburgh');
INSERT INTO restaurant VALUES(3,'Glasgow');
INSERT INTO restaurant VALUES(4,'Manchester');
INSERT INTO restaurant VALUES(5,'London');
INSERT INTO restaurant VALUES(6,'Cardiff');
INSERT INTO restaurant VALUES(7,'Sheffield');
INSERT INTO restaurant VALUES(8,'Liverpool');
INSERT INTO restaurant VALUES(9,'Leeds');
INSERT INTO restaurant VALUES(10,'Newcastle');
CREATE TABLE tables
        (tableId INT(3) PRIMARY KEY NOT NULL UNIQUE,
        tableSize INT(2) NOT NULL,
        restaurantId INT(4) NOT NULL,
        FOREIGN KEY (restaurantId) REFERENCES restaurant (restaurantId)
        );
INSERT INTO tables VALUES(0,4,1);
INSERT INTO tables VALUES(1,4,1);
INSERT INTO tables VALUES(2,4,1);
INSERT INTO tables VALUES(3,4,1);
INSERT INTO tables VALUES(4,4,1);
INSERT INTO tables VALUES(5,4,1);
INSERT INTO tables VALUES(6,4,1);
INSERT INTO tables VALUES(7,4,1);
INSERT INTO tables VALUES(8,4,1);
INSERT INTO tables VALUES(9,2,1);
INSERT INTO tables VALUES(10,2,1);
INSERT INTO tables VALUES(11,2,1);
INSERT INTO tables VALUES(12,2,1);
INSERT INTO tables VALUES(13,10,1);
INSERT INTO tables VALUES(14,10,1);
INSERT INTO tables VALUES(15,8,1);
INSERT INTO tables VALUES(16,8,1);
INSERT INTO tables VALUES(17,8,1);
INSERT INTO tables VALUES(18,8,1);
INSERT INTO tables VALUES(19,6,1);
INSERT INTO tables VALUES(20,6,1);
INSERT INTO tables VALUES(21,6,1);
INSERT INTO tables VALUES(22,6,1);
INSERT INTO tables VALUES(23,6,1);
INSERT INTO tables VALUES(24,6,1);
INSERT INTO tables VALUES(25,6,1);
INSERT INTO tables VALUES(26,6,1);
INSERT INTO tables VALUES(27,6,1);
INSERT INTO tables VALUES(28,6,1);
INSERT INTO tables VALUES(29,6,1);
CREATE TABLE reservationTimes
        (reservationTimeId INT(3) PRIMARY KEY NOT NULL,
        timeSlots VARCHAR(10)
        );
INSERT INTO reservationTimes VALUES(0,'12:00');
INSERT INTO reservationTimes VALUES(1,'13:00');
INSERT INTO reservationTimes VALUES(2,'14:00');
INSERT INTO reservationTimes VALUES(3,'15:00');
INSERT INTO reservationTimes VALUES(4,'16:00');
INSERT INTO reservationTimes VALUES(5,'17:00');
INSERT INTO reservationTimes VALUES(6,'18:00');
INSERT INTO reservationTimes VALUES(7,'19:00');
INSERT INTO reservationTimes VALUES(8,'20:00');
INSERT INTO reservationTimes VALUES(9,'21:00');
INSERT INTO reservationTimes VALUES(10,'22:00');
CREATE TABLE reservation
        (reservationId INT(3) PRIMARY KEY NOT NULL,
        customerName VARCHAR(20) NOT NULL,
        tableId INT(3),
        reservationTimeId INT(3),
        reservationDate DATETIME,
        restaurantId INT(4) NOT NULL,
        FOREIGN KEY (tableId) REFERENCES tables (tableId),
        FOREIGN KEY (reservationTimeId) REFERENCES reservationTimes (reservationTimeId),
        FOREIGN KEY (restaurantId) REFERENCES restaurant (restaurantId)
        );
CREATE TABLE inventory
        (stockId INT(4) PRIMARY KEY NOT NULL,
        stockNum INT(3) NOT NULL,
        stockPrice DECIMAL(10,2) NOT NULL,
        restaurantId INT(4) NOT NULL,
        FOREIGN KEY (restaurantId) REFERENCES restaurant (restaurantId)
        );
INSERT INTO inventory VALUES(1,50,10.99000000000000021,1);
INSERT INTO inventory VALUES(2,30,15.75,1);
INSERT INTO inventory VALUES(3,75,8.5,1);
INSERT INTO inventory VALUES(4,40,12.25,1);
INSERT INTO inventory VALUES(5,60,9.99000000000000021,1);
INSERT INTO inventory VALUES(6,25,18.5,1);
INSERT INTO inventory VALUES(7,55,11.25,1);
INSERT INTO inventory VALUES(8,35,14.99000000000000021,1);
INSERT INTO inventory VALUES(9,70,7.5,1);
INSERT INTO inventory VALUES(10,45,13.75,1);
CREATE TABLE menu
        (itemId INT(4) PRIMARY KEY NOT NULL,
        itemName VARCHAR(40) NOT NULL,
        price DECIMAL(10,2) NOT NULL,
        menuCategory VARCHAR(10) CHECK(menuCategory IN ('STARTER', 'MAIN', 'SIDE','DESSERT', 'DRINK')) NOT NULL,
        allergens VARCHAR(20),
        restaurantId INT(4) NOT NULL,
        FOREIGN KEY (restaurantId) REFERENCES restaurant (restaurantId)
        );
INSERT INTO menu VALUES(1,'Garlic Bread',5.990000000000000213,'STARTER','Garlic',1);
INSERT INTO menu VALUES(2,'Spaghetti Bolognese',12.5,'MAIN','Gluten',1);
INSERT INTO menu VALUES(3,'Caprese Salad',8.990000000000000213,'STARTER','Dairy',1);
INSERT INTO menu VALUES(4,'Chicken Parmesan',14.94999999999999929,'MAIN','Dairy, Gluten',1);
INSERT INTO menu VALUES(5,'Bruschetta',3.990000000000000213,'SIDE','Tomato, Garlic',1);
INSERT INTO menu VALUES(6,'Tiramisu',6.990000000000000213,'DESSERT','Dairy, Egg',1);
INSERT INTO menu VALUES(7,'Mushroom Risotto',11.75,'MAIN','Dairy',1);
INSERT INTO menu VALUES(8,'Minestrone Soup',4.5,'STARTER','None',1);
INSERT INTO menu VALUES(9,'Cannoli',3.490000000000000213,'DESSERT','Dairy',1);
INSERT INTO menu VALUES(10,'Margherita Pizza',9.99000000000000021,'MAIN','Dairy',1);
INSERT INTO menu VALUES(11,'Fettuccine Alfredo',10.75,'MAIN','Dairy',1);
INSERT INTO menu VALUES(12,'Antipasto Platter',15.99000000000000021,'STARTER','Dairy, Meat',1);
INSERT INTO menu VALUES(13,'Limoncello Sorbet',5.25,'DESSERT','None',1);
INSERT INTO menu VALUES(14,'Pesto Pasta with Sun-Dried Tomatoes',13.5,'MAIN','Nuts, Dairy',1);
INSERT INTO menu VALUES(15,'Arancini',8.990000000000000213,'STARTER','Dairy',1);
INSERT INTO menu VALUES(16,'Risotto al Nero di Seppia',12.5,'MAIN','Seafood, Dairy',1);
INSERT INTO menu VALUES(17,'Tuscan White Bean Soup',4.990000000000000213,'STARTER','None',1);
INSERT INTO menu VALUES(18,'Cappuccino',3.75,'DRINK','Dairy',1);
INSERT INTO menu VALUES(19,'Margherita Flatbread',7.25,'MAIN','Dairy',1);
INSERT INTO menu VALUES(20,'Panna Cotta',6.490000000000000213,'DESSERT','Dairy',1);
INSERT INTO menu VALUES(21,'Insalata di Rucola',8.75,'STARTER','None',1);
INSERT INTO menu VALUES(22,'Gnocchi alla Sorrentina',11.25,'MAIN','Dairy',1);
INSERT INTO menu VALUES(23,'Lemon Granita',4.25,'DESSERT','None',1);
INSERT INTO menu VALUES(24,'Calamari Fritti',9.99000000000000021,'STARTER','Seafood',1);
INSERT INTO menu VALUES(25,'Osso Buco',16.75,'MAIN','None',1);
INSERT INTO menu VALUES(26,'Affogato',5.5,'DESSERT','Dairy',1);
INSERT INTO menu VALUES(27,'Braciola di Maiale',12.25,'MAIN','None',1);
INSERT INTO menu VALUES(28,'Pistachio Gelato',4.25,'DESSERT','Nuts, Dairy',1);
INSERT INTO menu VALUES(29,'Cacio e Pepe',10.5,'MAIN','Dairy',1);
INSERT INTO menu VALUES(30,'Espresso',2.490000000000000213,'DRINK','None',1);
INSERT INTO menu VALUES(31, 'Lemonade', 2.29, 'DRINK', 'None', 1);
INSERT INTO menu VALUES(32, 'Soda', 1.99, 'DRINK', 'None', 1);
INSERT INTO menu VALUES(33, 'French Fries', 3.99, 'SIDE', 'None', 1);
INSERT INTO menu VALUES(34, 'Garlic Knots', 4.99, 'SIDE', 'None', 1);
INSERT INTO menu VALUES(35, 'Steamed Vegetables', 6.99, 'SIDE', 'None', 1);
INSERT INTO menu VALUES(36, 'Sparkling Water', 2.49, 'DRINK', 'None', 1);

CREATE TABLE menuIngredients
        (menuIngredientsId INT(4) PRIMARY KEY NOT NULL,
        stockId INT(4),
        itemId INT(4),
        quantity INT(4),
        restaurantId INT(4) NOT NULL,
        FOREIGN KEY (stockId) REFERENCES inventory (stockId),
        FOREIGN KEY (itemId) REFERENCES menu (itemId),
        FOREIGN KEY (restaurantId) REFERENCES restaurant (restaurantId)
        );
INSERT INTO menuIngredients VALUES(1,1,1,10,1);
INSERT INTO menuIngredients VALUES(2,2,2,15,1);
INSERT INTO menuIngredients VALUES(3,3,3,20,1);
INSERT INTO menuIngredients VALUES(4,4,4,12,1);
INSERT INTO menuIngredients VALUES(5,5,5,25,1);
INSERT INTO menuIngredients VALUES(6,6,6,18,1);
INSERT INTO menuIngredients VALUES(7,7,7,22,1);
INSERT INTO menuIngredients VALUES(8,8,8,30,1);
INSERT INTO menuIngredients VALUES(9,9,9,14,1);
INSERT INTO menuIngredients VALUES(10,10,10,16,1);
INSERT INTO menuIngredients VALUES(11,11,11,10,1);
INSERT INTO menuIngredients VALUES(12,12,12,8,1);
INSERT INTO menuIngredients VALUES(13,13,13,25,1);
INSERT INTO menuIngredients VALUES(14,14,14,20,1);
INSERT INTO menuIngredients VALUES(15,15,15,15,1);
INSERT INTO menuIngredients VALUES(16,16,16,18,1);
INSERT INTO menuIngredients VALUES(17,17,17,30,1);
INSERT INTO menuIngredients VALUES(18,18,18,12,1);
INSERT INTO menuIngredients VALUES(19,19,19,14,1);
INSERT INTO menuIngredients VALUES(20,20,20,20,1);
INSERT INTO menuIngredients VALUES(21,21,21,15,1);
INSERT INTO menuIngredients VALUES(22,22,22,18,1);
INSERT INTO menuIngredients VALUES(23,23,23,25,1);
INSERT INTO menuIngredients VALUES(24,24,24,20,1);
INSERT INTO menuIngredients VALUES(25,25,25,12,1);
INSERT INTO menuIngredients VALUES(26,26,26,15,1);
INSERT INTO menuIngredients VALUES(27,27,27,18,1);
INSERT INTO menuIngredients VALUES(28,28,28,22,1);
INSERT INTO menuIngredients VALUES(29,29,29,10,1);
INSERT INTO menuIngredients VALUES(30,30,30,25,1);
CREATE TABLE orders
        (orderId INT(4) NOT NULL,
        tableId INT(3) NOT NULL,
        itemId INT(4) NOT NULL,
        quantity INT(4) NOT NULL,
        orderStatus VARCHAR(20) NOT NULL,
        totalPrice DECIMAL(10,2) NOT NULL,
        orderDate DATETIME NOT NULL,
        restaurantId INT(4) NOT NULL,
        FOREIGN KEY (tableId) REFERENCES tables (tableId),
        FOREIGN KEY (itemId) REFERENCES menu (itemId),
        FOREIGN KEY (restaurantId) REFERENCES restaurant (restaurantId)
        );
CREATE TABLE payments
        (paymentId INT(4) NOT NULL,
        amount DECIMAL(10,2) NOT NULL,
        paymentDate DATETIME NOT NULL,
        restaurantId INT(4) NOT NULL,
        FOREIGN KEY (restaurantId) REFERENCES restaurant (restaurantId)
        );
COMMIT;
