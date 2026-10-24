select p2.id 
from Weather p1
join Weather p2
on p2.recordDate - p1.recordDate = 1
 and p1.temperature < p2.temperature;