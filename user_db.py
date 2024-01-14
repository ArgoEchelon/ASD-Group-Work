#Phoenix Burke Chang 21026891
#Zak Kannemeyer 22021286
#Leo Gan 22007334 
#Jack Wemyss 22027196
from DataAccessObject import *
c = conn.cursor()

try:
    #staff
    c.execute('''
        CREATE TABLE staff
        (staffId INT(4) PRIMARY KEY NOT NULL,
        password INT(4) NOT NULL,
        firstname VARCHAR(20) NOT NULL,
        lastname VARCHAR(20) NOT NULL,
        staffType VARCHAR(10) CHECK(staffType IN ('Staff', 'Manager', 'Admin', 'Chef')) NOT NULL,
        restaurantId INT(4) NOT NULL,
        FOREIGN KEY (restaurantId) REFERENCES restaurant (restaurantId)
        )
    ''')

    #insert admin details
    c.execute('''
        INSERT INTO staff
        (staffId, firstname, lastname, password, staffType, restaurantId)
        VALUES (1234, 'Phoenix', 'Burke', 1234, 'Admin', 1),
              (2345, 'Zak', 'Kannemeyer', 2345, 'Manager', 2),
              (3456, 'Jack', 'Wemyss', 3456, 'Chef', 3),
              (4567, 'Leo', 'Gan', 4567, 'Staff', 4);
    ''')

    #restaurants
    c.execute('''
        CREATE TABLE restaurant
        (restaurantId INT(4) PRIMARY KEY NOT NULL,
        restaurantName VARCHAR(50) NOT NULL
        )
    ''')

    c.execute('''
        INSERT INTO restaurant
        (restaurantId, restaurantName)
        VALUES
            (1, 'Bristol'),
            (2, 'Edinburgh'),
            (3, 'Glasgow'),
            (4, 'Manchester'),
            (5, 'London'),
            (6, 'Cardiff'),
            (7, 'Sheffield'),
            (8, 'Liverpool'),
            (9, 'Leeds'),
            (10, 'Newcastle');
    ''')

    #table
    c.execute('''
        CREATE TABLE tables
        (tableId INT(3) PRIMARY KEY NOT NULL UNIQUE,
        tableSize INT(2) NOT NULL,
        restaurantId INT(4) NOT NULL,
        FOREIGN KEY (restaurantId) REFERENCES restaurant (restaurantId)
        )
    ''')

    c.execute('''
        INSERT INTO tables
        (tableId, tableSize, restaurantId)
        VALUES
            (0,4,1),
            (1,4,1),
            (2,4,1),
            (3,4,1),
            (4,4,1),
            (5,4,1),
            (6,4,1),
            (7,4,1),
            (8,4,1),
            (9,2,1),
            (10,2,1),
            (11,2,1),
            (12,2,1),
            (13,10,1),
            (14,10,1),
            (15,8,1),
            (16,8,1),
            (17,8,1),
            (18,8,1),
            (19,6,1),
            (20,6,1),
            (21,6,1),
            (22,6,1),
            (23,6,1),
            (24,6,1),
            (25,6,1),
            (26,6,1),
            (27,6,1),
            (28,6,1),
            (29,6,1)
            ;
    ''')

    #reservations times
    c.execute('''
        CREATE TABLE reservationTimes
        (reservationTimeId INT(3) PRIMARY KEY NOT NULL,
        timeSlots VARCHAR(10)
        )
    ''')

    c.execute('''
    INSERT INTO reservationTimes
    (reservationTimeId, timeSlots)
    VALUES
        (0, '12:00'),
        (1, '13:00'),
        (2, '14:00'),
        (3, '15:00'),
        (4, '16:00'),
        (5, '17:00'),
        (6, '18:00'),
        (7, '19:00'),
        (8, '20:00'),
        (9, '21:00'),
        (10, '22:00')
        ;
    ''')
   
    #reservations
    c.execute('''
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
        )
    ''')


    #inventory
    c.execute('''
        CREATE TABLE inventory
        (stockId INT(4) PRIMARY KEY NOT NULL,
        stockNum INT(3) NOT NULL,
        stockPrice DECIMAL(10,2) NOT NULL,
        restaurantId INT(4) NOT NULL,
        FOREIGN KEY (restaurantId) REFERENCES restaurant (restaurantId)
        )
    ''')

    c.execute('''
        INSERT INTO inventory
        (stockId, stockNum, stockPrice, restaurantId)
        VALUES
            (1, 50, 10.99, 1),
            (2, 30, 15.75, 1),
            (3, 75, 8.50, 1),
            (4, 40, 12.25, 1),
            (5, 60, 9.99, 1),
            (6, 25, 18.50, 1),
            (7, 55, 11.25, 1),
            (8, 35, 14.99, 1),
            (9, 70, 7.50, 1),
            (10, 45, 13.75, 1);
    ''')

    #menu
    c.execute('''
        CREATE TABLE menu
        (itemId INT(4) PRIMARY KEY NOT NULL,
        itemName VARCHAR(40) NOT NULL,
        price DECIMAL(10,2) NOT NULL,
        menuCategory VARCHAR(10) CHECK(menuCategory IN ('STARTER', 'MAIN', 'SIDE','DESSERT', 'DRINK')) NOT NULL,
        allergens VARCHAR(20),
        restaurantId INT(4) NOT NULL,
        FOREIGN KEY (restaurantId) REFERENCES restaurant (restaurantId)
        )
    ''')

    c.execute('''
        INSERT INTO menu (itemId, itemName, price, menuCategory, allergens, restaurantId)
        VALUES
        (1, 'Garlic Bread', 5.99, 'STARTER', 'Garlic', 1),
        (2, 'Spaghetti Bolognese', 12.50, 'MAIN', 'Gluten', 1),
        (3, 'Caprese Salad', 8.99, 'STARTER', 'Dairy', 1),
        (4, 'Chicken Parmesan', 14.95, 'MAIN', 'Dairy, Gluten', 1),
        (5, 'Bruschetta', 3.99, 'SIDE', 'Tomato, Garlic', 1),
        (6, 'Tiramisu', 6.99, 'DESSERT', 'Dairy, Egg', 1),
        (7, 'Mushroom Risotto', 11.75, 'MAIN', 'Dairy', 1),
        (8, 'Minestrone Soup', 4.50, 'STARTER', 'None', 1),
        (9, 'Cannoli', 3.49, 'DESSERT', 'Dairy', 1),
        (10, 'Margherita Pizza', 9.99, 'MAIN', 'Dairy', 1),
        (11, 'Fettuccine Alfredo', 10.75, 'MAIN', 'Dairy', 1),
        (12, 'Antipasto Platter', 15.99, 'STARTER', 'Dairy, Meat', 1),
        (13, 'Limoncello Sorbet', 5.25, 'DESSERT', 'None', 1),
        (14, 'Pesto Pasta with Sun-Dried Tomatoes', 13.50, 'MAIN', 'Nuts, Dairy', 1),
        (15, 'Arancini', 8.99, 'STARTER', 'Dairy', 1),
        (16, 'Risotto al Nero di Seppia', 12.50, 'MAIN', 'Seafood, Dairy', 1),
        (17, 'Tuscan White Bean Soup', 4.99, 'STARTER', 'None', 1),
        (18, 'Cappuccino', 3.75, 'DRINK', 'Dairy', 1),
        (19, 'Margherita Flatbread', 7.25, 'MAIN', 'Dairy', 1),
        (20, 'Panna Cotta', 6.49, 'DESSERT', 'Dairy', 1),
        (21, 'Insalata di Rucola', 8.75, 'STARTER', 'None', 1),
        (22, 'Gnocchi alla Sorrentina', 11.25, 'MAIN', 'Dairy', 1),
        (23, 'Lemon Granita', 4.25, 'DESSERT', 'None', 1),
        (24, 'Calamari Fritti', 9.99, 'STARTER', 'Seafood', 1),
        (25, 'Osso Buco', 16.75, 'MAIN', 'None', 1),
        (26, 'Affogato', 5.50, 'DESSERT', 'Dairy', 1),
        (27, 'Braciola di Maiale', 12.25, 'MAIN', 'None', 1),
        (28, 'Pistachio Gelato', 4.25, 'DESSERT', 'Nuts, Dairy', 1),
        (29, 'Cacio e Pepe', 10.50, 'MAIN', 'Dairy', 1),
        (30, 'Espresso', 2.49, 'DRINK', 'None', 1),
        (31, 'Lemonade', 2.29, 'DRINK', 'None', 1),
        (32, 'Soda', 1.99, 'DRINK', 'None', 1),
        (33, 'French Fries', 3.99, 'SIDE', 'None', 1),
        (34, 'Garlic Knots', 4.99, 'SIDE', 'None', 1),
        (35, 'Steamed Vegetables', 6.99, 'SIDE', 'None', 1),
        (36, 'Sparkling Water', 2.49, 'DRINK', 'None', 1);
    ''')


    #menu ingredients
    c.execute('''
        CREATE TABLE menuIngredients
        (menuIngredientsId INT(4) PRIMARY KEY NOT NULL,
        stockId INT(4),
        itemId INT(4),
        quantity INT(4),
        restaurantId INT(4) NOT NULL,
        FOREIGN KEY (stockId) REFERENCES inventory (stockId),
        FOREIGN KEY (itemId) REFERENCES menu (itemId),
        FOREIGN KEY (restaurantId) REFERENCES restaurant (restaurantId)
        )
    ''')

    c.execute('''
        INSERT INTO menuIngredients (menuIngredientsId, stockId, itemId, quantity, restaurantId)
    VALUES
        (1, 1, 1, 10, 1),
        (2, 2, 2, 15, 1),
        (3, 3, 3, 20, 1),
        (4, 4, 4, 12, 1),
        (5, 5, 5, 25, 1),
        (6, 6, 6, 18, 1),
        (7, 7, 7, 22, 1),
        (8, 8, 8, 30, 1),
        (9, 9, 9, 14, 1),
        (10, 10, 10, 16, 1),
        (11, 11, 11, 10, 1),
        (12, 12, 12, 8, 1),
        (13, 13, 13, 25, 1),
        (14, 14, 14, 20, 1),
        (15, 15, 15, 15, 1),
        (16, 16, 16, 18, 1),
        (17, 17, 17, 30, 1),
        (18, 18, 18, 12, 1),
        (19, 19, 19, 14, 1),
        (20, 20, 20, 20, 1),
        (21, 21, 21, 15, 1),
        (22, 22, 22, 18, 1),
        (23, 23, 23, 25, 1),
        (24, 24, 24, 20, 1),
        (25, 25, 25, 12, 1),
        (26, 26, 26, 15, 1),
        (27, 27, 27, 18, 1),
        (28, 28, 28, 22, 1),
        (29, 29, 29, 10, 1),
        (30, 30, 30, 25, 1);
    ''')

    #order
    c.execute('''
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
        )
    ''')

    #payment
    c.execute('''
        CREATE TABLE payments
        (paymentId INT(4) NOT NULL,
        amount DECIMAL(10,2) NOT NULL,
        paymentDate DATETIME NOT NULL,
        restaurantId INT(4) NOT NULL,
        FOREIGN KEY (restaurantId) REFERENCES restaurant (restaurantId)
        )
    ''')

    conn.commit()

except Exception as e:
    print("Error:", e)
    conn.rollback()  # Rollback changes if an error occurs


#c.commit()
#conn.close()