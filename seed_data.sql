-- Insert real mango plant types
INSERT INTO mango_pests_planttype (id, name) VALUES (1, 'Kensington Pride');
INSERT INTO mango_pests_planttype (id, name) VALUES (2, 'R2E2');
INSERT INTO mango_pests_planttype (id, name) VALUES (3, 'Honey Gold');
INSERT INTO mango_pests_planttype (id, name) VALUES (4, 'Calypso');
INSERT INTO mango_pests_planttype (id, name) VALUES (5, 'Keitt');
INSERT INTO mango_pests_planttype (id, name) VALUES (6, 'Palmer');
INSERT INTO mango_pests_planttype (id, name) VALUES (7, 'Nam Doc Mai');
INSERT INTO mango_pests_planttype (id, name) VALUES (8, 'Tommy Atkins');
INSERT INTO mango_pests_planttype (id, name) VALUES (9, 'Kent');
INSERT INTO mango_pests_planttype (id, name) VALUES (10, 'Haden');


INSERT INTO mango_pests_pest (id, name, scientific_name, description, plant_type_id, owner_id, image)
VALUES (
    1,
    'Anthracnose',
    'Colletotrichum gloeosporioides',
    'A fungal disease causing black lesions on fruit and flowers.',
    1,
    (SELECT id FROM auth_user WHERE username = 'admin'),
    NULL
);