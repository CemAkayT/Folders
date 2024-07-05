
CREATE table company (
    id INT NOT NULL IDENTITY PRIMARY KEY,
    name VARCHAR(255),
    employees INT
);


INSERT INTO Company (name, employees) VALUES
('Apple Inc.', 147000),
('Amazon.com Inc.', 810000),
('Microsoft Corporation', 163000),
('Alphabet Inc. (Google)', 150000),
('Facebook, Inc.', 60654),
('Alibaba Group Holding Limited', 254600),
('Tencent Holdings Limited', 88000),
('Samsung Electronics Co., Ltd.', 320671),
('Toyota Motor Corporation', 364445),
('Volkswagen AG', 662043);
