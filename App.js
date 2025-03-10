// Frontend: App.js (React.js)
import React, { useState, useEffect } from 'react';

function App() {
    const [jobs, setJobs] = useState([]);
    const [name, setName] = useState('');
    const [email, setEmail] = useState('');
    const [jobId, setJobId] = useState('');

    useEffect(() => {
        fetch('http://localhost:5000/jobs')
            .then(res => res.json())
            .then(data => setJobs(data));
    }, []);

    const applyJob = async () => {
        await fetch('http://localhost:5000/apply', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ name, email, jobId })
        });
    };

    return (
        <div>
            <h1>Job Listings</h1>
            {jobs.map(job => (
                <div key={job._id}>
                    <h2>{job.title}</h2>
                    <p>{job.description}</p>
                    <button onClick={() => setJobId(job._id)}>Apply</button>
                </div>
            ))}
            <h2>Apply for a Job</h2>
            <input type="text" placeholder="Name" onChange={(e) => setName(e.target.value)} />
            <input type="email" placeholder="Email" onChange={(e) => setEmail(e.target.value)} />
            <button onClick={applyJob}>Submit</button>
        </div>
    );
}

export default App;
