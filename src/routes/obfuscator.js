const { exec } = require("child_process");
const { upload } = require("../controllers/obfuscator");
const path = require("path")
const router = require("express").Router();
const colors = require("colors");

const scriptPath = path.join("src/scripts/main.py")


function imgEncode(imgPath) {
    console.log("encoding image");
    return new Promise((resolve, reject) => {
        console.log(`python ${scriptPath} ${imgPath}`);
        exec(`python ${scriptPath} ${imgPath}`, (error, stdout, stderr) => {
            resolve(stdout);
        });
    });
}

function textEncode(textPath, imgPath) {
    console.log("encoding text");
    return new Promise((resolve, reject) => {
        exec(`python ${scriptPath} ${imgPath} ${textPath}`, (error, stdout, stderr) => {
            resolve(stdout);
        });
    });
}

//Create img
router.post("/uploadimg", async (req, res, next) => {
    try {
        const { imgPath } = req.body;
        console.log(req.body);
        imgEncode(imgPath).then((out) => {
            console.log(out);
            res.status(200).json({
                status: "success",
                path: out
            })
        }).catch((err) => {
            res.status(401).json({
                status: "failure",
                msg: "failed conversion"
            })
        })
    } catch (error) {
        next(error);
    }
});

//Create text
router.post("/uploadtext", async (req, res, next) => {
    try {
        const { textPath, imgPath } = req.body;
        console.log(req.body);
        textEncode(textPath, imgPath).then((out) => {
            res.status(200).json({
                status: "success",
                path: out
            })
        }).catch((err) => {
            res.status(401).json({
                status: "failure",
                msg: "failed conversion"
            })
        })
    } catch (error) {
        next(error);
    }
});


module.exports = router;
