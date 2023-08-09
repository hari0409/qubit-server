const { exec } = require("child_process")
const { getAlarms } = require("../controllers/ids")
const path = require("path")
const router = require("express").Router()
const fs = require('fs');
const csv = require('csv-parser');

const atopPath = path.join("src/scripts/atop.bash")
const datapath = "/home/hari/Downloads/proc.txt"

const outPath = path.join("src/sniffer/output.csv")
const countPath = path.join("src/scripts/data")

function countRowsInCSV(filePath) {
    let rowCount = 0;

    return new Promise((resolve, reject) => {
        fs.createReadStream(filePath)
            .pipe(csv())
            .on('data', () => rowCount++)
            .on('end', () => resolve(rowCount))
            .on('error', reject);
    });
}

function countFilesInDirectory(directoryPath) {
    try {
        const files = fs.readdirSync(directoryPath);
        const fileCount = files.filter(file => fs.statSync(path.join(directoryPath, file)).isFile()).length;
        return fileCount;
    } catch (error) {
        console.error(`Error: ${error.message}`);
        return 0;
    }
}


router.get("/alarms", async (req, res, next) => {
    var countCSV = countRowsInCSV(outPath)
        .then(rowCount => {
            const fileCount = countFilesInDirectory("/home/hari/Downloads/packs");
            res.status(200).json({
                status: "success",
                data: {
                    rowCount,
                    fileCount
                }
            })
            return rowCount

        })
        .catch(error => {
            console.error(`Error: ${error.message}`);
        });
})

router.get("/atop", async (req, res, next) => {
    exec(`bash ${atopPath} -pv`, (error, stdout, stderr) => {
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

module.exports = router;