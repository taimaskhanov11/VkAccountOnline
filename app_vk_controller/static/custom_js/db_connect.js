
var pg = require('pg');
var conString = "postgres://postgres:postgres@localhost:5432/django_db";

var client = new pg.Client(conString);
client.connect();
var query = client.query("SELECT * FROM app_vk_controller_message");
console.log(query)