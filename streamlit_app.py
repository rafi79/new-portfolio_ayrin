import streamlit as st
import pandas as pd
from PIL import Image
import base64

# Page Configuration
st.set_page_config(
    page_title="Fateha Jannat Ayrin - Portfolio",
    page_icon="👩‍💻",
    layout="wide"
)

# Custom CSS for styling
def local_css():
    st.markdown("""
    <style>
        .main {
            padding: 0rem 1rem;
        }
        .st-emotion-cache-1v0mbdj.e115fcil1 {
            margin-top: -75px;
        }
        h1, h2, h3 {
            color: #0e76a8;
        }
        .highlight {
            background-color: #f0f7fb;
            padding: 20px;
            border-radius: 10px;
            margin-bottom: 20px;
            border-left: 5px solid #0e76a8;
        }
        .skills span {
            background-color: #e7f3fe;
            padding: 5px 10px;
            border-radius: 15px;
            margin-right: 10px;
            margin-bottom: 10px;
            display: inline-block;
            font-size: 0.9em;
            color: #0e76a8;
            border: 1px solid #0e76a8;
        }
        .contact-info {
            padding: 10px;
            border-radius: 5px;
            margin-bottom: 20px;
        }
        .section-title {
            border-bottom: 2px solid #0e76a8;
            padding-bottom: 10px;
            margin-top: 30px;
        }
        .card {
            background-color: #ffffff;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            padding: 20px;
            margin-bottom: 20px;
        }
        .publication {
            border-left: 3px solid #0e76a8;
            padding-left: 15px;
            margin-bottom: 15px;
        }
        .timeline-item {
            margin-bottom: 20px;
            position: relative;
            padding-left: 30px;
        }
        .timeline-item:before {
            content: "";
            position: absolute;
            left: 0;
            top: 5px;
            width: 15px;
            height: 15px;
            border-radius: 50%;
            background-color: #0e76a8;
        }
        .timeline-item:after {
            content: "";
            position: absolute;
            left: 7px;
            top: 20px;
            bottom: -15px;
            width: 2px;
            background-color: #0e76a8;
        }
        .timeline-item:last-child:after {
            display: none;
        }
        .badge {
            background-color: #0e76a8;
            color: white;
            padding: 3px 10px;
            border-radius: 10px;
            font-size: 0.8em;
            margin-right: 10px;
        }
        .project-card {
            background-color: #f9f9f9;
            border-radius: 10px;
            padding: 15px;
            margin-bottom: 15px;
            border-left: 4px solid #0e76a8;
        }
    </style>
    """, unsafe_allow_html=True)

# Call the function to apply CSS
local_css()

# Navigation
def create_navbar():
    st.markdown("""
    <div style="display: flex; justify-content: space-around; padding: 10px; background-color: #f0f7fb; border-radius: 10px; margin-bottom: 20px;">
        <a href="#about" style="text-decoration: none; color: #0e76a8; font-weight: bold;">About</a>
        <a href="#experience" style="text-decoration: none; color: #0e76a8; font-weight: bold;">Experience</a>
        <a href="#education" style="text-decoration: none; color: #0e76a8; font-weight: bold;">Education</a>
        <a href="#research" style="text-decoration: none; color: #0e76a8; font-weight: bold;">Research</a>
        <a href="#projects" style="text-decoration: none; color: #0e76a8; font-weight: bold;">Projects</a>
        <a href="#skills" style="text-decoration: none; color: #0e76a8; font-weight: bold;">Skills</a>
        <a href="#certifications" style="text-decoration: none; color: #0e76a8; font-weight: bold;">Certifications</a>
        <a href="#contact" style="text-decoration: none; color: #0e76a8; font-weight: bold;">Contact</a>
    </div>
    """, unsafe_allow_html=True)

# Header Section
def header_section():
    col1, col2 = st.columns([1, 3])
    
    with col1:
        # Using a placeholder image - replace with your own image URL when deploying
        st.image("https://via.placeholder.com/300", width=220)
    
    with col2:
        st.title("Fateha Jannat Ayrin")
        st.subheader("Lecturer in Computer Science & Engineering")
        
        st.markdown("""
        <div class="highlight">
            As an educator and researcher, I am passionate about fostering the academic growth of students and creating
            an engaging learning environment. I am determined to mentor students, simplify complex concepts, and inspire
            critical thinking. My goal is to contribute to the academic community through effective teaching, guidance, and
            continuous learning.
        </div>
        """, unsafe_allow_html=True)
        
        with st.expander("Contact Information"):
            st.markdown("""
            <div class="contact-info">
                <p>📧 <b>Email:</b> fjayrin@gmail.com</p>
                <p>📱 <b>Phone:</b> +880 16 162 47349</p>
                <p>🔗 <b>GitHub:</b> <a href="https://github.com/ayrin21" target="_blank">github.com/ayrin21</a></p>
                <p>🔗 <b>LinkedIn:</b> <a href="https://www.linkedin.com/in/fateha-jannat-ayrin" target="_blank">linkedin.com/in/fateha-jannat-ayrin</a></p>
                <p>📍 <b>Present Address:</b> West High Level Road, Lalkhan Bazar, Chittagong, Bangladesh</p>
                <p>🏠 <b>Permanent Address:</b> Village: Jatarkul; PO: Hajir Para; Thana: Chandanaish; District: Chittagong</p>
            </div>
            """, unsafe_allow_html=True)

# About Section
def about_section():
    st.markdown('<h2 class="section-title" id="about">About Me</h2>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="card">
        I am a Lecturer in Computer Science & Engineering at Port City International University, Chittagong, Bangladesh. 
        My research focuses on Optical Character Recognition (OCR), deep learning, and natural language processing.
        
        <br><br>
        
        I have a strong background in web engineering and database management, and I am currently pursuing my Master's degree 
        in Computer Science & Engineering at the University of Chittagong. My academic journey has been marked by excellence, 
        with a CGPA of 3.73 out of 4 in my Bachelor's degree.
        
        <br><br>
        
        I am passionate about teaching and research, and I am committed to contributing to the academic community through 
        innovative research and effective teaching methods.
    </div>
    """, unsafe_allow_html=True)

# Experience Section
def experience_section():
    st.markdown('<h2 class="section-title" id="experience">Work Experience</h2>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="timeline-item card">
        <h3>Lecturer - Full Time</h3>
        <p><strong>Port City International University, Chittagong</strong> | Jan 2025 - Present</p>
        <p><em>Department of Computer Science & Engineering</em></p>
        <ul>
            <li>Taking different classes on Digital Logic Design (DLD), Computer Networking, Machine Learning, and various Engineering courses</li>
            <li>Mentoring students on research projects and academic development</li>
            <li>Contributing to curriculum development and department initiatives</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# Education Section
def education_section():
    st.markdown('<h2 class="section-title" id="education">Education</h2>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="card">
            <h3>Master of Science (Engineering) in CSE</h3>
            <p><strong>University of Chittagong</strong></p>
            <p>1st Semester, Ongoing (Session: 2022-2023)</p>
            <p><em>Working on OCR Technology with LVM in Final Year Thesis</em></p>
        </div>
        
        <div class="card">
            <h3>Bachelor of Science (Engineering) in CSE</h3>
            <p><strong>University of Chittagong</strong> | 2019 - 2022</p>
            <p><span class="badge">CGPA: 3.73/4.00</span></p>
            <p><em>Worked on OCR Technology for Blurred Images and Low Quality Images</em></p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="card">
            <h3>Higher Secondary Certificate</h3>
            <p><strong>BMS Girls' High School & College</strong> | 2016 - 2018</p>
            <p><span class="badge">GPA: 4.58/5.00</span></p>
        </div>
        
        <div class="card">
            <h3>Secondary School Certificate</h3>
            <p><strong>CMP School & College</strong> | 2006 - 2016</p>
            <p><span class="badge">GPA: 5.00/5.00</span></p>
        </div>
        """, unsafe_allow_html=True)

# Research Section
def research_section():
    st.markdown('<h2 class="section-title" id="research">Research & Publications</h2>', unsafe_allow_html=True)
    
    with st.expander("Final Year Thesis", expanded=True):
        st.markdown("""
        <div class="publication">
            <h3>An Optical Character Recognition Technique for Extracting Text from Blurred and Low Quality Images Using TrOCR</h3>
            <p><em>Accepted in IEEE ECCE - 2025</em></p>
            <ul>
                <li>Developed TrOCR system achieving 96.8% accuracy on IIIT 5K dataset</li>
                <li>Implemented TrOCR with VisionEncoderDecoder and Seq2Seq framework</li>
                <li><strong>Technologies:</strong> TrOCR, Seq2Seq, VisionEncoderDecoder</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with st.expander("Research Participation", expanded=True):
        st.markdown("""
        <div class="publication">
            <h3>Fine-Tuning LLMs for Regional Dialect Comprehended Question Answering in Bangla</h3>
            <p><em>Published in IEEE SCEECS 2025</em></p>
            <ul>
                <li>Created 12,500-sentence dataset from various Bangla dialects</li>
                <li>Achieved 53% BLEU score using ChatGPT-4 and LoRA fine-tuning</li>
                <li><strong>Technologies:</strong> LLMs, ChatGPT, LoRA</li>
            </ul>
        </div>
        
        <div class="publication">
            <h3>Fine-Tuning LLMs for Sentiment Classification of AI-Related Tweets</h3>
            <p><em>Published in IEEE WIECON-ECE 2024</em></p>
            <ul>
                <li>Analyzed 20,000 tweets using advanced prompt engineering</li>
                <li>Implemented successful classification using Llama 2</li>
                <li><strong>Technologies:</strong> LLMs, Llama2, Prompt Engineering</li>
            </ul>
        </div>
        
        <div class="publication">
            <h3>Towards Accurate Renal Micro-Structure Segmentation: An Assessment of YOLOv8 and Mask R-CNN Models</h3>
            <p><em>Published in IEEE WIECON-ECE 2024</em></p>
            <ul>
                <li>Achieved 84.55% IoU score using YOLOv8</li>
                <li>Applied Mask R-CNN for kidney structure detection</li>
                <li><strong>Technologies:</strong> YOLOv8, Mask R-CNN, Deep Learning</li>
            </ul>
        </div>
        
        <div class="publication">
            <h3>Deep Learning Analysis of COVID-19 Lung Infections in CT Scans</h3>
            <p><em>Published in IEEE AMATHE 2024 (Awarded as best paper)</em></p>
            <ul>
                <li>Developed 3D Unet model with 95.56% accuracy</li>
                <li><strong>Technologies:</strong> 3D UNet, Deep Learning, R-CNN</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

# Projects Section
def projects_section():
    st.markdown('<h2 class="section-title" id="projects">Projects</h2>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="project-card">
            <h3>JankenBou</h3>
            <p>A buy and selling platform for campus students</p>
            <ul>
                <li>Developed full-stack application using NodeJs and MongoDB</li>
                <li>Implemented real-time updates and user authentication</li>
            </ul>
        </div>
        
        <div class="project-card">
            <h3>Birdly - Bird Trading Platform</h3>
            <ul>
                <li>Developed comprehensive buy and selling platform using NodeJs and MongoDB</li>
                <li>Implemented frontend using HTML, CSS, and Bootstrap for responsive design</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="project-card">
            <h3>Flower Studio</h3>
            <ul>
                <li>Built Android app using Java and Firebase</li>
                <li>Integrated ML-based flower recognition system</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

# Skills Section
def skills_section():
    st.markdown('<h2 class="section-title" id="skills">Skills</h2>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="card">
        <h3>Web Engineering</h3>
        <div class="skills">
            <span>HTML</span>
            <span>CSS</span>
            <span>JavaScript</span>
            <span>Bootstrap5</span>
            <span>NodeJs</span>
        </div>
        
        <h3>Database</h3>
        <div class="skills">
            <span>MySQL</span>
            <span>PostgreSQL</span>
            <span>Oracle Database</span>
            <span>MongoDB</span>
        </div>
        
        <h3>Tools</h3>
        <div class="skills">
            <span>Git</span>
            <span>Trello</span>
            <span>MS Teams</span>
            <span>Canva</span>
        </div>
        
        <h3>Other Skills</h3>
        <div class="skills">
            <span>Software Documentation</span>
            <span>Software Testing</span>
            <span>Deep Learning</span>
            <span>OCR Technology</span>
            <span>LLM Fine-tuning</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Achievements Section
def achievements_section():
    st.markdown('<h2 class="section-title" id="achievements">Achievements & Awards</h2>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="card">
        <div class="timeline-item" style="padding-left: 30px;">
            <h3>Premire University IT Fest</h3>
            <p>January 2024</p>
            <p>Achieved 3rd position in the senior category, which focused on CSE-related topics.</p>
        </div>
        
        <div class="timeline-item" style="padding-left: 30px;">
            <h3>Information Technology Engineers Examination (ITEE)</h3>
            <p>March 2023</p>
            <p>Successfully achieved full passer status on the ITEE.</p>
        </div>
        
        <div class="timeline-item" style="padding-left: 30px;">
            <h3>6th International Girls' Programming Contest Participation</h3>
            <p>June 2022</p>
            <p>Demonstrated strong problem-solving skills and knowledge of CSE topics.</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Certifications Section
def certifications_section():
    st.markdown('<h2 class="section-title" id="certifications">Certifications</h2>', unsafe_allow_html=True)
    
    cert_data = {
        'Certification': [
            'Front-End Web UI Frameworks and Tools: Bootstrap 4',
            'Introduction to CSS3',
            'Interactivity with JavaScript',
            'Advanced Styling with Responsive Design',
            'Frontend Fundamentals',
            'Introduction to SQL Server',
            'Front-End Development'
        ],
        'Provider': [
            'The Hong Kong University of Science and Technology (Coursera)',
            'University of Michigan (Coursera)',
            'University of Michigan (Coursera)',
            'University of Michigan (Coursera)',
            'Pirple',
            'DataCamp',
            'SoloLearn'
        ],
        'Date': [
            'June 4, 2020',
            'April 27, 2020',
            'April 28, 2020',
            'April 29, 2020',
            'April 11, 2020',
            'May 22, 2020',
            'June 22, 2020'
        ]
    }
    
    cert_df = pd.DataFrame(cert_data)
    
    st.dataframe(cert_df, hide_index=True, use_container_width=True)

# Contact Section
def contact_section():
    st.markdown('<h2 class="section-title" id="contact">References</h2>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="card">
            <h3>Assistant Professor Abu Nowshed Chy</h3>
            <p>📧 nowshed@cu.ac.bd</p>
            <p>📱 +8801764207358</p>
        </div>
        
        <div class="card">
            <h3>Professor Dr. Kazi Ashrafuzzaman</h3>
            <p>📧 ashraf@cu.ac.bd</p>
            <p>📱 +8801717124315</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="card">
            <h3>Professor Muhammad Anwarul Azim</h3>
            <p>📧 azim@cu.ac.bd</p>
            <p>📱 +8801764207358</p>
        </div>
        
        <div class="card">
            <h3>Professor Dr. Mohammad Khairul Islam</h3>
            <p>📧 mkislam@cu.ac.bd</p>
            <p>📱 +8801919611867</p>
        </div>
        """, unsafe_allow_html=True)

# Footer Section
def footer_section():
    st.markdown("""
    <hr>
    <div style="text-align: center; padding: 20px; margin-top: 30px;">
        <p>&copy; 2025 Fateha Jannat Ayrin. All rights reserved.</p>
        <p>Made with ❤️ using Streamlit</p>
    </div>
    """, unsafe_allow_html=True)

# Main App
def main():
    create_navbar()
    header_section()
    about_section()
    experience_section()
    education_section()
    research_section()
    projects_section()
    skills_section()
    achievements_section()
    certifications_section()
    contact_section()
    footer_section()

if __name__ == "__main__":
    main()
