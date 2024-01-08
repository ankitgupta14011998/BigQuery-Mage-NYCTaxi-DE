-- fare amount paid by mode
select b.payment_type_name,sum(a.total_amount) from `steam-genius-410610.uber_dataengineering_project.fact_table` a
join 
`steam-genius-410610.uber_dataengineering_project.payment_dim` b
on a.payment_id=b.payment_id
group by b.payment_type_name;

--avg fare amount paid by different modes

select b.payment_type_name,avg(a.total_amount) from `steam-genius-410610.uber_dataengineering_project.fact_table` a
join 
`steam-genius-410610.uber_dataengineering_project.payment_dim` b
on a.payment_id=b.payment_id
group by b.payment_type_name;

--avg,min and max time of trips

SELECT AVG(DIFF),MAX(DIFF),MIN(DIFF) FROM (select TIMESTAMP_diff(TIMESTAMP(b.tpep_dropoff_datetime),TIMESTAMP(b.tpep_pickup_datetime),MINUTE) AS DIFF from `steam-genius-410610.uber_dataengineering_project.fact_table` a
join 
`steam-genius-410610.uber_dataengineering_project.datetime_dim` b
on a.datetime_id=b.datetime_id);

--top 10 pickup locations based on number of trips
alter table `steam-genius-410610.uber_dataengineering_project.fact_table` rename column location_id_y to dropoff_location_id;

select count(*),b.location_type_name as most_pickedup_location from `steam-genius-410610.uber_dataengineering_project.fact_table` a 
join `steam-genius-410610.uber_dataengineering_project.location_dim` b
on a.pickup_location_id=b.location_id
group by b.location_type_name
order by count(*) desc;

select count(*),b.location_type_name as most_droppedoff_location from `steam-genius-410610.uber_dataengineering_project.fact_table` a 
join `steam-genius-410610.uber_dataengineering_project.location_dim` b
on a.dropoff_location_id=b.location_id
group by b.location_type_name
order by count(*) desc;

--total number of trips by passenger count

select passenger_count,count(*) from `steam-genius-410610.uber_dataengineering_project.fact_table` a 
join `steam-genius-410610.uber_dataengineering_project.passenger_count_dim` b
on a.passenger_count_id=b.passenger_count_id
group by passenger_count;

-- avg fare amount by hour of the day

select b.pick_hour,sum(total_amount) as amount from `steam-genius-410610.uber_dataengineering_project.fact_table` a
join `steam-genius-410610.uber_dataengineering_project.datetime_dim` b
on a.datetime_id=b.datetime_id
group by b.pick_hour
order by amount desc
