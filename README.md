# CarterSearch
**A simple web searcher and Q&amp;A template to use with [Carter](https://carterlabs.ai/)**

Uses DuckDuckGo API to search and get results.
<br>
(optionally) uses a carter agent to answer the original question BASED on the search results.
This results in more of an answer rather than just the scraped text. 

**Prompt format for summary with Carter**

**"&lt;block of text info>. &lt;question>. &lt;post prompt>"**

**Text Info:** raw search results
<br>
**Question:** question to be answered
<br>
**Post Prompt:** last part of the prompt telling the agent what to do with the text info and the question


**Default Post Prompt:** *"Don't say according to where you got the answer, just answer the question"*