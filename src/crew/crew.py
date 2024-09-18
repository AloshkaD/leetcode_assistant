from crewai import Crew
from .agents import CodingAssistantAgents
from .tasks import CodingAssistantTasks

class CodingAssistantCrew:
    def __init__(self):
        agents = CodingAssistantAgents()
        self.capture_agent = agents.screen_capture_agent()
        self.no_question_agent = agents.question_not_found_agent()
        self.answer_agent = agents.answer_agent()
        self.tasks = CodingAssistantTasks()

    def kickoff(self, state):
        print("### Starting Coding Assistant Workflow")
        crew = Crew(
            agents=[self.capture_agent, self.no_question_agent, self.answer_agent],
            tasks=[
                self.tasks.capture_and_identify_task(self.capture_agent),
                # Subsequent tasks are managed by LangGraph
            ],
            verbose=True
        )
        result = crew.kickoff()
        return {**state, "result": result}
