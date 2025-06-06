INSERT INTO mango_pests_planttype (id, name) VALUES (1, 'PlantType_1');
INSERT INTO mango_pests_planttype (id, name) VALUES (2, 'PlantType_2');
INSERT INTO mango_pests_planttype (id, name) VALUES (3, 'PlantType_3');
INSERT INTO mango_pests_planttype (id, name) VALUES (4, 'PlantType_4');
INSERT INTO mango_pests_planttype (id, name) VALUES (5, 'PlantType_5');
INSERT INTO mango_pests_planttype (id, name) VALUES (6, 'PlantType_6');
INSERT INTO mango_pests_planttype (id, name) VALUES (7, 'PlantType_7');
INSERT INTO mango_pests_planttype (id, name) VALUES (8, 'PlantType_8');
INSERT INTO mango_pests_planttype (id, name) VALUES (9, 'PlantType_9');
INSERT INTO mango_pests_planttype (id, name) VALUES (10, 'PlantType_10');
INSERT INTO mango_pests_pest (id, name, scientific_name, description, image, plant_type_id) VALUES (1, 'Pest_1', 'Pestus scientificus 1', 'Description for Pest_1', 'image_1.jpg', 1);
INSERT INTO mango_pests_pest (id, name, scientific_name, description, image, plant_type_id) VALUES (2, 'Pest_2', 'Pestus scientificus 2', 'Description for Pest_2', 'image_2.jpg', 2);
INSERT INTO mango_pests_pest (id, name, scientific_name, description, image, plant_type_id) VALUES (3, 'Pest_3', 'Pestus scientificus 3', 'Description for Pest_3', 'image_3.jpg', 3);
INSERT INTO mango_pests_pest (id, name, scientific_name, description, image, plant_type_id) VALUES (4, 'Pest_4', 'Pestus scientificus 4', 'Description for Pest_4', 'image_4.jpg', 4);
INSERT INTO mango_pests_pest (id, name, scientific_name, description, image, plant_type_id) VALUES (5, 'Pest_5', 'Pestus scientificus 5', 'Description for Pest_5', 'image_5.jpg', 5);
INSERT INTO mango_pests_pest (id, name, scientific_name, description, image, plant_type_id) VALUES (6, 'Pest_6', 'Pestus scientificus 6', 'Description for Pest_6', 'image_6.jpg', 6);
INSERT INTO mango_pests_pest (id, name, scientific_name, description, image, plant_type_id) VALUES (7, 'Pest_7', 'Pestus scientificus 7', 'Description for Pest_7', 'image_7.jpg', 7);
INSERT INTO mango_pests_pest (id, name, scientific_name, description, image, plant_type_id) VALUES (8, 'Pest_8', 'Pestus scientificus 8', 'Description for Pest_8', 'image_8.jpg', 8);
INSERT INTO mango_pests_pest (id, name, scientific_name, description, image, plant_type_id) VALUES (9, 'Pest_9', 'Pestus scientificus 9', 'Description for Pest_9', 'image_9.jpg', 9);
INSERT INTO mango_pests_pest (id, name, scientific_name, description, image, plant_type_id) VALUES (10, 'Pest_10', 'Pestus scientificus 10', 'Description for Pest_10', 'image_10.jpg', 10);
INSERT INTO mango_pests_farmblock (id, name, location_description, grower_id) VALUES (1, 'Block_1', 'Location 1', 1);
INSERT INTO mango_pests_farmblock (id, name, location_description, grower_id) VALUES (2, 'Block_2', 'Location 2', 1);
INSERT INTO mango_pests_farmblock (id, name, location_description, grower_id) VALUES (3, 'Block_3', 'Location 3', 1);
INSERT INTO mango_pests_farmblock (id, name, location_description, grower_id) VALUES (4, 'Block_4', 'Location 4', 1);
INSERT INTO mango_pests_farmblock (id, name, location_description, grower_id) VALUES (5, 'Block_5', 'Location 5', 1);
INSERT INTO mango_pests_farmblock (id, name, location_description, grower_id) VALUES (6, 'Block_6', 'Location 6', 1);
INSERT INTO mango_pests_farmblock (id, name, location_description, grower_id) VALUES (7, 'Block_7', 'Location 7', 1);
INSERT INTO mango_pests_farmblock (id, name, location_description, grower_id) VALUES (8, 'Block_8', 'Location 8', 1);
INSERT INTO mango_pests_farmblock (id, name, location_description, grower_id) VALUES (9, 'Block_9', 'Location 9', 1);
INSERT INTO mango_pests_farmblock (id, name, location_description, grower_id) VALUES (10, 'Block_10', 'Location 10', 1);
INSERT INTO mango_pests_pestcheck (id, date_checked, part_of_plant, infestation_level, num_trees, positives, notes, path_pattern, farm_block_id, pest_id) VALUES (1, '2025-05-24', 'Roots', 'None', 72, 30, 'Check notes 1', 'Linear', 6, 4);
INSERT INTO mango_pests_pestcheck (id, date_checked, part_of_plant, infestation_level, num_trees, positives, notes, path_pattern, farm_block_id, pest_id) VALUES (2, '2025-05-21', 'Leaves', 'Moderate', 20, 0, 'Check notes 2', 'Random', 2, 4);
INSERT INTO mango_pests_pestcheck (id, date_checked, part_of_plant, infestation_level, num_trees, positives, notes, path_pattern, farm_block_id, pest_id) VALUES (3, '2025-05-28', 'Roots', 'High', 22, 5, 'Check notes 3', 'Zigzag', 10, 7);
INSERT INTO mango_pests_pestcheck (id, date_checked, part_of_plant, infestation_level, num_trees, positives, notes, path_pattern, farm_block_id, pest_id) VALUES (4, '2025-05-23', 'Roots', 'High', 81, 18, 'Check notes 4', 'Zigzag', 4, 4);
INSERT INTO mango_pests_pestcheck (id, date_checked, part_of_plant, infestation_level, num_trees, positives, notes, path_pattern, farm_block_id, pest_id) VALUES (5, '2025-05-07', 'Stem', 'High', 16, 7, 'Check notes 5', 'Grid', 6, 7);
INSERT INTO mango_pests_pestcheck (id, date_checked, part_of_plant, infestation_level, num_trees, positives, notes, path_pattern, farm_block_id, pest_id) VALUES (6, '2025-05-12', 'Leaves', 'Moderate', 89, 27, 'Check notes 6', 'Linear', 5, 5);
INSERT INTO mango_pests_pestcheck (id, date_checked, part_of_plant, infestation_level, num_trees, positives, notes, path_pattern, farm_block_id, pest_id) VALUES (7, '2025-05-19', 'Fruits', 'Low', 62, 29, 'Check notes 7', 'Zigzag', 4, 8);
INSERT INTO mango_pests_pestcheck (id, date_checked, part_of_plant, infestation_level, num_trees, positives, notes, path_pattern, farm_block_id, pest_id) VALUES (8, '2025-05-06', 'Leaves', 'Moderate', 45, 21, 'Check notes 8', 'Random', 4, 2);
INSERT INTO mango_pests_pestcheck (id, date_checked, part_of_plant, infestation_level, num_trees, positives, notes, path_pattern, farm_block_id, pest_id) VALUES (9, '2025-05-04', 'Fruits', 'None', 36, 12, 'Check notes 9', 'Zigzag', 3, 10);
INSERT INTO mango_pests_pestcheck (id, date_checked, part_of_plant, infestation_level, num_trees, positives, notes, path_pattern, farm_block_id, pest_id) VALUES (10, '2025-06-02', 'Leaves', 'High', 41, 5, 'Check notes 10', 'Random', 7, 3);
INSERT INTO mango_pests_pestcheck (id, date_checked, part_of_plant, infestation_level, num_trees, positives, notes, path_pattern, farm_block_id, pest_id) VALUES (11, '2025-05-18', 'Fruits', 'Moderate', 87, 18, 'Check notes 11', 'Random', 2, 9);
INSERT INTO mango_pests_pestcheck (id, date_checked, part_of_plant, infestation_level, num_trees, positives, notes, path_pattern, farm_block_id, pest_id) VALUES (12, '2025-05-24', 'Leaves', 'None', 13, 1, 'Check notes 12', 'Linear', 6, 1);
INSERT INTO mango_pests_pestcheck (id, date_checked, part_of_plant, infestation_level, num_trees, positives, notes, path_pattern, farm_block_id, pest_id) VALUES (13, '2025-05-03', 'Stem', 'High', 29, 1, 'Check notes 13', 'Linear', 9, 7);
INSERT INTO mango_pests_pestcheck (id, date_checked, part_of_plant, infestation_level, num_trees, positives, notes, path_pattern, farm_block_id, pest_id) VALUES (14, '2025-05-24', 'Stem', 'Low', 62, 27, 'Check notes 14', 'Random', 5, 5);
INSERT INTO mango_pests_pestcheck (id, date_checked, part_of_plant, infestation_level, num_trees, positives, notes, path_pattern, farm_block_id, pest_id) VALUES (15, '2025-05-16', 'Stem', 'None', 85, 3, 'Check notes 15', 'Random', 10, 6);
INSERT INTO mango_pests_pestcheck (id, date_checked, part_of_plant, infestation_level, num_trees, positives, notes, path_pattern, farm_block_id, pest_id) VALUES (16, '2025-05-08', 'Stem', 'Moderate', 78, 21, 'Check notes 16', 'Linear', 2, 8);
INSERT INTO mango_pests_pestcheck (id, date_checked, part_of_plant, infestation_level, num_trees, positives, notes, path_pattern, farm_block_id, pest_id) VALUES (17, '2025-05-08', 'Fruits', 'Moderate', 17, 0, 'Check notes 17', 'Zigzag', 3, 6);
INSERT INTO mango_pests_pestcheck (id, date_checked, part_of_plant, infestation_level, num_trees, positives, notes, path_pattern, farm_block_id, pest_id) VALUES (18, '2025-05-10', 'Fruits', 'High', 17, 8, 'Check notes 18', 'Zigzag', 10, 10);
INSERT INTO mango_pests_pestcheck (id, date_checked, part_of_plant, infestation_level, num_trees, positives, notes, path_pattern, farm_block_id, pest_id) VALUES (19, '2025-05-08', 'Roots', 'Moderate', 87, 22, 'Check notes 19', 'Random', 3, 7);
INSERT INTO mango_pests_pestcheck (id, date_checked, part_of_plant, infestation_level, num_trees, positives, notes, path_pattern, farm_block_id, pest_id) VALUES (20, '2025-06-02', 'Fruits', 'Low', 50, 23, 'Check notes 20', 'Grid', 4, 9);
