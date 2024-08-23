from models.base_model import BaseModel  
from models import storage  

class State(BaseModel):  
    """State class that represents a state in the AirBnB clone."""  

    name = ""  

    @property  
    def cities(self):  
        """Returns the list of City objects linked to the current State."""  
        return [city for city in storage.all(City).values() if city.state_id == self.id]  

    # Additional methods can be added here
