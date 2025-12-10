import panda as pd
print("hello panda")
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],            
        'City': ['New York', 'Los Angeles', 'Chicago']}
df = pd.DataFrame(data)
print(df)