exports.getAlarms = (req, res, next) => {
    try {
        res.status(200).json({
            msg: "hello",
            status: "success"
        })
    } catch (error) {
        next(error)
    }
}