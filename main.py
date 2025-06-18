# main.py

import os
from resume_loader import load_resume
from deepseek_client import ask_resume_question
from utils import clean_text, truncate_text
from rich.console import Console
from rich.prompt import Prompt
from rich.panel import Panel

console = Console()

def main():
    console.print(Panel.fit("📄 [bold cyan]Resume Q&A CLI[/bold cyan]\nAsk questions based on a local resume!", border_style="blue"))

    # Step 1: Get resume file path
    resume_path = Prompt.ask("📂 Enter the full path to the resume file (PDF, DOCX, or DOC)")

    try:
        console.print("[yellow]🔍 Extracting text from resume...[/yellow]")
        raw_text = load_resume(resume_path)

        # Clean and truncate text
        resume_text = clean_text(raw_text)
        resume_text = truncate_text(resume_text, max_chars=10000)

        console.print("[green]✅ Resume loaded and prepared successfully.[/green]\n")
    except Exception as e:
        console.print(f"[red]❌ Error:[/red] {str(e)}")
        return

    # Step 2: Ask questions
    console.print("[bold cyan]You can now ask questions about the resume.[/bold cyan]")
    console.print("[dim]Type 'exit' to quit.[/dim]\n")

    while True:
        user_question = Prompt.ask("❓ Your question")
        if user_question.strip().lower() == "exit":
            console.print("\n👋 [bold green]Goodbye![/bold green]")
            break

        try:
            console.print("[yellow]🧠 Thinking...[/yellow]")
            answer = ask_resume_question(resume_text, user_question)
            console.print(Panel.fit(answer.strip(), title="📝 Answer", border_style="green"))
        except Exception as e:
            console.print(f"[red]❌ API Error:[/red] {str(e)}")

if __name__ == "__main__":
    main()
