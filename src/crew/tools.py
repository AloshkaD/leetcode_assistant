 
from crewai_tools import BaseTool
from langsmith import traceable
class CaptureScreenTool(BaseTool):
    name: str = "Capture Screen"
    description: str = "Captures a screenshot of the current screen and returns the image file path."

    def _run(self) -> str:
        """
        Captures a screenshot and saves it to the screenshots directory.
        Returns the filepath of the saved screenshot.
        """
        timestamp = int(time.time())
        filepath = f'screenshots/screenshot_{timestamp}.png'
        screenshot = ImageGrab.grab()
        screenshot.save(filepath)
        return filepath

class ExtractQuestionTool(BaseTool):
    name: str = "Extract Question"
    description: str = "Extracts coding questions from the provided image path."

    def _run(self, image_path: str) -> str:
        """
        Extracts text from the image at the given path and identifies coding questions.
        """
        image = Image.open(image_path)
        text = pytesseract.image_to_string(image)
        # Use regex or NLP to find the coding question
        pattern = r"(?s)(?:(?:Problem|Question|Q\d*):\s*)(.*?)(?:\n\n|$)"
        matches = re.findall(pattern, text)
        question = matches[0].strip() if matches else None
        return question

class AnswerQuestionTool(BaseTool):
    name: str = "Answer Question"
    description: str = "Generates answers for coding questions using LLM and RAG."

    @traceable
    def _run(self, question: str) -> str:
        """
        Uses OpenAI's GPT-3.5 to answer the given coding question.
        Utilizes retrieved documents from the knowledge base to enhance the answer.
        """
        openai.api_key = "YOUR_OPENAI_API_KEY"  # Replace with your OpenAI API key
        kb = KnowledgeBase()
        docs = kb.search(question)
        context = "\n\n".join([doc.page_content for doc in docs])
        prompt = f"""
        Using the following context, answer the question:

        Context:
        {context}

        Question:
        {question}

        Answer:
        """
        response = openai.Completion.create(
            engine='gpt-3.5-turbo',
            prompt=prompt,
            max_tokens=500,
            temperature=0.7,
            n=1,
            stop=None
        )
        answer = response.choices[0].text.strip()
        return answer

class RAGSearchTool(BaseTool):
    name: str = "RAG Search"
    description: str = "Searches the knowledge base using RAG to find relevant information."

    def _run(self, query: str) -> list:
        """
        Searches the knowledge base using RAG to find relevant information.
        """
        kb = KnowledgeBase()
        documents = kb.search(query)
        return documents
