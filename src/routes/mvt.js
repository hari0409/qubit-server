const router = require("express").Router()
const { exec } = require('child_process');
const path = require("path");

const bashScriptPath = path.join("src/scripts/mvt.bash")


router.get("/mvt", async (req, res, next) => {
    console.log("Executing MVT Analysis");
    exec(`bash ${bashScriptPath}`, (error, stdout, stderr) => {
        if (error) {
            console.error(`Error: ${error.message}`);
            res.status(500).json({ status: "failure", error: 'Error executing script' });
            return
        }
        if (stderr) {
            console.error(`Stderr: ${stderr}`);
        }
        console.log(`Stdout: ${stdout}`);
        res.status(200).json({ status: "success" });
    });

})

module.exports = router