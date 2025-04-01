import streamlit as st
import pandas as pd
import requests

# Django backend API URL
BASE_URL = "http://127.0.0.1:8000/api/"

def make_clickable(link):
    return f'<a href="{link}" target="_blank">Download Resume</a>'

st.title("🚀 Recruitment System")

# Sidebar Navigation
menu = st.sidebar.radio("📌 Navigation", ["Post a Job", "View Jobs", "Apply for Job", "View Applications"])

# Post a Job
if menu == "Post a Job":
    st.header("📌 Post a Job Opening")
    job_title = st.text_input("Job Title")
    company = st.text_input("Company Name")
    location = st.text_input("Location")
    description = st.text_area("Job Description")
    
    if st.button("Post Job"):
        if job_title and company and location and description:
            job_data = {"title": job_title, "company": company, "location": location, "description": description}
            response = requests.post(BASE_URL + "jobs/", json=job_data)

            if response.status_code == 201:
                st.success("✅ Job posted successfully!")
            else:
                st.error(f"⚠️ Failed to post job. Error: {response.text}")
        else:
            st.warning("⚠️ Please fill all fields before posting.")

# View Jobs
elif menu == "View Jobs":
    st.header("📌 Available Job Openings")
    response = requests.get(BASE_URL + "jobs/")
    
    if response.status_code == 200:
        jobs = response.json()
        if jobs:
            df_jobs = pd.DataFrame(jobs)
            st.dataframe(df_jobs)  # Changed from st.table() for better formatting
        else:
            st.info("⚠️ No job postings available.")
    else:
        st.error(f"⚠️ Failed to fetch jobs. Error: {response.text}")

# Apply for a Job
elif menu == "Apply for Job":
    st.header("📌 Apply for a Job")
    response = requests.get(BASE_URL + "jobs/")

    if response.status_code == 200:
        jobs = response.json()
        if jobs:
            job_selected = st.selectbox("Select a Job", [job["title"] for job in jobs])
            selected_job = next(job for job in jobs if job["title"] == job_selected)
            job_id = selected_job["id"]
            name = st.text_input("Your Name")
            email = st.text_input("Your Email")
            resume = st.file_uploader("Upload Resume (PDF)", type=["pdf"])

            if st.button("Apply"):
                if name and email and resume:
                    files = {"resume": (resume.name, resume, "application/pdf")}
                    data = {"job": job_id, "name": name, "email": email}

                    response = requests.post(BASE_URL + "applications/create/", data=data, files=files)

                    if response.status_code == 201:
                        st.success("✅ Application submitted successfully!")
                    else:
                        st.error(f"⚠️ Failed to submit application. Error: {response.text}")
                else:
                    st.warning("⚠️ Please fill all fields and upload a resume before applying.")
        else:
            st.info("⚠️ No jobs available to apply for.")
    else:
        st.error(f"⚠️ Failed to fetch jobs. Error: {response.text}")

# View Applications
elif menu == "View Applications":
    st.header("📌 View Job Applications")
    response = requests.get(BASE_URL + "applications/")
    
    if response.status_code == 200:
        applications = response.json()
        if applications:
            df_apps = pd.DataFrame(applications)
            df_apps = df_apps.rename(columns={"name": "Applicant Name", "email": "Email", "resume": "Resume Link", "job": "Job ID"})
            df_apps["Resume Link"] = df_apps["Resume Link"].apply(make_clickable)

            # ✅ Displaying as an interactive table
            st.write(df_apps.to_html(escape=False, index=False), unsafe_allow_html=True)
        else:
            st.info("⚠️ No applications received yet.")
    else:
        st.error(f"⚠️ Failed to fetch applications. Error: {response.text}")
