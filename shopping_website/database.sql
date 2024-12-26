-- Insert sample users
INSERT INTO Users (Name, Email, Password, IsAdmin)
VALUES 
('John Doe', 'john.doe@example.com', 'hashed_password_1', FALSE),
('Jane Smith', 'jane.smith@example.com', 'hashed_password_2', FALSE),
('Admin User', 'admin@example.com', 'hashed_password_3', TRUE);

-- Insert sample products
INSERT INTO Products (Name, Description, Price, Stock)
VALUES 
('Laptop', 'A high-performance laptop', 999.99, 10),
('Smartphone', 'Latest model smartphone', 799.99, 15),
('Headphones', 'Noise-canceling headphones', 199.99, 30),
('Keyboard', 'Mechanical keyboard', 89.99, 20),
('Monitor', '4K Ultra HD Monitor', 299.99, 5);

-- Insert sample carts
INSERT INTO Carts (UserID)
VALUES 
(1), 
(2);

-- Insert sample cart items
INSERT INTO CartItems (CartID, ProductID, Quantity)
VALUES 
(1, 1, 1),  -- John Doe's cart: 1 Laptop
(1, 3, 2),  -- John Doe's cart: 2 Headphones
(2, 2, 1);  -- Jane Smith's cart: 1 Smartphone

-- Insert sample orders
INSERT INTO Orders (UserID, TotalAmount, Status)
VALUES 
(1, 1399.97, 'Shipped'),  -- John Doe's order
(2, 799.99, 'Pending');   -- Jane Smith's order

-- Insert sample order items
INSERT INTO OrderItems (OrderID, ProductID, Quantity)
VALUES 
(1, 1, 1),  -- John Doe's order: 1 Laptop
(1, 3, 2),  -- John Doe's order: 2 Headphones
(2, 2, 1);  -- Jane Smith's order: 1 Smartphone

-- Insert sample payments
INSERT INTO Payments (OrderID, PaymentDate, Amount, Status)
VALUES 
(1, NOW(), 1399.97, 'Completed'),  -- Payment for John Doe's order
(2, NOW(), 799.99, 'Pending');    -- Payment for Jane Smith's order

