const express = require('express');
const cors = require('cors');
const dotenv = require('dotenv');
const connectDB = require('./config/db');
const feedbackRoutes = require('./routes/feedback.routes');

dotenv.config();
const app = express();
app.use(cors());
app.use(express.json());

connectDB();

app.use('/api/feedbacks', feedbackRoutes);

const PORT = process.env.PORT || 5017;
app.listen(PORT, () => {
  console.log(`🚀 Feedback Service running on port ${PORT}`);
});