const { getAlarms } = require("../controllers/ids")

const router=require("express").Router()

router.get("/alarms",getAlarms)

module.exports=router