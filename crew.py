from crewai import Crew,Process
from scripts.core.tasks import research_task,write_task
from scripts.core.agents import news_researcher,news_writer

## Forming the tech focused crew with some enhanced configuration
crew=Crew(
    agents=[news_researcher,news_writer],
    tasks=[research_task,write_task],
    process=Process.sequential,

)

## starting the task execution process wiht enhanced feedback
result=crew.kickoff(inputs={'topic':'GenAI usecases in cancer detection'})
print(result)