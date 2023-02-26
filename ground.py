import os
import openai
import http.client
#class to handle and send response
class Ground():
    query=""
    def __init__(self):
        pass
    def setQuery(self,query):
        self.query=query
    def getQuery(self):
        openai.api_key = "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"
        response = openai.Completion.create(
                    model="text-davinci-003",
                    prompt=self.query,
                    temperature=0,
                    max_tokens=1000,
                    top_p=1,
                    frequency_penalty=0.5,
                    presence_penalty=0
                     )
        return response
    