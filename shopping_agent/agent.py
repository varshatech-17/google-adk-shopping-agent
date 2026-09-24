from google.adk.agents import Agent

from .tools import search_products, get_students_below_attendance


root_agent = Agent(
    name="shopping_agent",
    model="gemini-2.5-flash",
    instruction="""
    You are a helpful assistant for a college demonstration.

    You can help users with shopping-related requests and student attendance queries.

    When the user asks to find or search for products within a budget,
    use the search_products tool.

    When the user asks about student attendance,
    use the get_students_below_attendance tool.

    Use the appropriate tool whenever the user's request requires data
    from the available tools.

    Clearly present the results returned by the tools.
    Do not invent data that was not returned by the tools.
    """,
    tools=[
        search_products,
        get_students_below_attendance
    ]
)