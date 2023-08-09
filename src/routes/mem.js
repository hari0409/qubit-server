const router = require("express").Router()
const { exec } = require("child_process");
const path = require("path")
const fs = require("fs")

const bashPath = path.join("src/scripts/mem.bash")
const datapath="/home/hari/Downloads/vol_analysis.txt"

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
        fs.readFile(datapath, "utf-8", (err, data) => {
            if (err) {
                console.log(err.message);
                return
            }
            console.log(data);
            res.status(200).json({
                msg: data,
                status: "success"
            })
        })
    });
})

module.exports = router