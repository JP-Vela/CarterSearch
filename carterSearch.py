from duckduckgo_search import DDGS
import requests
import json

def carter_request(text, api_key, player_id, speak):
        headers = {"Content-Type": "application/json"}

        data=json.dumps({
                "text": text,
                "key": api_key,
                "playerId": player_id,
                "speak": speak
        })

        global response
        response = requests.post("https://api.carterlabs.ai/chat", headers=headers, data=data)
        return response.json()


"""
Prompt format for summary with Carter:

<block of text info>. <question>. <post prompt>

"""

class CarterSearch():
        def __init__(self):
                self.ddgs = DDGS()
                self.key = "3eafe49d-8753-472d-88ef-54e9736c5541" # Use for testing
                self.player = "defaultPlayer"

                # Last part of the prompt to steer the output into a simple answer
                # May need adjusting according to personality
                self.post_prompt = "Don't say according to where you got the answer, just answer the question"
                self.speak = "False"


        # Get 3 results from DuckDuckGo and put them together
        def DuckDuckSearch(self, query):
                results = self.ddgs.text(query, region='wt-wt', safesearch='Off')
                compile = []
                max_results = 3
                i=0

                for r in results:
                        if i>=max_results:
                                break
                        compile.append(r['body'])
                        i+=1

                output = ' '.join(compile)
                return output

        # Get compiled data and summarize it using carter
        def ask_answer(self, query):
                output = self.DuckDuckSearch(query)

                text = f"{output}. {query}. {self.post_prompt}"
                response = carter_request(text, self.key, self.player, self.speak)
       
                ret = {'output': response['output']['text']}
                return ret
        

        # Get compiled data
        def ask_raw(self, query):
                output = self.DuckDuckSearch(query)

                ret = {'output':output}
                return ret
        