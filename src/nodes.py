import keyboard
from .crew.crew import CodingAssistantCrew
from .database import init_db, save_qa_pair
import weave

class Nodes:
    def __init__(self):
        self.crew = CodingAssistantCrew()  # Initialize the crew
        init_db()

    def log_event(self, event):
        # Log events using Weave
        pass

    def wait_for_next_trigger(self, state):
        print("## Waiting for Ctrl+S to be pressed")
        self.log_event("Waiting for Ctrl+S")
        keyboard.wait('ctrl+s')
        print("## Ctrl+S pressed, proceeding to capture and identify")
        self.log_event("Ctrl+S pressed")
        return state

    def capture_and_identify(self, state):
        self.log_event("Capturing screen and identifying question")
        
        # Kick off the crew to perform the task
        result = self.crew.kickoff(state)  # Executes crew tasks
        
        question = result.get('question')

        # Ensure question is set in state
        if question:
            state['question'] = question
            self.log_event(f"Question found: {question}")
        else:
            state['question'] = None
            self.log_event("No question found in the screenshot.")
        return state

    def check_question_found(self, state):
        return state

    def question_found(self, state):
        # Check if question exists in the state
        if state.get('question'):
            return 'found'
        else:
            return 'not_found'

    def handle_no_question(self, state):
        # Handle case when no question was found
        self.log_event("Handling situation where no question was found")
        task = self.crew.tasks.handle_no_question_task(self.crew.no_question_agent)
        task.run(state)
        return state

    def answer_question(self, state):
        # Answer the identified question
        question = state.get('question')
        if question:
            self.log_event("Answering the question")
            task = self.crew.tasks.answer_question_task(self.crew.answer_agent, question)
            result = task.run(state)
            answer = result.get('answer')
            #answer = "The moon is 4.5 billion years old."
            # Ensure answer is set in state
            if answer:
                state['answer'] = answer
                self.log_event(f"Answer generated: {answer}")
            else:
                self.log_event("Failed to generate an answer.")
        else:
            self.log_event("No question to answer")
        return state

    def store_result(self, state):
        self.log_event("Storing question and answer in the database")
        question = state.get('question')
        answer = state.get('answer')
        
        # Debugging: print the current state to see what values are present
        print(f"Question: {question}, Answer: {answer}")
        
        if question and answer:
            save_qa_pair(question, answer)
            self.log_event("Question and answer saved to database")
        else:
            self.log_event("No question or answer to save")
            # Add handling here to avoid errors when either field is missing
            if not question:
                self.log_event("No question found to save.")
            if not answer:
                self.log_event("No answer found to save.")
        
        return state

