
//Create a post
exports.upload = async (req, res, next) => {
  try {
    const {type,path}=req.body
    console.log(req);
    res.status(200).json({ publishStatus: "success" });
  } catch (error) {
    next(error);
  }
};
