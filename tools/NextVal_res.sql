select MAX(id) from selected_items;
select nextval('selected_items_id_seq');
SELECT setval('selected_items_id_seq', (SELECT MAX(id) FROM selected_items));