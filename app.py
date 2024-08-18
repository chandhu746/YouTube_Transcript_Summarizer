import streamlit as st
from dotenv import load_dotenv
import os
import google.generativeai as genai
from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled
from fpdf import FPDF
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from docx import Document
from io import BytesIO


load_dotenv()  # Load all the environment variables

# Configure Google Gemini Pro
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    st.error("Google API Key is missing. Please check your environment variables.")
else:
    genai.configure(api_key=api_key)

prompt = """You are a YouTube video summarizer. You will be taking the transcript text
and summarizing the entire video, providing the important summary in points
within 250 words. Please provide the summary of the text given here: """

# Getting the transcript data from YT videos
def extract_transcript_details(youtube_video_url):
    try:
        video_id = youtube_video_url.split("=")[1]
        transcript_text = YouTubeTranscriptApi.get_transcript(video_id)

        transcript = ""
        for i in transcript_text:
            transcript += " " + i["text"]

        return transcript

    except TranscriptsDisabled:
        st.error("Transcripts are disabled for this video.")
    except Exception as e:
        st.error(f"An error occurred: {e}")

# Getting the summary based on Prompt from Google Gemini Pro
def generate_gemini_content(transcript_text, prompt):
    try:
        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content(prompt + transcript_text)
        return response.text
    except Exception as e:
        st.error(f"An error occurred while generating content: {e}")

def save_as_pdf(content):
    buffer = BytesIO()
    c = canvas.Canvas(buffer, pagesize=letter)
    width, height = letter
    text_object = c.beginText(40, height - 40)
    text_object.setFont("Helvetica", 12)

    for line in content.split('\n'):
        text_object.textLine(line)
    c.drawText(text_object)
    c.showPage()
    c.save()
    
    pdf_output = buffer.getvalue()
    buffer.close()
    return pdf_output


def save_as_word(content):
    doc = Document()
    doc.add_paragraph(content)
    word_output = BytesIO()
    doc.save(word_output)
    word_output.seek(0)
    return word_output.getvalue()

def save_as_markdown(content):
    return content

st.title("YouTube Transcript to Detailed Notes Converter")
youtube_link = st.text_input("Enter YouTube Video Link:")

if youtube_link:
    video_id = youtube_link.split("=")[1]
    st.image(f"http://img.youtube.com/vi/{video_id}/0.jpg", use_column_width=True)

if st.button("Get Detailed Notes"):
    transcript_text = extract_transcript_details(youtube_link)

    if transcript_text:
        summary = generate_gemini_content(transcript_text, prompt)
        if summary:
            st.markdown("## Detailed Notes:")
            st.write(summary)
            
            # Export as PDF
            pdf_output = save_as_pdf(summary)
            st.download_button(
                label="Download Summary as PDF",
                data=pdf_output,
                file_name='summary.pdf',
                mime='application/pdf'
            )
            
            # Export as Word Document
            word_output = save_as_word(summary)
            st.download_button(
                label="Download Summary as Word Document",
                data=word_output,
                file_name='summary.docx',
                mime='application/vnd.openxmlformats-officedocument.wordprocessingml.document'
            )

            # Export as Markdown
            markdown_output = save_as_markdown(summary)
            st.download_button(
                label="Download Summary as Markdown",
                data=markdown_output,
                file_name='summary.md',
                mime='text/markdown'
            )
