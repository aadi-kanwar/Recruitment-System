import streamlit as st
import pandas as pd

# Apply custom CSS for sidebar styling
st.markdown(
    """
    <style>
        /* Style the sidebar background */
        [data-testid="stSidebar"] {
            background-color: #5f80a2;
            padding: 20px;
        }
        
        /* Increase font size and style for sidebar title */
        [data-testid="stSidebarNav"] {
            font-size: 50px !important;
            font-weight: bold !important;
            color: #4A90E2;
        }
        
        /* Style sidebar radio buttons */
        div[data-testid="stSidebar"] .stRadio label {
            font-size: 20px !important;
            font-weight: bold;
            color: #333;
            padding: 5px;
        }

        /* Highlight active option */
        div[data-testid="stSidebar"] .stRadio div[role="radiogroup"] label[data-selected="true"] {
            color: #fffff!important;
            background-color: #4A90E2 !important;
            padding: 8px;
            border-radius: 5px;
        }

        /* Style sidebar text inputs */
        div[data-testid="stSidebar"] input {
            font-size: 25px;
            padding: 8px;
        }

    </style>
    """,
    unsafe_allow_html=True
)


# Initialize session state for job listings and applications
if 'jobs' not in st.session_state:
    st.session_state.jobs = []
if 'applications' not in st.session_state:
    st.session_state.applications = []

st.title("🚀 Recruitment System")

# Sidebar Navigation with improved styling
menu = st.sidebar.radio("📌 Navigation", ["Post a Job", "View Jobs", "Apply for Job", "View Applications"])

# Job Posting
if menu == "Post a Job":
    st.header("📌 Post a Job Opening")
    job_title = st.text_input("Job Title")
    company = st.text_input("Company Name")
    location = st.text_input("Location")
    description = st.text_area("Job Description")
    if st.button("Post Job"):
        st.session_state.jobs.append({
            "Title": job_title,
            "Company": company,
            "Location": location,
            "Description": description
        })
        st.success("✅ Job posted successfully!")

# View Jobs
elif menu == "View Jobs":
    st.header("📌 Available Job Openings")
    if st.session_state.jobs:
        df_jobs = pd.DataFrame(st.session_state.jobs)
        st.table(df_jobs)
    else:
        st.info("⚠️ No job postings available.")

# Apply for a Job
elif menu == "Apply for Job":
    st.header("📌 Apply for a Job")
    if st.session_state.jobs:
        job_selected = st.selectbox("Select a Job", [job["Title"] for job in st.session_state.jobs])
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        resume = st.file_uploader("Upload Resume (PDF)", type=["pdf"])
        if st.button("Apply"):
            st.session_state.applications.append({
                "Name": name,
                "Email": email,
                "Job Applied": job_selected
            })
            st.success("✅ Application submitted successfully!")
    else:
        st.info("⚠️ No jobs available to apply for.")

# View Applications (for Recruiters)
elif menu == "View Applications":
    st.header("📌 View Job Applications")
    if st.session_state.applications:
        df_apps = pd.DataFrame(st.session_state.applications)
        st.table(df_apps)
    else:
        st.info("⚠️ No applications received yet.")
