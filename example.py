from carterSearch import *

carter_search = CarterSearch()

# Get a raw output from DuckDuckGo
print("Raw Data")
output = carter_search.ask_raw("How much does the iphone 14 cost?")
print(output['output'])

# Get a summarized answer (using carter and prompting)
print("\nClean Answer")
output = carter_search.ask_answer("How much does the iphone 14 cost?")
print(output['output'])