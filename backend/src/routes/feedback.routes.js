const express = require('express');
const router = express.Router();
const controller = require('../controllers/feedback.controller');

router.post('/', controller.createFeedback);
router.get('/', controller.getAllFeedback);

module.exports = router;