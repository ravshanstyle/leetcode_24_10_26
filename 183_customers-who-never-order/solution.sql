select name as Customers
from Customers 
--left join Orders on Customers.id = Orders.customerId
where id not in (select customerId from Orders );