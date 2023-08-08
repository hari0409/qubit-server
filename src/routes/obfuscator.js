const { upload } = require("../controllers/obfuscator");

const router = require("express").Router();

//Create a post
router.post("/upload", async (req, res, next) => {
    try {
        const { type, path } = req.body;
        console.log(type,path);
        res.status(200).json({ status: "success" });
    } catch (error) {
        next(error);
    }
});

module.exports = router;
