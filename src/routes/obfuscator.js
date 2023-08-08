const { exec } = require("child_process");
const { upload } = require("../controllers/obfuscator");
const path = require("path")
const router = require("express").Router();
const colors = require("colors")

const scriptPath = path("../scripts/main.py")


//Create a post
router.post("/upload", async (req, res, next) => {
    try {
        const { type, path } = req.body;
        exec(`python3 ${scriptPath} ${path}`, (err, stdout, stderr) => {
            if (err) {
                console.log(`${err}`.red);
            }
            else {
                console.log(`${stdout}`.green);
            }
        })
        res.status(200).json({ status: "success" });
    } catch (error) {
        next(error);
    }
});

module.exports = router;
