const express = require("express");
const dotenv = require("dotenv");
const cors = require("cors");

// Load environment variables
dotenv.config();

const app = express();
app.use(express.json());
app.use(cors());

const PORT = process.env.PORT || 5000;

// Sequelize and SQLite Integration
const sequelize = require("./common/database");
const User = require("./common/models/User");

// Sync database
sequelize
  .sync({ force: true }) // Use { force: true } only during development to reset the database
  .then(() => {
    console.log("Database synced successfully.");
  })
  .catch((error) => {
    console.error("Error syncing database:", error);
  });

// Example test endpoint
app.get("/api/test", (req, res) => {
  res.json({ message: "API is working!" });
});

// Authentication routes
const authRoutes = require("./routes/auth");
app.use("/api/auth", authRoutes);

// Start the server
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});


