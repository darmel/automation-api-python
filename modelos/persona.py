from pprint import pprint
from pydantic import BaseModel, Field
from uuid import uuid4
import json
from pprint import pprint

class Persona(BaseModel):
    fname: str 
    lname: str
    person_id: int
    timestamp: str 

    def generate_valid_data(self):
        unique_lname = str(uuid4())
        person = open('./resources/data/persona.json', 'r')
        person_json = json.load(person)
        person_json['lname'] = unique_lname
        payload = person_json
        return payload