'''from crewai import Agent
from textwrap import dedent
from .tools import CaptureScreenTool, ExtractQuestionTool, AnswerQuestionTool, RAGSearchTool
 

class CodingAssistantAgents:
    def __init__(self):
        pass

    def screen_capture_agent(self):
        return Agent(
            role='Screen Capture Specialist',
            goal='Capture the screen and identify coding questions',
            backstory=dedent("""\
                As a Screen Capture Specialist, you have expertise in capturing screen content
                and extracting meaningful information, particularly coding questions.
                You are proficient in image processing and text extraction."""),
            tools=[
                CaptureScreenTool.capture_screen,
                ExtractQuestionTool.extract_question
            ],
            verbose=True,
            allow_delegation=True
        )

    def question_not_found_agent(self):
        return Agent(
            role='Question Investigation Expert',
            goal='Handle situations where no coding question is found',
            backstory=dedent("""\
                As a Question Investigation Expert, you excel at diagnosing why a coding question
                was not found and can provide guidance to the user on how to ensure the question
                is visible on the screen."""),
            verbose=True,
            allow_delegation=True
        )

    def answer_agent(self):
        return Agent(
            role='Coding Question Answerer',
            goal='Provide detailed answers to coding questions using advanced reasoning and RAG',
            backstory=dedent("""\
                You are a highly skilled software engineer with expertise in various programming languages
                and algorithms. You provide detailed and accurate answers to coding questions, utilizing
                advanced reasoning and retrieval augmented generation (RAG) for up-to-date information."""),
            tools=[
                AnswerQuestionTool.answer_question,
                RAGSearchTool.search_knowledge_base
            ],
            verbose=True,
            allow_delegation=False
        )
'''
# agents.py

from crewai import Agent
from textwrap import dedent
from .tools import CaptureScreenTool, ExtractQuestionTool, AnswerQuestionTool, RAGSearchTool

class CodingAssistantAgents:
    def __init__(self):
        pass

    def screen_capture_agent(self) -> Agent:
        return Agent(
            role='Screen Capture Specialist',
            goal='Capture the screen and identify coding questions',
            backstory=dedent("""\
                As a Screen Capture Specialist, you have expertise in capturing screen content
                and extracting meaningful information, particularly coding questions.
                You are proficient in image processing and text extraction."""),
            tools=[
                CaptureScreenTool(),
                ExtractQuestionTool()
            ],
            verbose=True,
            allow_delegation=True
        )

    def question_not_found_agent(self) -> Agent:
        return Agent(
            role='Question Investigation Expert',
            goal='Handle situations where no coding question is found',
            backstory=dedent("""\
                As a Question Investigation Expert, you excel at diagnosing why a coding question
                was not found and can provide guidance to the user on how to ensure the question
                is visible on the screen."""),
            verbose=True,
            allow_delegation=True
        )

    def answer_agent(self) -> Agent:
        return Agent(
            role='Coding Question Answerer',
            goal='Provide detailed answers to coding questions using advanced reasoning and RAG',
            backstory=dedent("""\
                You are a highly skilled software engineer with expertise in various programming languages
                and algorithms. You provide detailed and accurate answers to coding questions, utilizing
                advanced reasoning and retrieval augmented generation (RAG) for up-to-date information."""),
            tools=[
                AnswerQuestionTool(),
                RAGSearchTool()
            ],
            verbose=True,
            allow_delegation=False
        )
