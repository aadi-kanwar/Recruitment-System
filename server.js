// Backend: server.js (Node.js with Express)
const express = require('express');
const mongoose = require('mongoose');
const cors = require('cors');
const jwt = require('jsonwebtoken');

const app = express();
app.use(express.json());
app.use(cors());

mongoose.connect('mongodb://localhost:27017/recruitment', {
    useNewUrlParser: true,
    useUnifiedTopology: true
});

const JobSchema = new mongoose.Schema({
    title: String,
    description: String,
    applicants: [{ type: mongoose.Schema.Types.ObjectId, ref: 'Applicant' }]
});
const ApplicantSchema = new mongoose.Schema({
    name: String,
    email: String,
    jobId: { type: mongoose.Schema.Types.ObjectId, ref: 'Job' }
});
const InterviewSchema = new mongoose.Schema({
    applicantId: { type: mongoose.Schema.Types.ObjectId, ref: 'Applicant' },
    status: String,
    feedback: String
});

const Job = mongoose.model('Job', JobSchema);
const Applicant = mongoose.model('Applicant', ApplicantSchema);
const Interview = mongoose.model('Interview', InterviewSchema);

// Routes
app.post('/jobs', async (req, res) => {
    const job = new Job(req.body);
    await job.save();
    res.json(job);
});

app.post('/apply', async (req, res) => {
    const applicant = new Applicant(req.body);
    await applicant.save();
    res.json(applicant);
});

app.post('/schedule', async (req, res) => {
    const interview = new Interview(req.body);
    await interview.save();
    res.json(interview);
});

app.post('/evaluate', async (req, res) => {
    const { applicantId, status, feedback } = req.body;
    await Interview.findOneAndUpdate({ applicantId }, { status, feedback });
    res.json({ message: 'Evaluation updated' });
});

app.listen(5000, () => console.log('Server running on port 5000'));