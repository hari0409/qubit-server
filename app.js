// Basic Imports
const express = require("express");
const colors = require("colors");
const createError = require("http-errors");
const morgan = require("morgan");
const helmet = require("helmet");
const cors = require("cors");
var multipart = require("connect-multiparty");
require("dotenv").config();


// App Initialization
const app = express();

// Middlewares
app.use(cors());
app.use(helmet());
app.use(morgan("dev"));
app.use(express.json());
app.use(express.urlencoded({ extended: true }));
app.use(multipart());

//Health check for server
app.get("/health", async (req, res, next) => {
  res.status(200).json({ message: "Awesome it works 🐻" });
});

// Mounting routers
app.use("/api/obfuscator", require("./src/routes/obfuscator"));
app.use("/api/sec", require("./src/routes/sec"));
app.use("/api/mvt", require("./src/routes/mvt"));
app.use("/api/mem", require("./src/routes/mem"));


app.use((req, res, next) => {
  next(createError.NotFound());
});

app.use((err, req, res, next) => {
  res.status(err.status || 500);
  res.send({
    status: err.status || 500,
    message: err.message,
  });
});

const server = app.listen(process.env.PORT || 3000, () => {
  if (process.env.NODE_ENV === "production")
    console.log(`🚀 @ localhost:5000`.green.bold);
  else console.log(`🚀 @ localhost:5000`.green.bold);
});

// Handle unhandled promise rejections
process.on("unhandledRejection", (err, promise) => {
  console.log(`Error: ${err.message}`.red);
  server.close(() => process.exit(1));
});
