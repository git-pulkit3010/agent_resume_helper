# Resume Q&A CLI

 A command-line tool that lets you ask questions about resumes (PDF/DOCX) using the DeepSee
 API.

 ## Features

 - Load resumes in PDF or DOCX format
 - Clean and prepare resume text for analysis
 - Ask natural language questions about the resume content
 - Get AI-powered answers based on the resume information

 ## Prerequisites

 - Python 3.8+
 - pip package manager

 ## Installation

 1. Clone this repository:
    ```bash
    git clone https://github.com/yourusername/resume-qa-cli.git
    cd resume-qa-cli


 2 Create and activate a virtual environment (recommended):

    python -m venv venv
    source venv/bin/activate  # Linux/Mac
    venv\Scripts\activate     # Windows

 3 Install dependencies:

    pip install -r requirements.txt



                                       Configuration

 1 Create a .env file in the project root with your DeepSeek API key:

    DEEPSEEK_API_KEY=your_api_key_here

   Important: Never commit this file to version control. The .env file is included in
   .gitignore by default.
 2 Get your API key from DeepSeek's developer portal.


                                           Usage

Run the application:


 python main.py


The CLI will guide you through:

 1 Providing the path to your resume file (PDF or DOCX)
 2 Asking questions about the resume content
 3 Type 'exit' to quit the application


                                          Example


 $ python main.py
 📄 Resume Q&A CLI
 Ask questions based on a local resume!

 📂 Enter the full path to the resume file (PDF, DOCX, or DOC): ~/resumes/john_doe.pdf
 🔍 Extracting text from resume...
 ✅ Resume loaded and prepared successfully.

 You can now ask questions about the resume.
 Type 'exit' to quit.

 ❓ Your question: What programming languages does this candidate know?
 🧠 Thinking...
 📝 Answer: According to the resume, the candidate has experience with Python, JavaScript,
 and Java...



                                        Requirements

The following packages are required (automatically installed with requirements.txt):

 • python-dotenv - For environment variable management
 • pdfplumber - For PDF text extraction
 • python-docx - For DOCX text extraction
 • rich - For beautiful CLI formatting
 • requests - For API communication


                                      Troubleshooting

 • File not found: Ensure you provide the full absolute path to your resume file
 • API errors: Verify your DeepSeek API key is correct and has sufficient credits
 • Format issues: Currently only PDF and DOCX formats are supported


                                          License

This project is licensed under the MIT License - see the LICENSE file for details.



