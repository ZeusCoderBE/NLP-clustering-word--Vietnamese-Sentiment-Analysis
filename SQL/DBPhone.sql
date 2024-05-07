Create DataBase SalesPhone
go
use SalesPhone
go
CREATE TABLE users (
    id INT identity PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    full_name nVARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL
);

CREATE TABLE comments (
    id INT identity PRIMARY KEY,
    user_id INT,
    comment NVARCHAR(MAX),
    FOREIGN KEY (user_id) REFERENCES users(id)
);
INSERT INTO users (username, full_name, password) VALUES
('user1', N'Nguyễn Văn A', '123'),
('user2', N'Trần Thị B', '123'),
('user3', N'Lê Văn C', '123'),
('user4', N'Phạm Thị D', '123');
