from notion.client import NotionClient
from datetime import date, timedelta
import re

# Obtain the `token_v2` value by inspecting your browser cookies on a logged-in (non-guest) session on Notion.so
client = NotionClient(token_v2="ba564b31318de3e0a8154ca80557ab822e19907606a59869d642fc587c798cf3c5e4986cc4dc63789f5903657360a447d04a76b393048d3b8fa12db3637f20d9a53bd3e253db52d814ab9fc3e21c")

# Replace this URL with the URL of the page you want to edit
page = client.get_block("https://www.notion.so/Test-task-figured-out-7dc855e4fa41411bb9a258532a94ba04")
cv = client.get_collection_view("https://www.notion.so/9e8f03199daf4a73a9001a2afcab9450?v=ce96bfaad03f4f599b01980c35d81cdc")

for row in cv.collection.get_rows():
    # print(type(row))
    if (row.get_property("status") == "DONE"):
        if(row.set_date.start > date.today()):
            pass

        elif(row.set_date.start == date.today()):
            row.status = "TO DO"
            print(f"{row.title} move to TODO")

        else:
            # ? Getting all data from periodicity
            periodicity_array = row.periodicity

            # ? Filtering by / or Daily
            for i in periodicity_array:
                pattern = re.compile("/")

                if(pattern.search(i) or i == "Daily"):
                    if(i == "Daily"):
                        row.set_date.start = row.due_date.start

                    elif("/w" in i):
                        print(row.set_date.start)
                        actual_date = row.set_date.start - timedelta(1)
                        row.set_date.start = actual_date
                        
                        print(actual_date)
                        # print(row.due_date.start)
                        
                        # now = row.set_date.start
                        # print(now)                      # 2017-05-03 17:46:44.558754
                        # two_days = timedelta(2)
                        # in_two_days = row.set_date.start - timedelta(2)
                        # print(in_two_days)              # 2017-05-05 17:46:44.558754
                    elif("/m" in i):
                        row.set_date.start = row.due_date.start - timedelta(days=7)

                    elif("/2m" in i or "/3m" in i):
                        row.set_date.start = row.due_date.start - timedelta(days=14)

                    else:
                        print("Non-supported format")
                        


            # print(row.set_date.start)



# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__',
# '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', 
# '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 
# '__weakref__', '_format_datetime', '_parse_datetime', 'end', 'from_notion', 'reminder', 'start', 'timezone', 'to_notion', 'type']
