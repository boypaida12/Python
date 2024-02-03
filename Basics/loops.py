users = [
    {
        "name": "John Doe",
        "age": 21, 
        "gender": "F",  
        "hobby": "Reading", 
        "skills": ["Communication", "Content creator"],
        "email": "jon@email.com",
        "in_distess": False,
        "lat": 4.245655464456,
      
    },
    {
        "name": "Olivia", 
        "age": 21, 
        "gender": "F",  
        "hobby": "Reading", 
        "skills": ["Communication", "Content creator"],
        "email": "jon@email.com",
        "in_distress": True,
        "lat": 4.245655444456,
    },
    {
        "name": "Suad", 
        "age": 21, 
        "gender": "F",  
        "hobby": "Reading", 
        "skills": ["Communication", "Content creator"],
        "email": "jon@email.com",
        "in_distress": True,
        "lat": 4.245655494456,
    },
    {
        "name": "Paolo", 
        "age": 23, 
        "gender": "M",  
        "hobby": "Reading", 
        "skills": ["Communication", "Content creator"],
        "email": "jon@email.com",
        "in_distress": True,
        "lat": 4.245655494456,
    },
]

for user in users:
    print(f'Name: {user.get("name")}, Email:  {user.get("email")}')
    if user.get("in_distress") == True:
        print(f'Contacting community for {user.get("name")}...')
    closest_users = filter()