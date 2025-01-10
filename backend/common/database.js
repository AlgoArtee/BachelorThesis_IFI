const { Sequelize } = require("sequelize");

const sequelize = new Sequelize({
  dialect: "sqlite",
  storage: "./database.sqlite", // The database file will be created in the project root
});

module.exports = sequelize;
