const express = require("express");
const dotenv = require("dotenv");

dotenv.config({ path: `.env` });

const SERVER_PORT = process.env.SERVER_PORT;

const app = express();

app.use((error, request, response, next) => {
  console.error(error);
  response.status(500).send("Server Error");
});

app.get("./views/templates/index.html");

app.listen(SERVER_PORT, (error) => {
  if (error) {
    throw error;
  }
  console.log(`App listening on port ${SERVER_PORT}`);
});
