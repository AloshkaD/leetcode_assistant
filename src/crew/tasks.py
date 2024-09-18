from crewai import Task
from textwrap import dedent
from langsmith import traceable
class CodingAssistantTasks:
    @traceable
    def capture_and_identify_task(self, agent):
        return Task(
            description=dedent("""\
                Use the 'Capture Screen' tool to take a screenshot of the current screen.
                Then, use the 'Extract Question' tool to identify any coding questions in the screenshot.
                If a question is found, store it in the state under 'question'.
                """),
            agent=agent
        )

    def handle_no_question_task(self, agent):
        return Task(
            description=dedent("""\
                Since no coding question was found, analyze possible reasons why.
                Provide guidance to the user on how to ensure the question is visible on the screen.
                """),
            agent=agent
        )

    def answer_question_task(self, agent, question):
        return Task(
            description=dedent(f"""\
                Use advanced reasoning and the 'Answer Question' tool to provide a detailed answer to the following question:
                "{question}"
                Use the 'RAG Search' tool to retrieve relevant information from the knowledge base to support your answer.
                Store the answer in the state under 'answer'.
                """),
            agent=agent
        )
