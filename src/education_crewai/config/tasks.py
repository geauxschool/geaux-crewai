from crewai import Task
from .agents import researcher, compiler

# Task for the Researcher Agent
research_task = Task(
    description=(
        "Identify grade-appropriate curriculum materials for a student. "
        "This includes textbooks, online courses, and other educational content relevant to the student's grade level. "
        "Focus on gathering comprehensive, reliable, and engaging resources."
    ),
    expected_output="A list of resources with links and brief descriptions.",
    agent=researcher,
)

# Task for the Compiler Agent
compilation_task = Task(
    description=(
        "Using the gathered materials, organize them into a structured educational program for the student. "
        "The program should cover all necessary subjects and be easy to follow."
    ),
    expected_output="A structured educational program in a detailed format, such as a syllabus or weekly plan.",
    agent=compiler,
)