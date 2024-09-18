 
from typing import TypedDict
from dataclasses import dataclass

#@dataclass
class CodingAssistantState(TypedDict):
    question: str
    answer: str
    # You can add more state variables if needed
