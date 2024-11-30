// Create the `Customer` nodes;
CREATE CONSTRAINT FOR (c:Customer) REQUIRE c.id IS UNIQUE;
CREATE CONSTRAINT FOR (c:Customer) REQUIRE c.email IS UNIQUE;

// Insert data into the `Customer` nodes;
CREATE (c1:Customer {id:'0ac1d668-55aa-46a1-898a-8fa61457facb', email: 'henrik@gmail.com', phone_number:'10203040', first_name:'Henrik', last_name:'Henriksen', address:'Randomgade nr. 10 4. tv.'});
CREATE (c2:Customer {id:'bbbb06bc-268d-4f88-8b8e-3da4df118328', email: 'oli@oli.dk', phone_number:'12345678', first_name:'Oliver', last_name:'Jorgensen', address:'asdasd123'});
CREATE (c3:Customer {id:'daf830ad-be98-4f95-8fa8-3dc7efa540fe', email: 'tom@gmail.com', phone_number:'12345678', first_name:'Tom', last_name:'Tomsen', address:'Test 21'});
CREATE (c4:Customer {id:'f159bdaf-bc83-46c3-8a3f-f6b5c93ebbdc', email: 'james@gmail.com', phone_number:'12345678', first_name:'James', last_name:'Jamesen', address:'Test 21'});
CREATE (c5:Customer {id:'fc40f99e-13f0-460d-b79d-f75206acdd07', email: 'test@test.dk', phone_number:'12345678', first_name:'Test', last_name:'Teste', address:'Test 21'});

// Create the `SalesPerson` nodes;
CREATE CONSTRAINT FOR (sp:SalesPerson) REQUIRE sp.id IS UNIQUE;
CREATE CONSTRAINT FOR (sp:SalesPerson) REQUIRE sp.email IS UNIQUE;

// Insert data into the `SalesPerson` node;

// Create the 1st `SalesPerson` node;
CREATE (sp1:SalesPerson {
id:'d096d2e1-f06a-4555-9cd1-afa9f930f10c',
email: 'james@gmail.com',
hashed_password:'$2b$10$sB6/ocJJK9HodVv7qEozKO826Ik5gmZH/1GU/xReM1ijIjlA7hvTa',
first_name:'James',
last_name:'Jamesen'
});

// Create the 2nd `SalesPerson` node;
CREATE (sp2:SalesPerson {
id:'f9097a97-eca4-49b6-85a0-08423789c320',
email: 'hans@gmail.com',
hashed_password:'$2b$12$BKrnHSqhmb8NsKnUhhSGWeOj0Pnyx0so0xeXlUrDrNLplk2VnjDyK',
first_name:'Hans',
last_name:'Hansen'
});

// Create a unique constraint on the id property of Accessory nodes;
CREATE CONSTRAINT FOR (a:Accessory) REQUIRE a.id IS UNIQUE;

// Create a unique constraint on the name property of Accessory nodes;
CREATE CONSTRAINT FOR (a:Accessory) REQUIRE a.name IS UNIQUE;

// Insert data into the Accessory nodes;
CREATE (a1:Accessory {id:'0d61b4ee-2c27-400c-9ff5-38123284626c', name: 'Air Conditioning', price:99.95});

CREATE (a2:Accessory {id:'0f5a86c2-1db5-4486-b5e4-33b92fa3e741', name: 'Alloy Wheels', price:99.95});

CREATE (a3:Accessory {id:'31a9c926-cd49-4714-9be4-e145b982417e', name: 'Bluetooth Connectivity', price:99.95});

CREATE (a4:Accessory {id:'5b55aa29-8eb8-4f83-8110-f2bb50e7d08c', name: 'Sport Package', price:99.95});

CREATE (a5:Accessory {id:'5f94dd2c-6d3b-4f51-82e2-c3009b42250a', name: 'Keyless Entry', price:99.95});

CREATE (a6:Accessory {id:'6b00d785-bdb8-4441-9590-04938eefa481', name: 'Tow Hitch', price:99.95});

CREATE (a7:Accessory {id:'713d1b90-93e4-411e-8a63-6c6de9729641', name: 'Roof Rack', price:99.95});

CREATE (a8:Accessory {id:'7425be25-07cc-4167-b00d-6d1804026c17', name: 'GPS Navigation', price:99.95});

CREATE (a9:Accessory {id:'78ba9e9a-d693-4d71-b330-092928fe7123', name: 'Parking Sensors', price:99.95});

CREATE (a10:Accessory {id:'8466ac46-1926-4969-875c-825f58d8ef64', name: 'Premium Sound System', price:99.95});

CREATE (a11:Accessory {id:'8ac0c1eb-d36f-4a0c-9520-c9ec954f6948', name: 'Rear Spoiler', price:99.95});

CREATE (a12:Accessory {id:'8e637319-526c-4597-ad23-71eae78bde94', name: 'Cruise Control', price:99.95});

CREATE (a13:Accessory {id:'a0f75999-89b1-4120-9423-f6951d13334b', name: 'Fog Lights', price:99.95});

CREATE (a14:Accessory {id:'a191672a-5efa-4ac5-85c2-679c1708a176', name: 'Sunroof', price:99.95});

CREATE (a15:Accessory {id:'b09c572c-25b6-4f70-99f8-9d2817e5c1e5', name: 'Leather Seats', price:99.95});

CREATE (a16:Accessory {id:'c7114d43-1a56-482f-b46b-80878586462a', name: 'Electric Seats', price:99.95});

CREATE (a17:Accessory {id:'dab9106c-cf97-498b-8ed6-f5c02488f584', name: 'Backup Camera', price:99.95});

CREATE (a18:Accessory {id:'e620ec3c-625d-4bde-9b77-f7449b6352d5', name: 'Adaptive Headlights', price:99.95});

CREATE (a19:Accessory {id:'e7858d25-49e7-4ad5-821c-100de2b18918', name: 'Tinted Windows', price:99.95});

CREATE (a20:Accessory {id:'fc8f689e-9615-4cf6-9664-31400db7ebea', name: 'Heated Seats', price:99.95});

// Create the `Insurance` nodes;
CREATE CONSTRAINT FOR (i:Insurance) REQUIRE i.id IS UNIQUE;

CREATE CONSTRAINT FOR (i:Insurance) REQUIRE i.name IS UNIQUE;

// Insert data into the `Insurance` nodes;
CREATE (i1:Insurance {id:'37074fac-26da-4e38-9ae6-acbe755359e5', name: 'Earthquake', price:29.95});

CREATE (i2:Insurance {id:'3e9a0efb-f1a1-4757-b4c3-985fc856b8d5', name: 'Hauntings', price:39.95});

CREATE (i3:Insurance {id:'76b21d38-2103-4464-84f2-c87178e4a30c', name: 'Broken Window', price:19.95});

CREATE (i4:Insurance {id:'8456043d-5fb0-49bf-ac2c-51567a32cc87', name: 'Flat Tire', price:9.95});

CREATE (i5:Insurance {id:'a80a8bed-e1a2-462f-8a77-9483e757c0f2', name: 'Water Damage', price:49.95});

// Create the `Color` nodes;
CREATE CONSTRAINT FOR (c:Color) REQUIRE c.id IS UNIQUE;

CREATE CONSTRAINT FOR (c:Color) REQUIRE c.name IS UNIQUE;

// Insert data into the `Color` nodes;
CREATE (c1:Color {id:'14382aba-6fe6-405d-a5e2-0b8cfd1f9582', name: 'silver', price:299.95, red_value:192, green_value:192, blue_value:192});

CREATE (c2:Color {id:'5e755eb3-0099-4cdd-b064-d8bd95968109', name: 'blue', price:99.95, red_value:0, green_value:0, blue_value:255});

CREATE (c3:Color {id:'74251648-a7b1-492a-ab2a-f2248c58da00', name: 'red', price:199.95, red_value:255, green_value:0, blue_value:0});

CREATE (c4:Color {id:'7bb35b1d-37ff-43c2-988a-cf85c5b6d690', name: 'white', price:399.95, red_value:255, green_value:255, blue_value:255});

CREATE (c5:Color {id:'e2164054-4cb8-49d5-a0da-eca5b36a0b3b', name: 'black', price:0, red_value:0, green_value:0, blue_value:0});

// Create the `Brand` nodes;
CREATE CONSTRAINT FOR (b:Brand) REQUIRE b.id IS UNIQUE;

CREATE CONSTRAINT FOR (b:Brand) REQUIRE b.name IS UNIQUE;

// Insert data into the `Brand` nodes;
CREATE (b1:Brand {id:'83e36635-548d-491a-9e5f-3fafaab02ba0', name: 'Mercedes', logo_url:'https: //keacar.ams3.cdn.digitaloceanspaces.com/Mercedes-logo.png'});
CREATE (b2:Brand {id:'8bb880b8-e336-4039-ad86-2f758539e454', name: 'Ford', logo_url:'https: //keacar.ams3.cdn.digitaloceanspaces.com/Ford-logo.png'});
CREATE (b3:Brand {id:'fadeb491-9cde-4534-b855-b1ada31e2b47', name: 'Skoda', logo_url:'https: //keacar.ams3.cdn.digitaloceanspaces.com/Skoda-logo.png'});
CREATE (b4:Brand {id:'feb2efdb-93ee-4f45-88b1-5e4086c00334', name: 'BMW', logo_url:'https: //keacar.ams3.cdn.digitaloceanspaces.com/bmw-logo.png'});
CREATE (b5:Brand {id:'fff14a06-dc2a-447d-a707-9c03fe00c7a0', name: 'Audi', logo_url:'https: //keacar.ams3.cdn.digitaloceanspaces.com/Audi-logo.png'});

// Create the `Model` nodes;
CREATE CONSTRAINT FOR (m:Model) REQUIRE m.id IS UNIQUE;

// Create the `Model` node and relationships to `Brand` and `Color` nodes;
CREATE (m1:Model {id:'053b1148-1bb6-4445-85b1-9f71db5b7143', name: 'A4', price:10000.95, image_url:'https: //keacar.ams3.cdn.digitaloceanspaces.com/a4.png'})
WITH m1
MATCH (b5:Brand {id:'fff14a06-dc2a-447d-a707-9c03fe00c7a0'})
CREATE (m1)- [:BELONGS_TO] - >(b5)
WITH m1
MATCH (c3:Color {id:'74251648-a7b1-492a-ab2a-f2248c58da00'}), (c4:Color {id:'7bb35b1d-37ff-43c2-988a-cf85c5b6d690'}), (c5:Color {id:'e2164054-4cb8-49d5-a0da-eca5b36a0b3b'})
CREATE (m1)- [:HAS_COLOR] - >(c3), (m1)- [:HAS_COLOR] - >(c4), (m1)- [:HAS_COLOR] - >(c5);

CREATE (m2:Model {id:'1de1b6d3-da97-440b-ba3b-1c865e1de47f', name: 'Mustang', price:10990.95, image_url:'https: //keacar.ams3.cdn.digitaloceanspaces.com/mustang.png'})
WITH m2
MATCH (b2:Brand {id:'8bb880b8-e336-4039-ad86-2f758539e454'})
CREATE (m2)- [:BELONGS_TO] - >(b2)
WITH m2
MATCH (c4:Color {id:'7bb35b1d-37ff-43c2-988a-cf85c5b6d690'}), (c5:Color {id:'e2164054-4cb8-49d5-a0da-eca5b36a0b3b'})
CREATE (m2)- [:HAS_COLOR] - >(c4), (m2)- [:HAS_COLOR] - >(c5);

CREATE (m3:Model {id:'37c7b96c-4142-4890-a1c0-cdb4ff95606e', name: 'Explorer', price:10990.95, image_url:'https: //keacar.ams3.cdn.digitaloceanspaces.com/explorer.png'})
WITH m3
MATCH (b2:Brand {id:'8bb880b8-e336-4039-ad86-2f758539e454'})
CREATE (m3)- [:BELONGS_TO] - >(b2)
WITH m3
MATCH (c3:Color {id:'74251648-a7b1-492a-ab2a-f2248c58da00'}), (c4:Color {id:'7bb35b1d-37ff-43c2-988a-cf85c5b6d690'}), (c5:Color {id:'e2164054-4cb8-49d5-a0da-eca5b36a0b3b'})
CREATE (m3)- [:HAS_COLOR] - >(c3), (m3)- [:HAS_COLOR] - >(c4), (m3)- [:HAS_COLOR] - >(c5);

CREATE (m4:Model {id:'41e96e21-7e57-45aa-8462-35fe83565866', name: 'Kodiaq', price:19999.95, image_url:'https: //keacar.ams3.cdn.digitaloceanspaces.com/kodiaq.png'})
WITH m4
MATCH (b3:Brand {id:'fadeb491-9cde-4534-b855-b1ada31e2b47'})
CREATE (m4)- [:BELONGS_TO] - >(b3)
WITH m4
MATCH (c4:Color {id:'7bb35b1d-37ff-43c2-988a-cf85c5b6d690'}), (c5:Color {id:'e2164054-4cb8-49d5-a0da-eca5b36a0b3b'})
CREATE (m4)- [:HAS_COLOR] - >(c4), (m4)- [:HAS_COLOR] - >(c5);

CREATE (m5:Model {id:'44bb8524-0b5d-4451-9d20-9bdafe6f8808', name: 'Yeti', price:19999.95, image_url:'https: //keacar.ams3.cdn.digitaloceanspaces.com/yeti.png'})
WITH m5
MATCH (b3:Brand {id:'fadeb491-9cde-4534-b855-b1ada31e2b47'})
CREATE (m5)- [:BELONGS_TO] - >(b3)
WITH m5
MATCH (c2:Color {id:'5e755eb3-0099-4cdd-b064-d8bd95968109'}), (c4:Color {id:'7bb35b1d-37ff-43c2-988a-cf85c5b6d690'}), (c5:Color {id:'e2164054-4cb8-49d5-a0da-eca5b36a0b3b'})
CREATE (m5)- [:HAS_COLOR] - >(c2), (m5)- [:HAS_COLOR] - >(c4), (m5)- [:HAS_COLOR] - >(c5);

CREATE (m6:Model {id:'45395bf5-431b-4643-bce0-c8a3bdba3a63', name: 'A6', price:10000.95, image_url:'https: //keacar.ams3.cdn.digitaloceanspaces.com/a6.png'})
WITH m6
MATCH (b5:Brand {id:'fff14a06-dc2a-447d-a707-9c03fe00c7a0'})
CREATE (m6)- [:BELONGS_TO] - >(b5)
WITH m6
MATCH (c2:Color {id:'5e755eb3-0099-4cdd-b064-d8bd95968109'}), (c4:Color {id:'7bb35b1d-37ff-43c2-988a-cf85c5b6d690'}), (c5:Color {id:'e2164054-4cb8-49d5-a0da-eca5b36a0b3b'})
CREATE (m6)- [:HAS_COLOR] - >(c2), (m6)- [:HAS_COLOR] - >(c4), (m6)- [:HAS_COLOR] - >(c5);

CREATE (m7:Model {id:'460200f8-4e2d-47ad-b65e-e5e333c7ed4b', name: 'Octavia', price:19999.95, image_url:'https: //keacar.ams3.cdn.digitaloceanspaces.com/octavia.png'})
WITH m7
MATCH (b3:Brand {id:'fadeb491-9cde-4534-b855-b1ada31e2b47'})
CREATE (m7)- [:BELONGS_TO] - >(b3)
WITH m7
MATCH (c2:Color {id:'5e755eb3-0099-4cdd-b064-d8bd95968109'}), (c4:Color {id:'7bb35b1d-37ff-43c2-988a-cf85c5b6d690'}), (c5:Color {id:'e2164054-4cb8-49d5-a0da-eca5b36a0b3b'})
CREATE (m7)- [:HAS_COLOR] - >(c2), (m7)- [:HAS_COLOR] - >(c4), (m7)- [:HAS_COLOR] - >(c5);

CREATE (m8:Model {id:'48daf651-f67d-465e-8e14-fc02997c8cf9', name: 'Rapid', price:19999.95, image_url:'https: //keacar.ams3.cdn.digitaloceanspaces.com/rapid.png'})
WITH m8
MATCH (b3:Brand {id:'fadeb491-9cde-4534-b855-b1ada31e2b47'})
CREATE (m8)- [:BELONGS_TO] - >(b3)
WITH m8
MATCH (c3:Color {id:'74251648-a7b1-492a-ab2a-f2248c58da00'}), (c4:Color {id:'7bb35b1d-37ff-43c2-988a-cf85c5b6d690'}), (c5:Color {id:'e2164054-4cb8-49d5-a0da-eca5b36a0b3b'})
CREATE (m8)- [:HAS_COLOR] - >(c3), (m8)- [:HAS_COLOR] - >(c4), (m8)- [:HAS_COLOR] - >(c5);

CREATE (m9:Model {id:'4bcd231c-8d2c-4c9e-a850-12f5e74edef5', name: 'Series 3', price:10090.95, image_url:'https: //keacar.ams3.cdn.digitaloceanspaces.com/Series_3.png'})
WITH m9
MATCH (b4:Brand {id:'feb2efdb-93ee-4f45-88b1-5e4086c00334'})
CREATE (m9)- [:BELONGS_TO] - >(b4)
WITH m9
MATCH (c3:Color {id:'74251648-a7b1-492a-ab2a-f2248c58da00'}), (c4:Color {id:'7bb35b1d-37ff-43c2-988a-cf85c5b6d690'}), (c5:Color {id:'e2164054-4cb8-49d5-a0da-eca5b36a0b3b'})
CREATE (m9)- [:HAS_COLOR] - >(c3), (m9)- [:HAS_COLOR] - >(c4), (m9)- [:HAS_COLOR] - >(c5);

CREATE (m10:Model {id:'552bac65-bd5e-4dcd-8f50-cb5b1816d8b3', name: 'S-Class', price:19990.95, image_url:'https: //keacar.ams3.cdn.digitaloceanspaces.com/s-class.png'})
WITH m10
MATCH (b1:Brand {id:'83e36635-548d-491a-9e5f-3fafaab02ba0'})
CREATE (m10)- [:BELONGS_TO] - >(b1)
WITH m10
MATCH (c3:Color {id:'74251648-a7b1-492a-ab2a-f2248c58da00'}), (c4:Color {id:'7bb35b1d-37ff-43c2-988a-cf85c5b6d690'}), (c5:Color {id:'e2164054-4cb8-49d5-a0da-eca5b36a0b3b'})
CREATE (m10)- [:HAS_COLOR] - >(c3), (m10)- [:HAS_COLOR] - >(c4), (m10)- [:HAS_COLOR] - >(c5);

CREATE (m11:Model {id:'65e666f1-ea52-4982-a1e7-0f164891fee2', name: 'Citigo', price:19999.95, image_url:'https: //keacar.ams3.cdn.digitaloceanspaces.com/citigo.png'})
WITH m11
MATCH (b3:Brand {id:'fadeb491-9cde-4534-b855-b1ada31e2b47'})
CREATE (m11)- [:BELONGS_TO] - >(b3)
WITH m11
MATCH (c1:Color {id:'14382aba-6fe6-405d-a5e2-0b8cfd1f9582'}), (c2:Color {id:'5e755eb3-0099-4cdd-b064-d8bd95968109'}), (c3:Color {id:'74251648-a7b1-492a-ab2a-f2248c58da00'}), (c4:Color {id:'7bb35b1d-37ff-43c2-988a-cf85c5b6d690'}), (c5:Color {id:'e2164054-4cb8-49d5-a0da-eca5b36a0b3b'})
CREATE (m11)- [:HAS_COLOR] - >(c1), (m11)- [:HAS_COLOR] - >(c2), (m11)- [:HAS_COLOR] - >(c3), (m11)- [:HAS_COLOR] - >(c4), (m11)- [:HAS_COLOR] - >(c5);

CREATE (m12:Model {id:'77dc2097-6d49-4fc9-bd1a-b0221af35dc6', name: 'Fiesta', price:10990.95, image_url:'https: //keacar.ams3.cdn.digitaloceanspaces.com/fiesta.png'})
WITH m12
MATCH (b2:Brand {id:'8bb880b8-e336-4039-ad86-2f758539e454'})
CREATE (m12)- [:BELONGS_TO] - >(b2)
WITH m12
MATCH (c1:Color {id:'14382aba-6fe6-405d-a5e2-0b8cfd1f9582'}), (c2:Color {id:'5e755eb3-0099-4cdd-b064-d8bd95968109'}), (c3:Color {id:'74251648-a7b1-492a-ab2a-f2248c58da00'}), (c4:Color {id:'7bb35b1d-37ff-43c2-988a-cf85c5b6d690'}), (c5:Color {id:'e2164054-4cb8-49d5-a0da-eca5b36a0b3b'})
CREATE (m12)- [:HAS_COLOR] - >(c1), (m12)- [:HAS_COLOR] - >(c2), (m12)- [:HAS_COLOR] - >(c3), (m12)- [:HAS_COLOR] - >(c4), (m12)- [:HAS_COLOR] - >(c5);

CREATE (m13:Model {id:'78b4d92e-fa14-4081-9e77-71cd2bad502c', name: 'i8', price:10090.95, image_url:'https: //keacar.ams3.cdn.digitaloceanspaces.com/i8.png'})
WITH m13
MATCH (b4:Brand {id:'feb2efdb-93ee-4f45-88b1-5e4086c00334'})
CREATE (m13)- [:BELONGS_TO] - >(b4)
WITH m13
MATCH (c4:Color {id:'7bb35b1d-37ff-43c2-988a-cf85c5b6d690'}), (c5:Color {id:'e2164054-4cb8-49d5-a0da-eca5b36a0b3b'})
CREATE (m13)- [:HAS_COLOR] - >(c4), (m13)- [:HAS_COLOR] - >(c5);

CREATE (m14:Model {id:'866a22d1-0ea1-458d-9a12-e5206d6ed8fc', name: 'A1', price:10000.95, image_url:'https: //keacar.ams3.cdn.digitaloceanspaces.com/a1.png'})
WITH m14
MATCH (b5:Brand {id:'fff14a06-dc2a-447d-a707-9c03fe00c7a0'})
CREATE (m14)- [:BELONGS_TO] - >(b5)
WITH m14
MATCH (c1:Color {id:'14382aba-6fe6-405d-a5e2-0b8cfd1f9582'}), (c2:Color {id:'5e755eb3-0099-4cdd-b064-d8bd95968109'}), (c3:Color {id:'74251648-a7b1-492a-ab2a-f2248c58da00'}), (c4:Color {id:'7bb35b1d-37ff-43c2-988a-cf85c5b6d690'}), (c5:Color {id:'e2164054-4cb8-49d5-a0da-eca5b36a0b3b'})
CREATE (m14)- [:HAS_COLOR] - >(c1), (m14)- [:HAS_COLOR] - >(c2), (m14)- [:HAS_COLOR] - >(c3), (m14)- [:HAS_COLOR] - >(c4), (m14)- [:HAS_COLOR] - >(c5);

CREATE (m15:Model {id:'8ce88a9b-3275-4fea-86ac-2c15b92a6727', name: 'Fusion', price:10990.95, image_url:'https: //keacar.ams3.cdn.digitaloceanspaces.com/fusion.png'})
WITH m15
MATCH (b2:Brand {id:'8bb880b8-e336-4039-ad86-2f758539e454'})
CREATE (m15)- [:BELONGS_TO] - >(b2)
WITH m15
MATCH (c2:Color {id:'5e755eb3-0099-4cdd-b064-d8bd95968109'}), (c4:Color {id:'7bb35b1d-37ff-43c2-988a-cf85c5b6d690'}), (c5:Color {id:'e2164054-4cb8-49d5-a0da-eca5b36a0b3b'})
CREATE (m15)- [:HAS_COLOR] - >(c2), (m15)- [:HAS_COLOR] - >(c4), (m15)- [:HAS_COLOR] - >(c5);

CREATE (m16:Model {id:'8f599259-538f-4b3e-bc3b-50daa8f5fd96', name: 'Series 2', price:10090.95, image_url:'https: //keacar.ams3.cdn.digitaloceanspaces.com/Series_2.png'})
WITH m16
MATCH (b4:Brand {id:'feb2efdb-93ee-4f45-88b1-5e4086c00334'})
CREATE (m16)- [:BELONGS_TO] - >(b4)
WITH m16
MATCH (c2:Color {id:'5e755eb3-0099-4cdd-b064-d8bd95968109'}), (c4:Color {id:'7bb35b1d-37ff-43c2-988a-cf85c5b6d690'}), (c5:Color {id:'e2164054-4cb8-49d5-a0da-eca5b36a0b3b'})
CREATE (m16)- [:HAS_COLOR] - >(c2), (m16)- [:HAS_COLOR] - >(c4), (m16)- [:HAS_COLOR] - >(c5);

CREATE (m17:Model {id:'996f735f-b06d-426e-ac5b-e90827d92707', name: 'A3', price:10000.95, image_url:'https: //keacar.ams3.cdn.digitaloceanspaces.com/a3.png'})
WITH m17
MATCH (b5:Brand {id:'fff14a06-dc2a-447d-a707-9c03fe00c7a0'})
CREATE (m17)- [:BELONGS_TO] - >(b5)
WITH m17
MATCH (c2:Color {id:'5e755eb3-0099-4cdd-b064-d8bd95968109'}), (c4:Color {id:'7bb35b1d-37ff-43c2-988a-cf85c5b6d690'}), (c5:Color {id:'e2164054-4cb8-49d5-a0da-eca5b36a0b3b'})
CREATE (m17)- [:HAS_COLOR] - >(c2), (m17)- [:HAS_COLOR] - >(c4), (m17)- [:HAS_COLOR] - >(c5);

CREATE (m18:Model {id:'ad88f9d8-db4e-4527-b2c7-8abbb475467b', name: 'X6', price:10090.95, image_url:'https: //keacar.ams3.cdn.digitaloceanspaces.com/X6.png'})
WITH m18
MATCH (b4:Brand {id:'feb2efdb-93ee-4f45-88b1-5e4086c00334'})
CREATE (m18)- [:BELONGS_TO] - >(b4)
WITH m18
MATCH (c2:Color {id:'5e755eb3-0099-4cdd-b064-d8bd95968109'}), (c4:Color {id:'7bb35b1d-37ff-43c2-988a-cf85c5b6d690'}), (c5:Color {id:'e2164054-4cb8-49d5-a0da-eca5b36a0b3b'})
CREATE (m18)- [:HAS_COLOR] - >(c2), (m18)- [:HAS_COLOR] - >(c4), (m18)- [:HAS_COLOR] - >(c5);

CREATE (m19:Model {id:'be927e18-6bd4-491c-b031-73a569afa00b', name: 'A-Class', price:19990.95, image_url:'https: //keacar.ams3.cdn.digitaloceanspaces.com/a-class.png'})
WITH m19
MATCH (b1:Brand {id:'83e36635-548d-491a-9e5f-3fafaab02ba0'})
CREATE (m19)- [:BELONGS_TO] - >(b1)
WITH m19
MATCH (c1:Color {id:'14382aba-6fe6-405d-a5e2-0b8cfd1f9582'}), (c2:Color {id:'5e755eb3-0099-4cdd-b064-d8bd95968109'}), (c3:Color {id:'74251648-a7b1-492a-ab2a-f2248c58da00'}), (c4:Color {id:'7bb35b1d-37ff-43c2-988a-cf85c5b6d690'}), (c5:Color {id:'e2164054-4cb8-49d5-a0da-eca5b36a0b3b'})
CREATE (m19)- [:HAS_COLOR] - >(c1), (m19)- [:HAS_COLOR] - >(c2), (m19)- [:HAS_COLOR] - >(c3), (m19)- [:HAS_COLOR] - >(c4), (m19)- [:HAS_COLOR] - >(c5);

CREATE (m20:Model {id:'d4bd413c-00d8-45ce-be0e-1d1333ac5e75', name: 'R8', price:10000.95, image_url:'https: //keacar.ams3.cdn.digitaloceanspaces.com/r8.png'})
WITH m20
MATCH (b5:Brand {id:'fff14a06-dc2a-447d-a707-9c03fe00c7a0'})
CREATE (m20)- [:BELONGS_TO] - >(b5)
WITH m20
MATCH (c4:Color {id:'7bb35b1d-37ff-43c2-988a-cf85c5b6d690'}), (c5:Color {id:'e2164054-4cb8-49d5-a0da-eca5b36a0b3b'})
CREATE (m20)- [:HAS_COLOR] - >(c4), (m20)- [:HAS_COLOR] - >(c5);

CREATE (m21:Model {id:'d96e68ef-4f6f-4623-9c7b-7c4df75ff032', name: 'C-Class', price:19990.95, image_url:'https: //keacar.ams3.cdn.digitaloceanspaces.com/c-class.png'})
WITH m21
MATCH (b1:Brand {id:'83e36635-548d-491a-9e5f-3fafaab02ba0'})
CREATE (m21)- [:BELONGS_TO] - >(b1)
WITH m21
MATCH (c2:Color {id:'5e755eb3-0099-4cdd-b064-d8bd95968109'}), (c4:Color {id:'7bb35b1d-37ff-43c2-988a-cf85c5b6d690'}), (c5:Color {id:'e2164054-4cb8-49d5-a0da-eca5b36a0b3b'})
CREATE (m21)- [:HAS_COLOR] - >(c2), (m21)- [:HAS_COLOR] - >(c4), (m21)- [:HAS_COLOR] - >(c5);

CREATE (m22:Model {id:'deec07da-2049-484f-adc8-2fea95708964', name: 'G-Class', price:19990.95, image_url:'https: //keacar.ams3.cdn.digitaloceanspaces.com/g-class.png'})
WITH m22
MATCH (b1:Brand {id:'83e36635-548d-491a-9e5f-3fafaab02ba0'})
CREATE (m22)- [:BELONGS_TO] - >(b1)
WITH m22
MATCH (c2:Color {id:'5e755eb3-0099-4cdd-b064-d8bd95968109'}), (c4:Color {id:'7bb35b1d-37ff-43c2-988a-cf85c5b6d690'}), (c5:Color {id:'e2164054-4cb8-49d5-a0da-eca5b36a0b3b'})
CREATE (m22)- [:HAS_COLOR] - >(c2), (m22)- [:HAS_COLOR] - >(c4), (m22)- [:HAS_COLOR] - >(c5);

CREATE (m23:Model {id:'ed996516-a141-4f4e-8991-3edeaba81c14', name: 'Series 1', price:10090.95, image_url:'https: //keacar.ams3.cdn.digitaloceanspaces.com/Series_1.png'})
WITH m23
MATCH (b4:Brand {id:'feb2efdb-93ee-4f45-88b1-5e4086c00334'})
CREATE (m23)- [:BELONGS_TO] - >(b4)
WITH m23
MATCH (c1:Color {id:'14382aba-6fe6-405d-a5e2-0b8cfd1f9582'}), (c2:Color {id:'5e755eb3-0099-4cdd-b064-d8bd95968109'}), (c3:Color {id:'74251648-a7b1-492a-ab2a-f2248c58da00'}), (c4:Color {id:'7bb35b1d-37ff-43c2-988a-cf85c5b6d690'}), (c5:Color {id:'e2164054-4cb8-49d5-a0da-eca5b36a0b3b'})
CREATE (m23)- [:HAS_COLOR] - >(c1), (m23)- [:HAS_COLOR] - >(c2), (m23)- [:HAS_COLOR] - >(c3), (m23)- [:HAS_COLOR] - >(c4), (m23)- [:HAS_COLOR] - >(c5);

CREATE (m24:Model {id:'fa967f9a-598b-4240-ac49-70ad190795af', name: 'Pickup', price:10990.95, image_url:'https: //keacar.ams3.cdn.digitaloceanspaces.com/pickup.png'})
WITH m24
MATCH (b2:Brand {id:'8bb880b8-e336-4039-ad86-2f758539e454'})
CREATE (m24)- [:BELONGS_TO] - >(b2)
WITH m24
MATCH (c2:Color {id:'5e755eb3-0099-4cdd-b064-d8bd95968109'}), (c4:Color {id:'7bb35b1d-37ff-43c2-988a-cf85c5b6d690'}), (c5:Color {id:'e2164054-4cb8-49d5-a0da-eca5b36a0b3b'})
CREATE (m24)- [:HAS_COLOR] - >(c2), (m24)- [:HAS_COLOR] - >(c4), (m24)- [:HAS_COLOR] - >(c5);

CREATE (m25:Model {id:'fb98b121-6648-4a82-b05c-6793b419c1c9', name: 'AmgGT', price:19990.95, image_url:'https: //keacar.ams3.cdn.digitaloceanspaces.com/amgGT.png'})
WITH m25
MATCH (b1:Brand {id:'83e36635-548d-491a-9e5f-3fafaab02ba0'})
CREATE (m25)- [:BELONGS_TO] - >(b1)
WITH m25
MATCH (c4:Color {id:'7bb35b1d-37ff-43c2-988a-cf85c5b6d690'}), (c5:Color {id:'e2164054-4cb8-49d5-a0da-eca5b36a0b3b'})
CREATE (m25)- [:HAS_COLOR] - >(c4), (m25)- [:HAS_COLOR] - >(c5);

// Create the `Car` nodes;
CREATE CONSTRAINT FOR (car:Car) REQUIRE car.id IS UNIQUE;

// Create the 1st `Car` node and relationships to `Model`, `Color`, `Customer`, `SalesPerson`, `Accessory`, and `Insurance` nodes;
CREATE (car1:Car {id:'0be86135-c58f-43b6-a369-a3c5445b9948', purchase_deadline: date('2024-12-07'), total_price:10530.8})
WITH car1
MATCH (m20:Model {id:'d4bd413c-00d8-45ce-be0e-1d1333ac5e75'}), (c4:Color {id:'7bb35b1d-37ff-43c2-988a-cf85c5b6d690'}), (cus4:Customer {id:'f159bdaf-bc83-46c3-8a3f-f6b5c93ebbdc'}), (sp2:SalesPerson {id:'f9097a97-eca4-49b6-85a0-08423789c320'}), (a19:Accessory {id:'e7858d25-49e7-4ad5-821c-100de2b18918'}), (i1:Insurance {id:'37074fac-26da-4e38-9ae6-acbe755359e5'})
CREATE (car1)- [:HAS_MODEL] - >(m20), (car1)- [:HAS_COLOR] - >(c4), (car1)- [:OWNED_BY] - >(cus4), (car1)- [:SOLD_BY] - >(sp2), (car1)- [:HAS_ACCESSORY] - >(a19), (car1)- [:HAS_INSURANCE] - >(i1);

// Create the 2nd `Car` node and relationships to `Model`, `Color`, `Customer`, `SalesPerson`, `Accessory`, and `Insurance` nodes;
CREATE (car2:Car {id:'a1b1e305-1a89-4b06-86d1-21ac1fa3c8a6', purchase_deadline: date('2024-12-04'), total_price:10530.8})
WITH car2
MATCH (m20:Model {id:'d4bd413c-00d8-45ce-be0e-1d1333ac5e75'}), (c4:Color {id:'7bb35b1d-37ff-43c2-988a-cf85c5b6d690'}), (cus4:Customer {id:'f159bdaf-bc83-46c3-8a3f-f6b5c93ebbdc'}), (sp1:SalesPerson {id:'d096d2e1-f06a-4555-9cd1-afa9f930f10c'}), (a19:Accessory {id:'e7858d25-49e7-4ad5-821c-100de2b18918'}), (i1:Insurance {id:'37074fac-26da-4e38-9ae6-acbe755359e5'})
CREATE (car2)- [:HAS_MODEL] - >(m20), (car2)- [:HAS_COLOR] - >(c4), (car2)- [:OWNED_BY] - >(cus4), (car2)- [:SOLD_BY] - >(sp1), (car2)- [:HAS_ACCESSORY] - >(a19), (car2)- [:HAS_INSURANCE] - >(i1);

// Create the 3rd `Car` node and relationships to `Model`, `Color`, `Customer`, `SalesPerson`, `Accessory`, and `Insurance` nodes;
CREATE (car3:Car {id:'a5503fbb-c388-4789-a10c-d7ae7bdf7408', purchase_deadline: date('2024-12-05'), total_price:10530.8})
WITH car3
MATCH (m20:Model {id:'d4bd413c-00d8-45ce-be0e-1d1333ac5e75'}), (c4:Color {id:'7bb35b1d-37ff-43c2-988a-cf85c5b6d690'}), (cus4:Customer {id:'f159bdaf-bc83-46c3-8a3f-f6b5c93ebbdc'}), (sp2:SalesPerson {id:'f9097a97-eca4-49b6-85a0-08423789c320'}), (a19:Accessory {id:'e7858d25-49e7-4ad5-821c-100de2b18918'}), (i1:Insurance {id:'37074fac-26da-4e38-9ae6-acbe755359e5'})
CREATE (car3)- [:HAS_MODEL] - >(m20), (car3)- [:HAS_COLOR] - >(c4), (car3)- [:OWNED_BY] - >(cus4), (car3)- [:SOLD_BY] - >(sp2), (car3)- [:HAS_ACCESSORY] - >(a19), (car3)- [:HAS_INSURANCE] - >(i1);

// Create the 4th `Car` node and relationships to `Model`, `Color`, `Customer`, `SalesPerson`, `Accessory`, and `Insurance` nodes;
CREATE (car4:Car {id:'d4c7f1f8-4451-43bc-a827-63216a2ddece', purchase_deadline: date('2024-12-04'), total_price:10530.8})
WITH car4
MATCH (m20:Model {id:'d4bd413c-00d8-45ce-be0e-1d1333ac5e75'}), (c4:Color {id:'7bb35b1d-37ff-43c2-988a-cf85c5b6d690'}), (cus1:Customer {id:'0ac1d668-55aa-46a1-898a-8fa61457facb'}), (sp2:SalesPerson {id:'f9097a97-eca4-49b6-85a0-08423789c320'}), (a19:Accessory {id:'e7858d25-49e7-4ad5-821c-100de2b18918'}), (i1:Insurance {id:'37074fac-26da-4e38-9ae6-acbe755359e5'})
CREATE (car4)- [:HAS_MODEL] - >(m20), (car4)- [:HAS_COLOR] - >(c4), (car4)- [:OWNED_BY] - >(cus1), (car4)- [:SOLD_BY] - >(sp2), (car4)- [:HAS_ACCESSORY] - >(a19), (car4)- [:HAS_INSURANCE] - >(i1);

// Create the 1st `Purchase` node and relationship to `Car` node;
CREATE CONSTRAINT FOR (p:Purchase) REQUIRE p.id IS UNIQUE;

CREATE (p1:Purchase {
id:'bdfca7c4-e0ad-4618-8766-9bb355371c81',
date_of_purchase: date('2024-11-04')
})
WITH p1
MATCH (car4:Car {id:'d4c7f1f8-4451-43bc-a827-63216a2ddece'})
CREATE (p1)- [:MADE_FOR] - >(car4);
