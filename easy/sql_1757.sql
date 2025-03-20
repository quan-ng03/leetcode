"""
SELECT returns the variable specified, FROM specifies the table to select from,
and WHERE specifies the conditions that must be met.
"""
SELECT product_id 
FROM Products
WHERE 
    low_fats = 'Y' AND recyclable = 'Y';