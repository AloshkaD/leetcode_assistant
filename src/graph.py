'''from langgraph.graph import StateGraph
from .state import CodingAssistantState
from .nodes import Nodes
from .crew.crew import CodingAssistantCrew
class Workflow:
    def __init__(self):
        nodes = Nodes()
        workflow = StateGraph(CodingAssistantState)

        workflow.add_node("wait_for_next_trigger", nodes.wait_for_next_trigger)
        #workflow.add_node("capture_and_identify", nodes.capture_and_identify)
        workflow.add_node("capture_and_identify", CodingAssistantCrew().kickoff)
        workflow.add_node("check_question_found", nodes.check_question_found)
        workflow.add_node("handle_no_question", nodes.handle_no_question)
        workflow.add_node("answer_question", nodes.answer_question)
        workflow.add_node("store_result", nodes.store_result)

        workflow.set_entry_point("wait_for_next_trigger")
        workflow.add_edge("wait_for_next_trigger", "capture_and_identify")
        workflow.add_edge("capture_and_identify", "check_question_found")
        workflow.add_conditional_edges(
            "check_question_found",
            nodes.question_found,
            {
                "found": "answer_question",
                "not_found": "handle_no_question"
            }
        )
        workflow.add_edge("answer_question", "store_result")
        workflow.add_edge("handle_no_question", "wait_for_next_trigger")
        workflow.add_edge("store_result", "wait_for_next_trigger")
        self.app = workflow.compile()
'''

from langgraph.graph import StateGraph
from .state import CodingAssistantState
from .nodes import Nodes
from .crew.crew import CodingAssistantCrew

class Workflow:
    def __init__(self):
        nodes = Nodes()
        workflow = StateGraph(CodingAssistantState)

        workflow.add_node("wait_for_next_trigger", nodes.wait_for_next_trigger)

        # Explicitly kick off the crew here
        workflow.add_node("capture_and_identify", nodes.capture_and_identify)
        
        workflow.add_node("check_question_found", nodes.check_question_found)
        workflow.add_node("handle_no_question", nodes.handle_no_question)
        workflow.add_node("answer_question", nodes.answer_question)
        workflow.add_node("store_result", nodes.store_result)

        # Define the entry point and the edges for state transitions
        workflow.set_entry_point("wait_for_next_trigger")
        workflow.add_edge("wait_for_next_trigger", "capture_and_identify")
        workflow.add_edge("capture_and_identify", "check_question_found")
        
        # Conditional edge for question handling
        workflow.add_conditional_edges(
            "check_question_found",
            nodes.question_found,
            {
                "found": "answer_question",
                "not_found": "handle_no_question"
            }
        )
        
        # Continue to store result and loop back
        workflow.add_edge("answer_question", "store_result")
        workflow.add_edge("handle_no_question", "wait_for_next_trigger")
        workflow.add_edge("store_result", "wait_for_next_trigger")

        self.app = workflow.compile()
