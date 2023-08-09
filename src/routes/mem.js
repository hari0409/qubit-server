const router = require("express").Router()
const { exec } = require("child_process");
const path = require("path")
const fs = require("fs")

const bashPath = path.join("src/scripts/mem.bash")

router.post("/mem", async (req, res, next) => {
    const { filePath } = req.body;
    const dir = path.dirname(filePath)
    const name = path.basename(filePath)
    exec(`bash ${bashPath} ${dir} ${name}`, (error, stdout, stderr) => {
        if (error) {
            console.error(`Error: ${error.message}`);
            res.status(500).json({ status: "failure", error: 'Error executing script' });
            return
        }
        if (stderr) {
            console.error(`Stderr: ${stderr}`);
        }
        res.status(200).json({
            status: "success"
        })
    });
})

module.exports = router