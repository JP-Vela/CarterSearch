from carterSearch import *

carter_search = CarterSearch()

# Get a raw output from DuckDuckGo
print("Raw Data")
output = carter_search.ask_raw("How fast is the apple m2 chip?")
print(output['output'])

# Get a summarized answer (using carter and prompting)
print("\nClean Answer")
output = carter_search.ask_answer("How fast is the apple m2 chip?")
print(output['output'])


# Using your own Carter agent
custom_search = CarterSearch("API KEY", "PLAYER ID", "POST PROMPT")